# YouTube Sentiment Analyzer

Given a list of YouTube video IDs and the number of comments to scrape from each video, this program will write a csv file containing each video ID, the comment, the comment date, and the sentiment score [-1, +1] where -1 is most negative, 0 is neutral, and +1 is most positive sentiment.

This uses YouTube's Data API to scrape comments which can be obtained from [here](https://developers.google.com/youtube/v3).

The sentiment scores are obtained using the TextBlob python package which uses Natural Language Processing (NLP).

**Usage:**
 - Activate virtual environment: ```source .gitignore/venv/bin/activate```
 - Compile a list of YouTube video IDs into a txt file (example of video ID is shown below). Each entry is one line.<img width="289" alt="Untitled12" src="https://user-images.githubusercontent.com/52505296/156219547-e31669cc-0d2e-442b-ac63-925a2aaeea40.png">
 
 - Get your YouTube Data API from [here](https://developers.google.com/youtube/v3)
 - Place your YouTube Data API in ```scrape.py``` located here:
 https://github.com/benfogiel/YouTube_Sentiment/blob/b19e3c9ccb70510bf5f41237b3c9aff5fa49d1d0/scrape.py#L50
 - Edit ```main.py``` with your input txt path, desired output txt path, and number of comments to scrape per video
 - run main ```python3 main.py```
