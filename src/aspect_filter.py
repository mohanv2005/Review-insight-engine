from src.aspect_normalizer import ASPECT_GROUPS

ALLOWED_ASPECTS = set(ASPECT_GROUPS.keys())

def filter_aspects(aspects):
    filtered = []

    for aspect in aspects:
        if aspect in ALLOWED_ASPECTS:
            filtered.append(aspect)

    return filtered