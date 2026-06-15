import requests
import json
from config import PAGE_ACCESS_TOKEN, TIME_CRITERIA, SEARCH_CRITERIA, DIRECTORY_FB, PAGE_ID

def get_fb_data():
    all_data = []
    url = f"https://graph.facebook.com/v25.0/{PAGE_ID}/video_reels"
    params = {
        "fields": "description,views,likes.summary(true),created_time,permalink_url",
        "access_token": PAGE_ACCESS_TOKEN,
        "limit": 100
    }

    while url:
        response = requests.get(url, params=params)
        data = response.json()
        all_data.extend(data.get('data', []))
        paging = data.get('paging', {})
        url = paging.get('next')
        params = {}

    total_likes = 0
    total_views = 0
    i_count = 0

    for dict in all_data:
        likes = dict['likes']['summary']['total_count']
        if TIME_CRITERIA in dict['created_time']:
            if SEARCH_CRITERIA.lower() in dict['description'].lower():
                total_views = total_views + int(dict['views'])
                total_likes = total_likes + int(likes)

    with open(DIRECTORY_FB, 'w') as f:
        for dict in all_data:
            if TIME_CRITERIA in dict['created_time']:
                if SEARCH_CRITERIA in dict['description'].lower():
                    permalink_fb = dict['permalink_url']
                    f.write(f"https://www.facebook.com{permalink_fb} \n")
                    i_count = i_count + 1

    print(f"SAVED FB links in {DIRECTORY_FB}, kopa {i_count} video")
    return total_likes, total_views
