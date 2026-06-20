## About The Project

    This is my custom made script, which counts views and likes for specific type of videos in specific social media profile. This script uses client's API keys from Youtube, Facebook, Instagram. Accessing API data, it fetches number of likes, views for specific kind of videos. This program is good fit for those social media accounts which have like multiple videos/podcasts about one subject or topic.
        This is the visisble data that is being shown on IG, FB pages.
    This is the output(example):
    EPISODE: "Miti" (Video topic)
    IG likes: 1167, IG views: 73267 
    FB likes: 635, FB views: 52353
    YT likes: 49, YT views: 1599
    Total: 127219
    Current status: 85% from 150000
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## SETTING UP THE WHOLE PROGRAM. STEP BY STEP.
Social Media Data Fetcher

Fetches data from Facebook Pages, Instagram Business accounts, and YouTube channels using their official APIs.

This guide explains how to get the credentials (tokens and IDs) the app needs.

Note: Facebook and Google change their dashboards often. If a button name has moved, look for the closest equivalent.

What you'll need

A Meta Developer account — https://developers.facebook.com A Facebook Page you manage An Instagram Business account linked to that Page (for Instagram data) A Google account for Google Cloud Console — https://console.cloud.google.com

Step 1 — Facebook & Instagram

Both use the same Meta app, so you set this up once.

Create the app

Go to https://developers.facebook.com/apps → Create App. Pick a Business type app, name it, and create it. On the dashboard, add the Instagram Graph API product (and Facebook Login).

Get a user token

Open the Graph API Explorer: https://developers.facebook.com/tools/explorer Top right: select your app. Click Generate Access Token and approve. Add these permissions when asked:

pages_show_list pages_read_engagement instagram_basic instagram_manage_insights

This token only lasts ~2 hours — that's fine, you'll upgrade it next.

Make the token permanent (2 calls)

Call 1 — turn the short token into a 60-day token:

https://graph.facebook.com/v25.0/oauth/access_token?grant_type=fb_exchange_token&client_id=APP_ID&client_secret=APP_SECRET&fb_exchange_token=SHORT_TOKEN

(Find APP_ID and APP_SECRET under Settings → Basic on your app dashboard.)

Call 2 — use that new token to get your Page token and IDs:

https://graph.facebook.com/v25.0/me/accounts?access_token=LONG_TOKEN

The result gives you, for your Page:

id → your Page ID access_token → your Page Token (this one won't expire — see below)

Get your Instagram Business ID

https://graph.facebook.com/v25.0/PAGE_ID?fields=instagram_business_account&access_token=PAGE_TOKEN

The instagram_business_account.id is your Instagram Business ID.

Step 2 — YouTube

Go to https://console.cloud.google.com → create a project. APIs & Services → Library → search YouTube Data API v3 → Enable. APIs & Services → Credentials → Create Credentials → API key. Copy it. Note the Channel ID of the channel you want (in YouTube channel settings).

Step 3 — Configuration

Put everything in a .env file. Never commit real values to GitHub.

env# Facebook / Instagram FB_APP_ID= FB_APP_SECRET= FB_PAGE_ID= FB_PAGE_ACCESS_TOKEN= IG_BUSINESS_ID=

YouTube

YT_API_KEY= YT_CHANNEL_ID=

Add .env to your .gitignore:

gitignore.env

Step 4 — Run

bashnpm install # or: pip install -r requirements.txt npm start # or: python main.py

About the Page token (why two calls?)

A Page token copies the lifetime of the user token used to fetch it:

Short-lived user token → Page token dies in ~2 hours. Long-lived user token → Page token never expires.

That's why you exchange the user token first, then call me/accounts second. The order is what makes the Page token permanent.

To check a token: paste it at https://developers.facebook.com/tools/debug/accesstoken — Expires should say Never.

Security

Treat tokens like passwords. Never push real tokens or your App Secret to GitHub. If a token was ever committed, regenerate it — it stays in git history. Tokens stop working if permissions are revoked or the account password changes.
  
