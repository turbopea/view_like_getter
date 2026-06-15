#!/usr/bin/env python3

from facebook import get_fb_data
from instagram import get_ig_data
from youtube import get_yt_data
from config import SEARCH_CRITERIA

fb_likes, fb_views = get_fb_data()
ig_likes, ig_views = get_ig_data()
yt_likes, yt_views = get_yt_data()

visible_ig_likes = ig_likes + fb_likes
visible_ig_views = ig_views + fb_views
total_likes = visible_ig_likes + fb_likes + yt_likes
total_views = visible_ig_views + fb_views + yt_views
goal_views = 150000


print(f"Epizode:{SEARCH_CRITERIA.upper()}")
print(f"Facebook like: {fb_likes}, Facebook skatijumi: {fb_views}")
print(f"Instagram likes: {visible_ig_likes}, Instagram skatijumi:{visible_ig_views}")
print(f"Youtube like:{yt_likes}, Youtube skatijumi: {yt_views}")
print(f"Kopejais like skaits YT, FB, IG platformas: {total_likes}")
print(f"Kopejais skatijumu skaits YT,FB,IG platformas: {total_views}")
print(f"Sobrid sasniegts: {round(total_views/goal_views*100,0)}%")
