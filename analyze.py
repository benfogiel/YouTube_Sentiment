import pdb

from textblob import TextBlob
from statistics import mean

def get_sentiments(file):
    """
    param file: (str - .txt file) each row is a phrase of interest
    return: (list - floats) list of polarity values [-1,1]
    """
    polarities = []
    with open(file, "r") as f:
        for phrase in f:
            testimonial = TextBlob(phrase)
            polarities.append(testimonial.sentiment.polarity)

    return polarities