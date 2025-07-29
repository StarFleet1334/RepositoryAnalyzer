from typing import Dict, List, Tuple
import numpy as np

class ParetoAnalyzer:
    @staticmethod
    def perform_pareto_analysis(data: Dict[str, int], threshold: float = 80.0):
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

    @staticmethod
    def prepare_plotly_data(data: Dict[str, int]) -> Tuple[List[str], List[int], np.ndarray, np.ndarray]:
        sorted_items = sorted(data.items(), key=lambda x: x[1], reverse=True)
        keys, values = zip(*sorted_items)
        cum_values = np.cumsum(values)
        cum_percentage = 100 * cum_values / cum_values[-1]

        return list(keys), list(values), cum_values, cum_percentage
