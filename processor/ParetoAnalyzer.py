from typing import Dict, List, Tuple

class ParetoAnalyzer:
    @staticmethod
    def perform_pareto_analysis(data: Dict[str, int], threshold: float = 80.0) -> List[Tuple[str, int, int, float]]:
        sorted_items = sorted(data.items(), key=lambda x: x[1], reverse=True)
        total = sum(data.values())
        cumulative = 0
        pareto_items = []

        for key, count in sorted_items:
            cumulative += count
            cumulative_pct = (cumulative / total) * 100
            pareto_items.append((key, count, cumulative, cumulative_pct))
            if cumulative_pct >= threshold:
                break

        return pareto_items
