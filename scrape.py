import os
import googleapiclient.discovery
import pandas as pd
import numpy as np

def get_comments(videos, file_name, comments_per_vid):
    """
    :param videos: (str) path to txt containing all the video IDs
    :param file_name: (str) file name to store comment data
    :param comments_per_vid: (int) max number of comments to scrape per video
    :return: (DataFrame) headers: video_id, comment, comment_date, and sent_score (Note: sent_score vals are Nan's)
    """

    # get all video ids
    video_ids = []
    with open(videos, 'r') as f:
        for line in f:
            if '\n' in line: line = line[:-1]
            video_ids.append(line)

    # delete duplicates
    video_ids = list(dict.fromkeys(video_ids))

    # get all the snippets
    snippets = []
    for video in video_ids:
        snippets.append(scrape(video_id=video, count=comments_per_vid))

    data = {'video_id': [], 'author': [], 'comment': [], 'comment_date': [], 'sent_score': []}
    for snippet in snippets:
        for i, k in enumerate(snippet['items']):
            # top level comment
            data['video_id'].append(k['snippet']['videoId'])
            data['author'].append(k['snippet']['topLevelComment']['snippet']['authorChannelId']['value'])
            data['comment'].append(k['snippet']['topLevelComment']['snippet']['textOriginal'].replace('\n', ' '))
            data['comment_date'].append(k['snippet']['topLevelComment']['snippet']['publishedAt'])
            # get replies
            replies = {}
            try:
                replies = k['replies']
            except:
                # no replies
                pass
            if len(replies):
                for r in replies['comments']:
                    data['video_id'].append(r['snippet']['videoId'])
                    data['author'].append(r['snippet']['authorChannelId']['value'])
                    data['comment'].append(
                        r['snippet']['textOriginal'].replace('\n', ' '))
                    data['comment_date'].append(r['snippet']['publishedAt'])
    # add Nan values for sent_score - these values will be added later
    data['sent_score'] = np.full(len(data['video_id']), np.nan)

    return pd.DataFrame(data)


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
        part="snippet,replies",
        maxResults=count,
        order="relevance",
        textFormat="plainText",
        videoId = video_id,
    )
    return request.execute()