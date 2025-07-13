import pandas as pd

df = pd.read_csv("sentiment_dataset.csv")

positive_words = ["love", "happy", "best", "great", "awesome", "good"]
negative_words = ["awful", "sad", "worst", "disappointed", "bad", "terrible"]

def classify_sentiment(text):
    text = text.lower()
    if any(word in text for word in positive_words):
        return "Positive"
    elif any(word in text for word in negative_words):
        return "Negative"
    else:
        return "Neutral"

df['Predicted Sentiment'] = df['Text'].apply(classify_sentiment)

print(df)
