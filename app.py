from flask import Flask, request, jsonify
import hmac
import hashlib
import json
from bot_processor import BotProcessor
import config

app = Flask(__name__)
processor = BotProcessor()


def verify_webhook_signature(payload_body, signature):
    """Verify GitHub webhook signature"""
    if not config.WEBHOOK_SECRET:
        return True  # Skip verification if no secret configured
    
    expected_signature = 'sha256=' + hmac.new(
        config.WEBHOOK_SECRET.encode(),
        payload_body,
        hashlib.sha256
    ).hexdigest()
    
    return hmac.compare_digest(signature, expected_signature)


@app.route('/webhook', methods=['POST'])
def webhook():
    """Handle GitHub webhooks"""
    
    # Verify signature
    signature = request.headers.get('X-Hub-Signature-256', '')
    payload_body = request.get_data()
    
    if not verify_webhook_signature(payload_body, signature):
        return jsonify({'error': 'Invalid signature'}), 401
    
    try:
        data = request.json
        event_type = request.headers.get('X-GitHub-Event')
        
        print(f"Received webhook event: {event_type}")
        
        if event_type == 'issues':
            handle_issue_event(data)
        elif event_type == 'pull_request':
            handle_pr_event(data)
        elif event_type == 'issue_comment':
            handle_issue_comment_event(data)
        elif event_type == 'pull_request_review_comment':
            handle_pr_comment_event(data)
        elif event_type == 'discussion':
            handle_discussion_event(data)
        
        return jsonify({'status': 'success'}), 200
    
    except Exception as e:
        print(f"Error processing webhook: {e}")
        return jsonify({'error': str(e)}), 500


def handle_issue_event(data):
    """Handle issue events"""
    action = data.get('action')
    issue = data.get('issue', {})
    issue_number = issue.get('number')
    title = issue.get('title')
    body = issue.get('body', '')
    
    if action == 'opened':
        processor.process_issue_opened(issue_number, title, body)
    elif action == 'labeled':
        # Could trigger analysis based on labels
        pass


def handle_pr_event(data):
    """Handle pull request events"""
    action = data.get('action')
    pr = data.get('pull_request', {})
    pr_number = pr.get('number')
    title = pr.get('title')
    body = pr.get('body', '')
    
    if action == 'opened':
        processor.process_pr_opened(pr_number, title, body)
    elif action == 'synchronize':
        # Handle new commits pushed to PR
        pass


def handle_issue_comment_event(data):
    """Handle issue comment events"""
    action = data.get('action')
    
    if action == 'created':
        issue = data.get('issue', {})
        comment = data.get('comment', {})
        issue_number = issue.get('number')
        comment_body = comment.get('body')
        
        processor.process_issue_comment(issue_number, comment_body)


def handle_pr_comment_event(data):
    """Handle pull request comment events"""
    action = data.get('action')
    
    if action == 'created':
        pr = data.get('pull_request', {})
        comment = data.get('comment', {})
        pr_number = pr.get('number')
        comment_body = comment.get('body')
        
        processor.process_pr_comment(pr_number, comment_body)


def handle_discussion_event(data):
    """Handle discussion events"""
    action = data.get('action')
    discussion = data.get('discussion', {})
    title = discussion.get('title')
    body = discussion.get('body', '')
    
    if action == 'created':
        processor.process_discussion_created(title, body)


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'}), 200


@app.route('/', methods=['GET'])
def home():
    """Home endpoint"""
    return jsonify({
        'name': 'Hiils Bot',
        'version': '1.0.0',
        'status': 'running'
    }), 200


if __name__ == '__main__':
    # For development: python app.py
    # For production: use gunicorn or similar
    app.run(host='0.0.0.0', port=5000, debug=False)
