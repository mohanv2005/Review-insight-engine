import json
import os

# Load sentiment lexicon safely
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEXICON_PATH = os.path.join(BASE_DIR, "lexicons", "movie_sentiment_lexicon.json")

with open(LEXICON_PATH, "r") as f:
    SENTIMENT_LEXICON = json.load(f)


def score_aspect_sentiment(tokens, aspect, window_size=3):
    """
    Scores sentiment for a given aspect based on nearby sentiment words.

    Args:
        tokens (list): Clean tokens from preprocessing
        aspect (str): Aspect word (noun)
        window_size (int): How many words to look around the aspect

    Returns:
        sentiment_score (int)
    """

    score = 0

    for i, token in enumerate(tokens):
        if token == aspect:
            # Look at words around the aspect
            start = max(0, i - window_size)
            end = min(len(tokens), i + window_size + 1)

            for j in range(start, end):
                word = tokens[j]
                if word in SENTIMENT_LEXICON:
                    score += SENTIMENT_LEXICON[word]

    return score
