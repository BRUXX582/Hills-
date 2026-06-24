import os
from dotenv import load_dotenv

load_dotenv()

# GitHub Configuration
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPOSITORY = os.getenv("GITHUB_REPOSITORY", "BRUXX582/Hills-")

# AI Model Configuration
AI_MODEL = os.getenv("AI_MODEL", "gpt-4")  # Options: gpt-4, claude, llama
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
LLAMA_API_URL = os.getenv("LLAMA_API_URL", "http://localhost:11434")

# Model Parameters
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "1000"))
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))

# Features
ENABLE_PR_REVIEW = os.getenv("ENABLE_PR_REVIEW", "true").lower() == "true"
ENABLE_ISSUE_RESPONSE = os.getenv("ENABLE_ISSUE_RESPONSE", "true").lower() == "true"
ENABLE_DISCUSSION_RESPONSE = os.getenv("ENABLE_DISCUSSION_RESPONSE", "true").lower() == "true"
MAX_CODE_CONTEXT_LINES = int(os.getenv("MAX_CODE_CONTEXT_LINES", "100"))

# Webhook Configuration
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")
