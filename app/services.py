from config.config import Config
from github_api.github_api import GitHubAPIClient
from processor.commitProcessor import CommitProcessor
from processor.ParetoAnalyzer import ParetoAnalyzer
from processor.paretoChartVisualizer import ParetoChartVisualizer
from file_filter_strategy.dependencyFileFilter import DependencyFileFilter


def run_pareto_analysis(owner, repo, token):
    config = Config()
    config.owner = owner
    config.repo = repo
    config.github_token = token

    api_client = GitHubAPIClient(owner, repo, token)
    commit_processor = CommitProcessor(api_client, DependencyFileFilter())
    pareto_analyzer = ParetoAnalyzer()

    filename_counts, author_counts, _ = commit_processor.get_all_relevant_filenames_and_author_counts()

    filename_pareto = pareto_analyzer.perform_pareto_analysis(filename_counts)
    contributor_pareto = pareto_analyzer.perform_pareto_analysis(author_counts)

    ParetoChartVisualizer.save_pareto_chart_image(filename_counts, "File Changes", "Files", "Commits", filename="file_changes_pareto.png")
    ParetoChartVisualizer.save_pareto_chart_image(author_counts, "Contributor Activity", "Contributors", "Commits", filename="contributor_activity_pareto.png")

    return {
        "files": filename_pareto,
        "contributors": contributor_pareto
    }
