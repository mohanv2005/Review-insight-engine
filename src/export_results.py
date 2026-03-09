import pandas as pd
import matplotlib.pyplot as plt
import os

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

    file_path = os.path.join(output_dir, "aspect_sentiment_chart.png")
    plt.savefig(file_path)
    plt.close() # Good practice to close the plot to free up memory


def plot_top_aspects(top_positive, top_negative, output_dir):

    pos_aspects = [a[0] for a in top_positive]
    pos_scores = [a[1] for a in top_positive]

    neg_aspects = [a[0] for a in top_negative]
    neg_scores = [a[1] for a in top_negative]

    plt.figure(figsize=(10,5))

    plt.bar(pos_aspects, pos_scores, label="Positive Aspects", color='green') # Added color for clarity
    plt.bar(neg_aspects, neg_scores, label="Negative Aspects", color='red') # Added color for clarity

    plt.title("Top Positive vs Negative Aspects")
    plt.xlabel("Aspect")
    plt.ylabel("Sentiment Score")

    plt.legend()

    plt.tight_layout()

    file_path = os.path.join(output_dir, "top_aspects_chart.png")
    plt.savefig(file_path)
    plt.close() # Good practice to close the plot


def generate_html_report(movie_name, summary, insights, aspect_scores, output_dir):

    rows = ""
    for aspect, score in aspect_scores.items():
        rows += f"<tr><td>{aspect}</td><td>{score}</td></tr>"

    insights_html = ""
    for insight in insights:
        insights_html += f"<li>{insight}</li>"

    html_content = f"""
    <html>
    <head>
        <title>Review Insights Engine Report</title>

        <style>
        body {{
            font-family: Arial;
            margin: 40px;
            background-color: #f4f6f8;
        }}

        h1 {{
            color: #2c3e50;
        }}

        h2 {{
            color: #34495e;
        }}

        .card {{
            background: white;
            padding: 20px;
            margin-bottom: 25px;
            border-radius: 8px;
            box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
        }}

        table {{
            border-collapse: collapse;
            width: 100%;
        }}

        th, td {{
            border: 1px solid #ddd;
            padding: 10px;
        }}

        th {{
            background-color: #2c3e50;
            color: white;
        }}

        img {{
            width: 700px;
            margin-top: 15px;
        }}
        </style>
    </head>

    <body>

        <h1>Review Insights Engine</h1>

        <div class="card">
            <h2>Movie</h2>
            <p>{movie_name}</p>
        </div>

        <div class="card">
            <h2>Summary</h2>
            <p>{summary}</p>
        </div>

        <div class="card">
            <h2>Key Insights</h2>
            <ul>
            {insights_html}
            </ul>
        </div>

        <div class="card">
            <h2>Aspect Sentiment Scores</h2>

            <table>
            <tr>
                <th>Aspect</th>
                <th>Score</th>
            </tr>

            {rows}

            </table>
        </div>

        <div class="card">
            <h2>Aspect Sentiment Distribution</h2>
            <img src="aspect_sentiment_chart.png">
        </div>

        <div class="card">
            <h2>Top Positive vs Negative Aspects</h2>
            <img src="top_aspects_chart.png">
        </div>

    </body>
    </html>
    """

    file_path = os.path.join(output_dir, "report.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)