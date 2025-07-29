import os

from processor.ParetoAnalyzer import ParetoAnalyzer

import plotly.graph_objects as go

class ParetoChartVisualizer:
    @staticmethod
    def show_interactive_pareto_chart(data: dict, title: str, xlabel: str, ylabel: str, top_n: int = 40):
        keys, values, cum_values, cum_percentage = ParetoAnalyzer.prepare_plotly_data(data)

        # Limiting to top N, setting to high number should plot all, but it gets tighter, still
        # since we use plotly, it is interactive so anyone who users service can easily inspect
        keys, values, cum_values, cum_percentage = (
            keys[:top_n],
            values[:top_n],
            cum_values[:top_n],
            cum_percentage[:top_n]
        )

        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=keys,
            y=values,
            name='Frequency',
            marker=dict(color='steelblue')
        ))

        fig.add_trace(go.Scatter(
            x=keys,
            y=cum_percentage,
            name='Cumulative %',
            mode='lines+markers+text',
            text=[f'{p:.0f}%' for p in cum_percentage],
            textposition='top center',
            line=dict(color='crimson'),
            yaxis='y2'
        ))

        fig.update_layout(
            title=title + f" (Top {top_n})",
            xaxis_title=xlabel,
            yaxis=dict(title=ylabel),
            yaxis2=dict(
                title='Cumulative Percentage (%)',
                overlaying='y',
                side='right',
                range=[0, 110]
            ),
            legend=dict(x=0.75, y=0.95),
            template='plotly_white'
        )

        fig.show()

    @staticmethod
    def save_pareto_chart_image(data, title, xlabel, ylabel, filename="pareto_chart.png"):
        sorted_items = sorted(data.items(), key=lambda x: x[1], reverse=True)
        labels, counts = zip(*sorted_items)

        cumulative = []
        total = sum(counts)
        cum_sum = 0
        for c in counts:
            cum_sum += c
            cumulative.append(cum_sum / total * 100)

        fig = go.Figure()

        fig.add_trace(go.Bar(x=labels, y=counts, name="Commits", marker=dict(color="steelblue")))

        fig.add_trace(go.Scatter(x=labels, y=cumulative, name="Cumulative %", yaxis="y2", mode="lines+markers",
                                 line=dict(color="orange")))

        fig.update_layout(
            title=title,
            xaxis=dict(title=xlabel),
            yaxis=dict(title=ylabel),
            yaxis2=dict(
                title="Cumulative %",
                overlaying="y",
                side="right",
                range=[0, 100],
                showgrid=False
            ),
            legend=dict(x=0.01, y=0.99),
            margin=dict(l=60, r=60, t=80, b=150),
            height=600,
            width=1000
        )

        for path in ["app/static", "reports"]:
            os.makedirs(path, exist_ok=True)
            full_path = os.path.join(path, filename)
            fig.write_image(full_path)
            print(f"Saved Pareto chart to: {full_path}")