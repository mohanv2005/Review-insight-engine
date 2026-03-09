def get_top_aspects(aspect_scores, top_n=3):

    # Sort aspects by score
    sorted_aspects = sorted(aspect_scores.items(), key=lambda x: x[1], reverse=True)

    # Top positive
    top_positive = [a for a in sorted_aspects if a[1] > 0][:top_n]

    # Top negative
    top_negative = sorted([a for a in sorted_aspects if a[1] < 0], key=lambda x: x[1])[:top_n]

    return top_positive, top_negative