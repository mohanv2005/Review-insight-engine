import pandas as pd
import matplotlib.pyplot as plt


def save_aspect_scores(aspect_scores):

    df = pd.DataFrame(
        aspect_scores.items(),
        columns=["Aspect", "Sentiment Score"]
    )

    df.to_csv("outputs/aspect_scores.csv", index=False)

def save_insights(insights):

    with open("outputs/insights.txt", "w") as f:

        f.write("Generated Insights\n\n")

        for insight in insights:
            f.write("- " + insight + "\n")



def plot_aspect_sentiments(aspect_scores):

    aspects = list(aspect_scores.keys())
    scores = list(aspect_scores.values())

    plt.figure(figsize=(10,5))

    plt.bar(aspects, scores)

    plt.title("Aspect Sentiment Scores")
    plt.xlabel("Aspect")
    plt.ylabel("Sentiment Score")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("outputs/aspect_sentiment_chart.png")