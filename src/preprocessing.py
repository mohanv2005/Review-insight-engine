import re
import spacy
from nltk.corpus import stopwords

# Load stopwords
stop_words = set(stopwords.words('english'))

# Load spaCy model
nlp = spacy.load("en_core_web_sm")


def preprocess_review(review):
    
    # Convert to lowercase and remove punctuation/numbers
    review = review.lower()
    review = re.sub(r'[^a-z\s]', '', review)

    doc = nlp(review)
    clean_tokens = []

    # Lemmatize and remove stop words and short tokens
    for token in doc: 
        if token.text in stop_words:
            continue
        if len(token.text) <= 2:
            continue
        clean_tokens.append(token.lemma_)

    return clean_tokens
