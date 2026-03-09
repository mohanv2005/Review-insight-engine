ASPECT_GROUPS = {

    # story
    "story": "story",
    "plot": "story",
    "script": "story",
    "screenplay": "story",
    "climax": "story",

    # acting
    "acting": "acting",
    "actor": "acting",
    "lead": "acting",
    "role": "acting",
    "performance": "acting",
    "cast": "acting",

    # visuals
    "cinematography": "visuals",
    "visual": "visuals",
    "scene": "visuals",

    # direction
    "direction": "direction",
    "storytelling": "direction",

    # music
    "music": "music",
    "background": "music",
    "score": "music",

    # dialogue
    "dialogue": "dialogue"
}


def normalize_aspects(aspect_sentiments):
    normalized = {}

    for aspect, score in aspect_sentiments.items():
        grouped_aspect = ASPECT_GROUPS.get(aspect, aspect)

        if grouped_aspect in normalized:
            normalized[grouped_aspect] += score
        else:
            normalized[grouped_aspect] = score

    return normalized