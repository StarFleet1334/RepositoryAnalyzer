from collections import defaultdict
from typing import Any, Tuple, Dict, List

from file_filter_strategy.dependencyFileFilter import FileFilterStrategy
from github_api.github_api import GitHubAPIClient


def get_commit_author(details: Any):
    author_data = details.get("author")
    if author_data and "login" in author_data:
        return author_data["login"]

    commit_author = details.get("commit", {}).get("author", {})
    return commit_author.get("name", "Unknown Author")


class CommitProcessor:
    def __init__(self, api_client: GitHubAPIClient, file_filter: FileFilterStrategy):
        self.api_client = api_client
        self.file_filter = file_filter

    def get_commit_filenames(self, sha: str):
        details = self.api_client.get_commit_details(sha)
        files = details.get("files", [])
        filenames = [
            file_info.get("filename") for file_info in files
            if not self.file_filter.is_excluded(file_info.get("filename"))
        ]
        return filenames

    def get_all_relevant_filenames_and_author_counts(self) -> Tuple[Dict[str, int], Dict[str, int], List[Any]]:
        commits = self.api_client.get_all_commits()
        filename_counts = defaultdict(int)
        author_counts = defaultdict(int)

        for commit in commits:
            sha = commit.get("sha")
            if not sha:
                continue

            filenames = self.get_commit_filenames(sha)
            for filename in filenames:
                filename_counts[filename] += 1

            commit_details = self.api_client.get_commit_details(sha)
            author = get_commit_author(commit_details)
            author_counts[author] += 1

        return filename_counts, author_counts, commits