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
