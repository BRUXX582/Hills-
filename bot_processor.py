from ai_models import get_ai_model
from github_handler import GitHubHandler
import config
from typing import Optional

class BotProcessor:
    """Main processor for handling GitHub events"""
    
    def __init__(self):
        self.ai_model = get_ai_model()
        self.github = GitHubHandler()
    
    def process_issue_opened(self, issue_number: int, title: str, body: str) -> bool:
        """Process when an issue is opened"""
        if not config.ENABLE_ISSUE_RESPONSE:
            return False
        
        print(f"Processing issue #{issue_number}: {title}")
        
        prompt = f"""
        A new GitHub issue has been created:
        
        Title: {title}
        Body: {body}
        
        Please provide a helpful response that:
        1. Acknowledges the issue
        2. Offers initial guidance or clarification questions
        3. Suggests relevant documentation or resources
        4. If applicable, provides code examples
        """
        
        response = self.ai_model.generate_response(prompt)
        
        # Post comment to issue
        return self.github.create_issue_comment(issue_number, response)
    
    def process_issue_comment(self, issue_number: int, comment: str) -> bool:
        """Process when a comment is added to an issue"""
        if not config.ENABLE_ISSUE_RESPONSE:
            return False
        
        print(f"Processing comment on issue #{issue_number}")
        
        prompt = f"""
        A comment has been added to a GitHub issue:
        
        Comment: {comment}
        
        Please provide a helpful response that:
        1. Addresses the comment directly
        2. Provides relevant coding assistance or guidance
        3. Suggests solutions if applicable
        4. Maintains a professional tone
        """
        
        response = self.ai_model.generate_response(prompt)
        
        return self.github.create_issue_comment(issue_number, response)
    
    def process_pr_opened(self, pr_number: int, title: str, body: str) -> bool:
        """Process when a PR is opened"""
        if not config.ENABLE_PR_REVIEW:
            return False
        
        print(f"Processing PR #{pr_number}: {title}")
        
        # Get PR files for context
        files = self.github.get_pr_files(pr_number)
        files_str = ", ".join(files) if files else "No files"
        
        prompt = f"""
        A new Pull Request has been created:
        
        Title: {title}
        Description: {body}
        Files Changed: {files_str}
        
        Please provide a code review that includes:
        1. Summary of changes
        2. Code quality observations
        3. Potential issues or improvements
        4. Questions about implementation choices
        5. Suggestions for testing
        
        Be constructive and helpful.
        """
        
        response = self.ai_model.generate_response(prompt)
        
        return self.github.create_pr_review(pr_number, response)
    
    def process_pr_comment(self, pr_number: int, comment: str) -> bool:
        """Process when a comment is added to a PR"""
        if not config.ENABLE_PR_REVIEW:
            return False
        
        print(f"Processing comment on PR #{pr_number}")
        
        prompt = f"""
        A comment has been added to a Pull Request review:
        
        Comment: {comment}
        
        Please provide a relevant response that:
        1. Addresses the comment
        2. Provides code review feedback if applicable
        3. Suggests solutions or improvements
        4. Maintains professional tone
        """
        
        response = self.ai_model.generate_response(prompt)
        
        return self.github.create_pr_comment(pr_number, response)
    
    def process_discussion_created(self, discussion_title: str, discussion_body: str) -> bool:
        """Process when a discussion is created"""
        if not config.ENABLE_DISCUSSION_RESPONSE:
            return False
        
        print(f"Processing discussion: {discussion_title}")
        
        prompt = f"""
        A new GitHub Discussion has been created:
        
        Title: {discussion_title}
        Body: {discussion_body}
        
        Please provide a helpful response that:
        1. Engages with the discussion topic
        2. Provides relevant insights or resources
        3. Asks clarifying questions if needed
        4. Offers coding guidance if applicable
        """
        
        response = self.ai_model.generate_response(prompt)
        
        # Return True (actual posting would require discussions API)
        print(f"Response ready: {response}")
        return True
    
    def answer_coding_question(self, question: str, code_context: Optional[str] = None) -> str:
        """Answer a coding question with optional code context"""
        prompt = f"""
        A coding question has been asked:
        
        Question: {question}
        """
        
        if code_context:
            prompt += f"\nCode Context:\n{code_context}"
        
        prompt += """
        
        Please provide:
        1. Clear explanation of the solution
        2. Code examples if applicable
        3. Best practices
        4. Links to relevant documentation
        """
        
        return self.ai_model.generate_response(prompt, context=code_context)
