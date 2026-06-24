from github import Github
from github.Repository import Repository
from github.Issue import Issue
from github.PullRequest import PullRequest
import config
from typing import Optional, List

class GitHubHandler:
    """Handles interactions with GitHub API"""
    
    def __init__(self):
        self.g = Github(config.GITHUB_TOKEN)
        self.repo = self.get_repository()
    
    def get_repository(self) -> Repository:
        """Get the GitHub repository"""
        try:
            owner, repo = config.GITHUB_REPOSITORY.split('/')
            return self.g.get_user(owner).get_repo(repo)
        except Exception as e:
            print(f"Error getting repository: {e}")
            return None
    
    def get_issue(self, issue_number: int) -> Optional[Issue]:
        """Get an issue by number"""
        try:
            return self.repo.get_issue(issue_number)
        except Exception as e:
            print(f"Error getting issue: {e}")
            return None
    
    def get_pull_request(self, pr_number: int) -> Optional[PullRequest]:
        """Get a pull request by number"""
        try:
            return self.repo.get_pull(pr_number)
        except Exception as e:
            print(f"Error getting PR: {e}")
            return None
    
    def get_file_content(self, file_path: str, ref: str = "main") -> Optional[str]:
        """Get file content from repository"""
        try:
            content = self.repo.get_contents(file_path, ref=ref)
            return content.decoded_content.decode('utf-8')
        except Exception as e:
            print(f"Error getting file content: {e}")
            return None
    
    def create_issue_comment(self, issue_number: int, comment: str) -> bool:
        """Create a comment on an issue"""
        try:
            issue = self.get_issue(issue_number)
            if issue:
                issue.create_comment(comment)
                return True
        except Exception as e:
            print(f"Error creating issue comment: {e}")
        return False
    
    def create_pr_comment(self, pr_number: int, comment: str) -> bool:
        """Create a comment on a pull request"""
        try:
            pr = self.get_pull_request(pr_number)
            if pr:
                pr.create_issue_comment(comment)
                return True
        except Exception as e:
            print(f"Error creating PR comment: {e}")
        return False
    
    def create_pr_review(self, pr_number: int, comment: str, event: str = "COMMENT") -> bool:
        """Create a review on a pull request"""
        try:
            pr = self.get_pull_request(pr_number)
            if pr:
                pr.create_review(body=comment, event=event)
                return True
        except Exception as e:
            print(f"Error creating PR review: {e}")
        return False
    
    def get_pr_files(self, pr_number: int) -> List[str]:
        """Get list of files changed in a PR"""
        try:
            pr = self.get_pull_request(pr_number)
            if pr:
                return [file.filename for file in pr.get_files()]
        except Exception as e:
            print(f"Error getting PR files: {e}")
        return []
    
    def get_pr_diff(self, pr_number: int) -> Optional[str]:
        """Get diff for a pull request"""
        try:
            pr = self.get_pull_request(pr_number)
            if pr:
                return pr.get_commits()[0].commit.message if pr.get_commits().totalCount > 0 else None
        except Exception as e:
            print(f"Error getting PR diff: {e}")
        return None
