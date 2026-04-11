import html
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

_CHARTS_DIR = "static"


def _ensure_charts_dir():
    os.makedirs(_CHARTS_DIR, exist_ok=True)

def save_aspect_scores(aspect_scores, output_dir):

    df = pd.DataFrame(
        aspect_scores.items(),
        columns=["Aspect", "Sentiment Score"]
    )

    file_path = os.path.join(output_dir, "aspect_scores.csv")
    df.to_csv(file_path, index=False)


def save_insights(insights, output_dir):

    file_path = os.path.join(output_dir, "insights.txt")
    with open(file_path, "w", encoding="utf-8") as f:

        f.write("Generated Insights\n\n")

        for insight in insights:
            f.write("- " + insight + "\n")


def plot_aspect_sentiments(aspect_scores, output_dir):

    aspects = list(aspect_scores.keys())
    scores = list(aspect_scores.values())

    plt.figure(figsize=(10,5))

    plt.bar(aspects, scores)

    plt.title("Aspect Sentiment Scores")
    plt.xlabel("Aspect")
    plt.ylabel("Sentiment Score")

    plt.xticks(rotation=45)

    plt.tight_layout()

    _ensure_charts_dir()
    file_path = os.path.join(_CHARTS_DIR, "aspect_sentiment_chart.png")
    plt.savefig(file_path)
    plt.close()


def plot_top_aspects(top_positive, top_negative, output_dir):

    pos_aspects = [a[0] for a in top_positive]
    pos_scores = [a[1] for a in top_positive]

    neg_aspects = [a[0] for a in top_negative]
    neg_scores = [a[1] for a in top_negative]

    plt.figure(figsize=(10,5))

    plt.bar(pos_aspects, pos_scores, label="Positive Aspects", color='green')
    plt.bar(neg_aspects, neg_scores, label="Negative Aspects", color='red')

    plt.title("Top Positive vs Negative Aspects")
    plt.xlabel("Aspect")
    plt.ylabel("Sentiment Score")

    plt.legend()
    plt.tight_layout()

    _ensure_charts_dir()
    file_path = os.path.join(_CHARTS_DIR, "top_aspects_chart.png")
    plt.savefig(file_path)
    plt.close()


def generate_html_report(movie_name, summary, insights, aspect_scores, output_dir):

    safe_movie = html.escape(str(movie_name))
    safe_summary = html.escape(str(summary))

    rows = ""
    for aspect, score in aspect_scores.items():
        rows += (
            f"<tr><td>{html.escape(str(aspect))}</td>"
            f"<td>{html.escape(str(score))}</td></tr>"
        )

    insights_html = ""
    for insight in insights:
        insights_html += f"<li>{html.escape(str(insight))}</li>"

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Review Insights Engine — Report</title>
    <link rel="stylesheet" href="/static/css/theme.css">
</head>
<body>
    <div class="site-wrap">
        <header class="site-header">
            <h1 class="site-title">Review Insights Engine</h1>
            <p class="site-subtitle">Aspect-based sentiment analysis from your uploaded reviews.</p>
            <span class="report-badge">Analysis report</span>
        </header>

        <div class="content-stack">
            <section class="card">
                <h2 class="card-title">Movie name</h2>
                <p class="card-body">{safe_movie}</p>
            </section>

            <section class="card">
                <h2 class="card-title">Summary</h2>
                <p class="card-body">{safe_summary}</p>
            </section>

            <section class="card">
                <h2 class="card-title">Key insights</h2>
                <ul class="insight-list card-body">
                    {insights_html}
                </ul>
            </section>

            <section class="card">
                <h2 class="card-title">Aspect sentiment scores</h2>
                <div class="data-table-wrap">
                    <table class="data-table">
                        <thead>
                            <tr>
                                <th>Aspect</th>
                                <th>Score</th>
                            </tr>
                        </thead>
                        <tbody>
                            {rows}
                        </tbody>
                    </table>
                </div>
            </section>

            <section class="card">
                <h2 class="card-title">Aspect sentiment distribution</h2>
                <figure class="figure-block">
                    <img class="report-img" src="/static/aspect_sentiment_chart.png" alt="Aspect sentiment bar chart">
                </figure>
            </section>

            <section class="card">
                <h2 class="card-title">Top positive vs negative aspects</h2>
                <figure class="figure-block">
                    <img class="report-img" src="/static/top_aspects_chart.png" alt="Top positive vs negative aspects chart">
                </figure>
            </section>

            <section class="card report-footer">
                <a href="/" class="btn btn-primary" role="button">Upload Another CSV</a>
            </section>
        </div>
    </div>
</body>
</html>
"""

    file_path = os.path.join(output_dir, "report.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)