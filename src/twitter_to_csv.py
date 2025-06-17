import os
import requests
import pandas as pd
from datetime import datetime
import json
import sys
from dotenv import load_dotenv

load_dotenv()  # ✅ Load .env
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
CACHE_FILE = "cached_tweets.json"

def create_headers(token):
    return {"Authorization": f"Bearer {token}"}

def search_tweets(query, max_results=10):
    url = "https://api.twitter.com/2/tweets/search/recent"
    headers = create_headers(BEARER_TOKEN)
    params = {
        "query": query,
        "max_results": max_results,
        "tweet.fields": "id,text,author_id,created_at"
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(f"Request failed: {response.status_code} - {response.text}")
    
    return response.json()

def save_to_csv(data, filename):
    tweets = data.get("data", [])
    df = pd.DataFrame(tweets)
    if not df.empty:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        df.to_csv(filename, index=False)
        print(f"✅ Saved {len(df)} tweets to {filename}")
    else:
        print("⚠️ No tweets found for this query.")

def save_to_json(data, filename=CACHE_FILE):
    with open(filename, "w") as f:
        json.dump(data, f)
    print(f"✅ Cached tweets to {filename}")

def load_from_json(filename=CACHE_FILE):
    with open(filename, "r") as f:
        return json.load(f)

def fetch_and_save_tweets():
    search_term = "Snowflake data engineering"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"tweets_{timestamp}.csv"
    file_path = os.path.join("sql", file_name)

    use_cache = True

    if use_cache and os.path.exists(CACHE_FILE):
        print("📦 Using cached tweets")
        tweet_data = load_from_json()
    else:
        tweet_data = search_tweets(search_term, max_results=20)
        save_to_json(tweet_data)

    save_to_csv(tweet_data, file_path)

