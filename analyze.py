from textblob import TextBlob
from statistics import mean

def analyze_sent(file):
    """
    param file: (.txt file) each row is a phrase of interest
    return: (float - [-1,1]) mean of polarity
    """
    polarities = []
    with open(file) as f:
        phrase = f.readline()
        testimonial = TextBlob(phrase)
        polarities.append(testimonial.sentiment.polarity)

    return mean(polarities)