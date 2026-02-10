import pandas as pd

# Import preprocessing, aspect extraction, and sentiment scoring logic
from src.preprocessing import preprocess_review
from src.aspect_extraction import extract_aspects
from src.sentiment_analysis import score_aspect_sentiment


def main():
    
    df = pd.read_csv("data/movies_reviews.csv")

    # Select one review for demonstration (first review)
    review = df.loc[0, "review_text"]

    print("Original Review:\n")
    print(review)

    tokens = preprocess_review(review)

    print("\nClean Tokens:\n")
    print(tokens)

    aspects = extract_aspects(review)

    print("\nExtracted Aspects:\n")
    print(aspects)

    print("\nAspect-wise Sentiment Scores:\n")

    for aspect in aspects:
        score = score_aspect_sentiment(tokens, aspect)

        print(f"{aspect} → {score}")


if __name__ == "__main__":
    main()
