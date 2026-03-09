def score_to_label(score):
    if score >= 3:
        return "strongly positive"
    elif score > 0:
        return "positive"
    elif score == 0:
        return "neutral"
    else:
        return "negative"


def generate_insights(aspect_sentiments):

    insights = []

    # Sort aspects by sentiment strength
    sorted_aspects = sorted(
        aspect_sentiments.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for aspect, score in sorted_aspects:

        # Skip neutral aspects to avoid weak insights
        if score == 0:
            continue

        sentiment_label = score_to_label(score)

        if sentiment_label == "strongly positive":
            insights.append(f"Viewers strongly praised the {aspect}.")
        elif sentiment_label == "positive":
            insights.append(f"Viewers appreciated the {aspect}.")
        elif sentiment_label == "negative":
            insights.append(f"Viewers were dissatisfied with the {aspect}.")

    return insights

def generate_summary(aspect_sentiments):

    positive_aspects = []
    negative_aspects = []

    for aspect, score in aspect_sentiments.items():

        if score > 0:
            positive_aspects.append(aspect)

        elif score < 0:
            negative_aspects.append(aspect)

    summary = ""

    if positive_aspects:
        pos_list = ", ".join(positive_aspects[:3])
        summary += f"Audiences appreciated the {pos_list}"

    if negative_aspects:
        neg_list = ", ".join(negative_aspects[:3])
        summary += f" while criticizing the {neg_list}"

    if summary:
        summary = "Overall, " + summary + "."

    return summary