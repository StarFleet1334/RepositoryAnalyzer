import requests
import os
from dotenv import load_dotenv

load_dotenv()

class GitHubRepoClient:
    def __init__(self, owner: str, repo: str, token: str):
        self.owner = owner
        self.repo = repo
        self.token = token
        self.base_url = f"https://api.github.com/repos/{self.owner}/{self.repo}"

    def _get_headers(self):
        return {
            "Accept": "application/vnd.github+json",
            "Authorization": f"token {self.token}"
        }

    def get_all_commits(self):
        """Fetches all commits from the GitHub repository with paging."""
        commits = []
        page = 1
        per_page = 100

        while True:
            url = f"{self.base_url}/commits?page={page}&per_page={per_page}"
            response = requests.get(url, headers=self._get_headers())
            response.raise_for_status()
            current_page_commits = response.json()

            if not current_page_commits:
                break

            commits.extend(current_page_commits)
            page += 1

        return commits


if __name__ == "__main__":
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    OWNER = os.getenv("OWNER")
    REPO = os.getenv("REPO")

    if not GITHUB_TOKEN:
        raise ValueError("GITHUB_TOKEN environment variable is not set.")

    client = GitHubRepoClient(OWNER, REPO, GITHUB_TOKEN)
    all_commits = client.get_all_commits()
    print(f"Fetched {len(all_commits)} commits.")
