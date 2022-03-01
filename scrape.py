""""
scrapes YouTube comments
https://developers.google.com/youtube/v3/docs/commentThreads/list
"""

# -*- coding: utf-8 -*-

# Sample Python code for youtube.commentThreads.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
import googleapiclient.discovery
import pandas as pd

def get_comments(videos, file_name, comments_per_vid):
    """
    :param videos: (str) path to txt containing all the video IDs
    :param file_name: (str) file name to store comment data
    :param comments_per_vid: (int) max number of comments to scrape per video
    :return: writes comments to csv <file_name>
    """

    # get all video ids
    video_ids = []
    with open(videos, 'r') as f:
        for line in f:
            if '\n' in line: line = line[:-1]
            video_ids.append(line)

    # get all the snippets
    snippets = []
    for video in video_ids:
        snippets.append(scrape(video_id=video, count=comments_per_vid))
    write(file_name=file_name,snippets=snippets)


def scrape(video_id, count):
    """
    :param video_id: YouTube video ID (found in url)
    :param count: number of comments to scrape
    :return: (json obj) google comments extractor snippet
    """
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = os.environ["GOOG_CLOUD_API"] # insert your google api (here I stored it as an environment var)

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet",
        maxResults=count,
        order="time",
        textFormat="plainText",
        videoId = video_id,
    )
    return request.execute()

def write(file_name, snippets):
    """
    write to csv
    param file_name: (str) csv file name
    param snippets: (list of json objs) google comments extractor snippets
    """
    # merge all of them into a dictionary
    data = {'video_id': [], 'comment': [], 'comment_date': []}
    for snippet in snippets:
        for i, k in enumerate(snippet['items']):
            data['video_id'].append(k['snippet']['videoId'])
            data['comment'].append(k['snippet']['topLevelComment']['snippet']['textOriginal'].replace('\n',' '))
            data['comment_date'].append(k['snippet']['topLevelComment']['snippet']['publishedAt'])

    df = pd.DataFrame(data)
    df.to_csv(file_name, encoding='utf-8', index=False)

if __name__ == "__main__":
    main()