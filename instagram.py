import requests
import json
from config import PAGE_ACCESS_TOKEN, IG_BUS_ID, TIME_CRITERIA, SEARCH_CRITERIA, DIRECTORY_IG

def get_ig_data():
    response = requests.get(
    f"https://graph.facebook.com/v25.0/{IG_BUS_ID}/media",
    params ={
        "fields": "timestamp, id, permalink, caption",
        "access_token": PAGE_ACCESS_TOKEN,
        "limit": 100
        }
    )
    data = response.json()
    batch = []

    for dict_data in data['data']:
        if TIME_CRITERIA in dict_data['timestamp'] and SEARCH_CRITERIA.lower() in dict_data['caption'].lower():
            id = dict_data.get('id')
            batch.append({
                "method": "GET",
                "relative_url": f"{id}/insights?metric=views,likes"
            })
    i_count = 0
    with open(DIRECTORY_IG, 'w') as f:
        for dict_data in data['data']:
            if TIME_CRITERIA in dict_data['timestamp'] and SEARCH_CRITERIA.lower() in dict_data['caption'].lower():
                permalink = dict_data.get('permalink')
                i_count = i_count + 1
                f.write(f"{permalink} \n")
        print(f"SAVED IG links in {DIRECTORY_IG}, kopa {i_count} video")        
   

    results = requests.post(
        "https://graph.facebook.com/v25.0/",
        params={"access_token":PAGE_ACCESS_TOKEN},
        data = {"batch": json.dumps(batch)}
    )
    ig_likes = 0
    ig_views = 0
    
    data = results.json()
    for batch_data in data:
        body = json.loads(batch_data['body'])
        body_data = body['data']
        for items in body_data:
            if items['name'] == 'views':
                views_ig=items['values'][0]['value']
            if items['name'] == 'likes':
                likes_ig = items['values'][0]['value']
                ig_likes = ig_likes + likes_ig
                ig_views = ig_views + views_ig
    return ig_likes, ig_views





    