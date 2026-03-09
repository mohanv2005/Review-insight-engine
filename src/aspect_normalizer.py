ASPECT_GROUPS = {
    # story & writing
    "story": "story",
    "plot": "story",
    "script": "story",
    "screenplay": "story",
    "writing": "story",
    "narrative": "story",
    "climax": "story",
    "ending": "story",
    "twist": "story",
    "character": "story",
    "characters": "story",

    # acting
    "acting": "acting",
    "actor": "acting",
    "actress": "acting",
    "lead": "acting",
    "role": "acting",
    "performance": "acting",
    "cast": "acting",
    "ensemble": "acting",

    # visuals & production
    "visuals": "visuals",
    "visual": "visuals",
    "cinematography": "visuals",
    "scene": "visuals",
    "cgi": "visuals",
    "effects": "visuals",
    "vfx": "visuals",
    "lighting": "visuals",
    "set": "visuals",
    "costume": "visuals",
    "makeup": "visuals",

    # direction
    "direction": "direction",
    "director": "direction",
    "storytelling": "direction",
    "execution": "direction",

    # pacing & editing
    "pacing": "pacing",
    "editing": "pacing",
    "length": "pacing",
    "runtime": "pacing",
    "middle": "pacing",

    # audio & music
    "music": "music",
    "background": "music",
    "score": "music",
    "soundtrack": "music",
    "sound": "music",
    "audio": "music",

    # dialogue
    "dialogue": "dialogue",
    "dialogues": "dialogue"
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