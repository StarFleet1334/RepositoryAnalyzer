from config.config import Config
from file_filter_strategy.dependencyFileFilter import FileFilterStrategy, DependencyFileFilter
from formatter.outputFormatter import OutputFormatter
from github_api.github_api import GitHubAPIClient
from processor.commitProcessor import CommitProcessor


class GitHubRepoClientFacade:
    def __init__(self, config: Config, file_filter: FileFilterStrategy = None):
        self.config = config
        self.api_client = GitHubAPIClient(config.owner, config.repo, config.github_token)
        self.file_filter = file_filter or DependencyFileFilter()
        self.commit_processor = CommitProcessor(self.api_client, self.file_filter)
        self.output_formatter = OutputFormatter()

    def run(self):
        filename_counts, author_counts, commits = self.commit_processor.get_all_relevant_filenames_and_author_counts()
        self.output_formatter.print_filenames_summary(filename_counts)
        print("======================================================")
        self.output_formatter.print_contributors_summary(author_counts)

def main():
    config = Config()
    client_facade = GitHubRepoClientFacade(config)
    client_facade.run()

if __name__ == "__main__":
    main()