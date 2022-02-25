from textblob import TextBlob
"""
currently used only to demo textblob
"""

def main():
    testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")
    testimonial.sentiment
    print(testimonial.sentiment.polarity)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
