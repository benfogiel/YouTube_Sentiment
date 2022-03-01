from textblob import TextBlob

def get_sentiments(phrases):
    """
    param phrases: (list - str) phrases to run sentiment analysis on
    return: (list - floats) list of polarity values [-1,1]
    """
    polarities = []
    for phrase in phrases:
        testimonial = TextBlob(phrase)
        polarities.append(testimonial.sentiment.polarity)

    return polarities