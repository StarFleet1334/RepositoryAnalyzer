import os

from config.config import Config
from file_filter_strategy.dependencyFileFilter import FileFilterStrategy, DependencyFileFilter
from formatter.outputFormatter import OutputFormatter
from github_api.github_api import GitHubAPIClient
from processor.ParetoAnalyzer import ParetoAnalyzer
from processor.commitProcessor import CommitProcessor
from processor.paretoChartVisualizer import ParetoChartVisualizer


class GitHubRepoClientFacade:
    def __init__(self, config: Config, file_filter: FileFilterStrategy = None):
        self.config = config
        self.api_client = GitHubAPIClient(config.owner, config.repo, config.github_token)
        self.file_filter = file_filter or DependencyFileFilter()
        self.commit_processor = CommitProcessor(self.api_client, self.file_filter)
        self.output_formatter = OutputFormatter()
        self.pareto_analyzer = ParetoAnalyzer()

    def save_markdown_report(self, filename_pareto, contributor_pareto, path="reports"):
        os.makedirs(path, exist_ok=True)
        with open(f"{path}/pareto_summary.md", "w") as f:
            f.write("# 📌 Pareto Analysis Report\n\n## Files\n\n")
            for file, count, cum, pct in filename_pareto:
                f.write(f"- **{file}**: {count} commits ({pct:.2f}%)\n")

            f.write("\n## Contributors\n\n")
            for contributor, count, cum, pct in contributor_pareto:
                f.write(f"- **{contributor}**: {count} commits ({pct:.2f}%)\n")

    def run(self):
        filename_counts, author_counts, commits = self.commit_processor.get_all_relevant_filenames_and_author_counts()

        # Original summaries
        self.output_formatter.print_filenames_summary(filename_counts)
        print("=" * 80)
        self.output_formatter.print_contributors_summary(author_counts)

        # Pareto Analysis Summaries
        filename_pareto = self.pareto_analyzer.perform_pareto_analysis(filename_counts)
        contributor_pareto = self.pareto_analyzer.perform_pareto_analysis(author_counts)

        self.save_markdown_report(filename_pareto, contributor_pareto)

        print("=" * 80)
        self.output_formatter.print_pareto_summary(
            filename_pareto, label="Filename",
            title="📌 Pareto Analysis for Files (80%)"
        )

        print("=" * 80)
        self.output_formatter.print_pareto_summary(
            contributor_pareto, label="Contributor",
            title="📌 Pareto Analysis for Contributors (80%)"
        )

        # Visualization (Interactive Pareto Chart)
        ParetoChartVisualizer.show_interactive_pareto_chart(
            data=filename_counts,
            title="📊 Pareto Chart - File Changes",
            xlabel="Files",
            ylabel="Number of Commits"
        )

        ParetoChartVisualizer.show_interactive_pareto_chart(
            data=author_counts,
            title="👥 Pareto Chart - Contributor Activity",
            xlabel="Contributors",
            ylabel="Number of Commits"
        )

def main():
    config = Config()
    client_facade = GitHubRepoClientFacade(config)
    client_facade.run()

if __name__ == "__main__":
    main()
