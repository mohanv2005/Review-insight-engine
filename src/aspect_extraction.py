import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")


def extract_aspects(text):
    doc = nlp(text.lower())
    aspects = []

    for token in doc:
        # POS tag NOUN or PROPN (proper noun)
        if token.pos_ in ["NOUN", "PROPN"]:
            # Ignore very short or meaningless nouns
            if len(token.text) > 2:
                aspects.append(token.lemma_)

    return aspects
