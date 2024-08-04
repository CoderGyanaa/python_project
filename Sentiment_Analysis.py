from textblob import TextBlob

def analyze_your_sentiment(text):
   
    blob = TextBlob(text)
    sentiment_rate = blob.sentiment.polarity

    if sentiment_rate > 0:
        sentiment = "Positive"
    elif sentiment_rate < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, sentiment_rate

def main():
    print("\t---------------------------")
    print("\t| Sentiment Analysis Tool |")
    print("\t---------------------------")

    while True:
        user_input = input("Enter a sentence or review (or type 'exit' to quit): ")

        if user_input.lower() == 'exit':
            print("Exiting the Sentiment Analysis Tool. Visit Again!")
            break

        if not user_input.strip():
            print("Input cannot be empty. Please enter a valid sentence or review.")
            continue

        sentiment, score = analyze_your_sentiment(user_input)
        print(f"The sentiment of the given text is: {sentiment} (Rate: {score})")
        print()

if __name__ == "__main__":
    main()
