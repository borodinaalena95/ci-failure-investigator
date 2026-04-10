import os
from dotenv import load_dotenv


load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")