import pandas as pd

from src.preprocessing import preprocess_review
from src.aspect_extraction import extract_aspects
from src.sentiment_analysis import score_aspect_sentiment
from src.insight_generator import generate_insights
from src.aspect_filter import filter_aspects
from src.aspect_normalizer import normalize_aspects
from src.aspect_ranking import get_top_aspects


def main():
    
    df = pd.read_csv("data/movies_reviews.csv")

    aspect_totals = {}

    for review in df["review_text"]:

        tokens = preprocess_review(review)
        aspects = extract_aspects(review)
        aspects = filter_aspects(aspects)

        # compute sentiment score for each aspect
        for aspect in aspects:

            score = score_aspect_sentiment(tokens, aspect)

            # If aspect already exists → add score
            if aspect in aspect_totals:
                aspect_totals[aspect] += score
            else:
                aspect_totals[aspect] = score

    print("\nAspect-wise Sentiment Scores (Before Normalization):\n")

    for aspect, score in aspect_totals.items():
        print(f"{aspect} → {score}")

    # Normalize similar aspects (actor → acting etc.)
    normalized_aspects = normalize_aspects(aspect_totals)

    print("\nNormalized Aspect Sentiment Scores:\n")

    
    # Get top positive and negative aspects
    top_positive, top_negative = get_top_aspects(normalized_aspects)
    print("\nTop Positive Aspects:\n")
    for aspect, score in top_positive:
        print(f"{aspect} (+{score})")

    print("\nTop Negative Aspects:\n")
    for aspect, score in top_negative:
        print(f"{aspect} ({score})")

    for aspect, score in normalized_aspects.items():
        print(f"{aspect} → {score}")

    # Generate human readable insights
    print("\nGenerated Insights:\n")

    insights = generate_insights(normalized_aspects)

    for insight in insights:
        print("-", insight)


if __name__ == "__main__":
    main()