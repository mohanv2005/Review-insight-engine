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

    for aspect, score in aspect_sentiments.items():
        sentiment_label = score_to_label(score)

        if sentiment_label == "strongly positive":
            insights.append(f"Viewers strongly praised the {aspect}.")
        elif sentiment_label == "positive":
            insights.append(f"Viewers appreciated the {aspect}.")
        elif sentiment_label == "negative":
            insights.append(f"Viewers were dissatisfied with the {aspect}.")
        else:
            insights.append(f"Viewers had mixed opinions about the {aspect}.")

    return insights
