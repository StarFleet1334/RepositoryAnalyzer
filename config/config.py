import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    def __init__(self):
        self.github_token = os.getenv("GITHUB_TOKEN")
        self.owner = os.getenv("OWNER")
        self.repo = os.getenv("REPO")
        self.validate()

    def validate(self):
        if not self.github_token:
            raise ValueError("GITHUB_TOKEN environment variable is not set.")
        if not self.owner or not self.repo:
            raise ValueError("OWNER and REPO environment variables must be set.")
