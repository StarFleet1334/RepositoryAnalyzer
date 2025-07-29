class OutputFormatter:
    @staticmethod
    def _print_summary(title: str, data: dict, label: str):
        print(f"\n{title}")
        if not data:
            print(f"  No {label.lower()} were found.")
            return

        max_key_length = max(len(key) for key in data.keys())
        print(f"\n{label.ljust(max_key_length)} | Count")
        print(f"{'-' * max_key_length}-|-------")

        for key, count in sorted(data.items(), key=lambda x: x[1], reverse=True):
            print(f"{key.ljust(max_key_length)} | {str(count).rjust(6)}")

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
