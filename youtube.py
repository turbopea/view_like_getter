from config import API_KEY, SEARCH_CRITERIA, TIME_CRITERIA, CHANNEL_ID, DIRECTORY_YT
from googleapiclient.discovery import build
import requests

def get_channel_stats(youtube, CHANNEL_ID):
    request = youtube.search().list(
                                    part='snippet',
                                    channelId="UCALP7Fam0rROugichV9gzQQ",
                                    maxResults = 50, 
                                    q = f"{SEARCH_CRITERIA}",
                                    publishedAfter = '2026-01-01T00:00:00Z'
                                    )
           

    response = request.execute()
    video_id_list= []
    views = response['items']
    for view in views:
            dict_id = view['id']
            videos_ids = dict_id['videoId']
            video_id_list.append(videos_ids)
    return video_id_list

def get_video_views(youtube,video_id_list):
    total = 0
    total_likes = 0
    for video_id in video_id_list:
        request = youtube.videos().list(
             part = 'statistics',
             id = video_id
             
        )
        response = request.execute()
        for item_list in response['items']:
            statistics = item_list['statistics']
            view_count = statistics['viewCount']
            view_count = int(view_count)
            total = total + view_count 
            like_count = statistics['likeCount']
            like_count = int(like_count)
            total_likes = total_likes + like_count


    return total, total_likes

def save_video_links(video_id_list, directory): 
    with open(directory, 'w') as f:
        for video_id in video_id_list:
            build = f"https://www.youtube.com/watch?v={video_id}\n"
            f.write(build)
    print(f"SAVED YT links in {directory}, kopā {len(video_id_list)} video")

     

def get_yt_data():
    base_url = "https://www.googleapis.com/youtube/v3/channelid/UCALP7Fam0rROugichV9gzQQ?key=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"
    youtube = build('youtube', 'v3', developerKey = API_KEY)
    get_channel_stats(youtube, CHANNEL_ID)
    video_id_list = get_channel_stats(youtube,CHANNEL_ID)
    save_video_links(video_id_list,DIRECTORY_YT)
    total, total_likes = get_video_views(youtube,video_id_list)
    return total_likes, total


                        




