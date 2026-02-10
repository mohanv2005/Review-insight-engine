import pandas as pd

from src.preprocessing import preprocess_review
from src.aspect_extraction import extract_aspects
from src.sentiment_analysis import score_aspect_sentiment
from src.insight_generator import generate_insights
from src.aspect_normalizer import normalize_aspects


def main():
    """
    Pipeline:
    1. Load review data
    2. Preprocess review text
    3. Extract aspects
    4. Compute aspect-wise sentiment scores
    5. Normalize / group related aspects
    6. Generate human-readable insights
    """

    df = pd.read_csv("data/movies_reviews.csv")

    review = df.loc[0, "review_text"]

    tokens = preprocess_review(review)

    aspects = extract_aspects(review)

    aspect_sentiments = {}

    for aspect in aspects:
        score = score_aspect_sentiment(tokens, aspect)
        aspect_sentiments[aspect] = score

    print("\nAspect-wise Sentiment Scores (Before Normalization):\n")
    for aspect, score in aspect_sentiments.items():
        print(f"{aspect} → {score}")

    normalized_aspects = normalize_aspects(aspect_sentiments)

    print("\nNormalized Aspect Sentiment Scores:\n")
    for aspect, score in normalized_aspects.items():
        print(f"{aspect} → {score}")

    print("\nGenerated Insights:\n")
    insights = generate_insights(normalized_aspects)

    for insight in insights:
        print("-", insight)


if __name__ == "__main__":
    main()
