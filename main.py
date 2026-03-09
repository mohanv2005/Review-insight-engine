import pandas as pd
import os

from src.preprocessing import preprocess_review
from src.aspect_extraction import extract_aspects
from src.aspect_filter import filter_aspects
from src.sentiment_analysis import score_aspect_sentiment
from src.aspect_normalizer import normalize_aspects
from src.aspect_ranking import get_top_aspects
from src.insight_generator import generate_insights
from src.export_results import save_aspect_scores, save_insights, plot_aspect_sentiments


def main():

    print("\nRunning Review Insights Engine...\n")

    # Ensure outputs folder exists
    os.makedirs("outputs", exist_ok=True)

    # Load dataset
    df = pd.read_csv("data/movies_reviews.csv")

    # Dictionary to store cumulative sentiment scores
    aspect_totals = {}

    # Process each review
    for review in df["review_text"]:

        # Preprocess review text
        tokens = preprocess_review(review)

        # Extract aspects using NLP
        aspects = extract_aspects(review)

        # Remove irrelevant aspects
        aspects = filter_aspects(aspects)

        # Compute sentiment score for each aspect
        for aspect in aspects:

            score = score_aspect_sentiment(tokens, aspect)

            # Add score to cumulative totals
            aspect_totals[aspect] = aspect_totals.get(aspect, 0) + score


    # Normalize similar aspects
    normalized_aspects = normalize_aspects(aspect_totals)

    # Rank aspects
    top_positive, top_negative = get_top_aspects(normalized_aspects)

    # Generate human-readable insights
    insights = generate_insights(normalized_aspects)

    # Save outputs to files
    save_aspect_scores(normalized_aspects)
    save_insights(insights)
    plot_aspect_sentiments(normalized_aspects)

    print("Analysis complete.\n")
    print("Results saved to the 'outputs' folder:")
    print(" - aspect_scores.csv")
    print(" - insights.txt")
    print(" - aspect_sentiment_chart.png\n")


if __name__ == "__main__":
    main()