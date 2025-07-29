from typing import List, Tuple


class OutputFormatter:
    @staticmethod
    def _print_summary(title: str, data: dict, label: str):
        print(f"\n{title}")
        if not data:
            print(f"  No {label.lower()} were found.")
            return

        sorted_items = sorted(data.items(), key=lambda x: x[1], reverse=True)
        total_count = sum(count for _, count in sorted_items)

        max_key_len = max(len(label), max(len(key) for key in data.keys()))
        max_count_len = max(len("Count"), max(len(str(v)) for v in data.values()))
        max_cum_freq_len = len("Cumulative Frequency")
        max_cum_pct_len = len("Cumulative Frequency Percentage (%)")

        print(
            f"\n{label.ljust(max_key_len)} | "
            f"{'Count'.rjust(max_count_len)} | "
            f"{'Cumulative Frequency'.rjust(max_cum_freq_len)} | "
            f"{'Cumulative Frequency Percentage (%)'.rjust(max_cum_pct_len)}"
        )
        print(
            f"{'-' * max_key_len}-|"
            f"{'-' * (max_count_len + 2)}|"
            f"{'-' * (max_cum_freq_len + 2)}|"
            f"{'-' * (max_cum_pct_len + 3)}"
        )

        cumulative = 0
        for key, count in sorted_items:
            cumulative += count
            percentage = (cumulative / total_count) * 100
            print(
                f"{key.ljust(max_key_len)} | "
                f"{str(count).rjust(max_count_len)} | "
                f"{str(cumulative).rjust(max_cum_freq_len)} | "
                f"{f'{percentage:.2f}%'.rjust(max_cum_pct_len)}"
            )

    @staticmethod
    def print_pareto_summary(pareto_data: List[Tuple[str, int, int, float]], label: str, title: str):
        if not pareto_data:
            print(f"No data available for {label}.")
            return

        max_label_len = max(len(label), max(len(key) for key, _, _, _ in pareto_data))
        count_width = max(len("Count"), max(len(str(count)) for _, count, _, _ in pareto_data))
        cum_freq_width = len("Cumulative")
        cum_pct_width = len("Cum. %")

        print(f"\n{title}")
        print(
            f"{label.ljust(max_label_len)} | "
            f"{'Count'.rjust(count_width)} | "
            f"{'Cumulative'.rjust(cum_freq_width)} | "
            f"{'Cum. %'.rjust(cum_pct_width)}"
        )
        print("-" * (max_label_len + count_width + cum_freq_width + cum_pct_width + 9))

        for key, count, cumulative, percentage in pareto_data:
            print(
                f"{key.ljust(max_label_len)} | "
                f"{str(count).rjust(count_width)} | "
                f"{str(cumulative).rjust(cum_freq_width)} | "
                f"{f'{percentage:.2f}%'.rjust(cum_pct_width)}"
            )

    @staticmethod
    def print_filenames_summary(filename_counts: dict):
        OutputFormatter._print_summary(
            title="📂 Summary of File Changes Across All Commits:",
            data=filename_counts,
            label="Filename"
        )

    @staticmethod
    def print_contributors_summary(contributor_counts: dict):
        OutputFormatter._print_summary(
            title="👤 Summary of Contributors Across All Commits:",
            data=contributor_counts,
            label="Contributor Name"
        )
