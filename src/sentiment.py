from src.sentiment import predict_sentiment
def predict_sentiment(text):
    text = text.lower()

    positive_words = ['good', 'great', 'positive', 'profit', 'gain']
    negative_words = ['bad', 'loss', 'negative', 'drop', 'crash']

    score = 0

    for word in positive_words:
        if word in text:
            score += 1

    for word in negative_words:
        if word in text:
            score -= 1

    if score > 0:
        return "positive"
    elif score < 0:
        return "negative"
    else:
        return "neutral"
