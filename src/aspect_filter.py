ALLOWED_ASPECTS = {
    "acting",
    "actor",
    "performance",
    "lead",
    "role",
    "cast",

    "story",
    "plot",
    "script",
    "screenplay",
    "climax",

    "visual",
    "cinematography",
    "scene",

    "direction",
    "storytelling",

    "music",
    "background",
    "score",

    "dialogue",

    "pacing",
    "execution"
}


def filter_aspects(aspects):

    filtered = []

    for aspect in aspects:
        if aspect in ALLOWED_ASPECTS:
            filtered.append(aspect)

    return filtered