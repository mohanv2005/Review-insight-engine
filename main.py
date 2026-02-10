import pandas as pd

from src.preprocessing import preprocess_review
from src.aspect_extraction import extract_aspects
from src.sentiment_analysis import score_aspect_sentiment
from src.insight_generator import generate_insights


def main():
    df = pd.read_csv("data/movies_reviews.csv")
    review = df.loc[0, "review_text"]

    tokens = preprocess_review(review)
    aspects = extract_aspects(review)

    # Store aspect → sentiment score
    aspect_sentiments = {}

    for aspect in aspects:
        score = score_aspect_sentiment(tokens, aspect)
        aspect_sentiments[aspect] = score

    print("\nAspect-wise Sentiment Scores:\n")
    for aspect, score in aspect_sentiments.items():
        print(f"{aspect} → {score}")

    print("\nGenerated Insights:\n")
    insights = generate_insights(aspect_sentiments)

    for insight in insights:
        print("-", insight)


if __name__ == "__main__":
    main()
