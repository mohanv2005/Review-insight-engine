import pandas as pd
import os
import argparse

from src.preprocessing import preprocess_review
from src.aspect_extraction import extract_aspects
from src.aspect_filter import filter_aspects
from src.sentiment_analysis import score_aspect_sentiment
from src.aspect_normalizer import normalize_aspects
from src.aspect_ranking import get_top_aspects
from src.insight_generator import generate_insights, generate_summary
from src.export_results import (
    save_aspect_scores,
    save_insights,
    plot_aspect_sentiments,
    plot_top_aspects,
    generate_html_report
)

def run_pipeline(input_path, output_dir):

    print("\nRunning Review Insights Engine...\n")

    # Use the dynamic output directory instead of a hardcoded "outputs" folder
    os.makedirs(output_dir, exist_ok=True)

    df = pd.read_csv(input_path)
    movie_name = df["movie"].iloc[0]

    aspect_totals = {}

    for review in df["review_text"]:

        # Step 1: Preprocess text
        tokens = preprocess_review(review)

        # Step 2: Extract aspects
        aspects = extract_aspects(review)

        # Step 3: Filter irrelevant aspects
        aspects = filter_aspects(aspects)

        # Step 4: Score sentiment for each aspect
        for aspect in aspects:
            score = score_aspect_sentiment(tokens, aspect)
            aspect_totals[aspect] = aspect_totals.get(aspect, 0) + score

    # Step 5: Normalize aspects
    normalized_aspects = normalize_aspects(aspect_totals)

    # Step 6: Rank aspects
    top_positive, top_negative = get_top_aspects(normalized_aspects)

    # Step 7: Generate insights
    insights = generate_insights(normalized_aspects)

    # Step 8: Generate summary
    summary = generate_summary(normalized_aspects)

    # Step 9: Export results (passing the output directory)
    save_aspect_scores(normalized_aspects, output_dir)
    save_insights(insights, output_dir)

    plot_aspect_sentiments(normalized_aspects, output_dir)
    plot_top_aspects(top_positive, top_negative, output_dir)

    # Step 10: Generate HTML report
    generate_html_report(movie_name, summary, insights, normalized_aspects, output_dir)

    print("Analysis complete.\n")

    print("Summary:\n")
    print(summary)

    print(f"\nResults successfully saved in the '{output_dir}' folder!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Review Insights Engine")

    parser.add_argument("--input", type=str, default="data/movies_reviews.csv", help="Path to input CSV")
    parser.add_argument("--output", type=str, default="outputs", help="Directory to save output files")
    
    args = parser.parse_args()
    
    # Pass both arguments into the main function
    run_pipeline(args.input, args.output)