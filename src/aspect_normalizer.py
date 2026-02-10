ASPECT_GROUPS = {
    "story": "story",
    "plot": "story",
    "script": "story",

    "acting": "acting",
    "performance": "acting",

    "direction": "direction",
    "storytelling": "direction",

    "cinematography": "visuals",
    "visuals": "visuals"
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