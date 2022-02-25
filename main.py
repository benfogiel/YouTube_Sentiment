from textblob import TextBlob
from textblob.en import Sentiment

def main():
    testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")
    testimonial.sentiment
    Sentiment(polarity=0.39166666666666666, subjectivity=0.4357142857142857)
    print(testimonial.sentiment.polarity)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
