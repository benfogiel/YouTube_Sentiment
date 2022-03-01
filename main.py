import sent
import scrape
import pandas as pd
"""
currently used only to demo textblob
"""

def main():
    """
    scrapes comments, runs sentiment analysis, and stores into csv
    """
    videos = 'data/markiplier_videos.txt'  # txt containing all of the video IDs
    file_name = 'data/markiplier.csv'  # output file name here (will overwrite an existing file with the same name)
    comments_per_vid = 100  # number of comments to scrape per video

    # get comments
    df = scrape.get_comments(videos, file_name, comments_per_vid)
    # add sentiment analysis score column
    df['sent_score'] = sent.get_sentiments(df['comment'])
    # write csv
    df.to_csv(file_name, encoding='utf-8', index=False)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
