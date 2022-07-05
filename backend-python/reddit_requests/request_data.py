import requests, config, time, os
from reddit_requests.request_auth import get_access_token
from dotenv import load_dotenv
load_dotenv()

def request_data(reddit_URL):
    headers = {
        "Authorization": "bearer " + os.environ["ACCESS_TOKEN"], 
        "User-Agent": config.USER_AGENT
    }

    response = requests.get(reddit_URL, headers=headers)

    if response.status_code == 401:
        print('Expired token.')
        os.environ["ACCESS_TOKEN"] = get_access_token()
        headers["Authorization"] = "bearer " + os.environ["ACCESS_TOKEN"]
        response = requests.get(reddit_URL, headers=headers)

    content = {
        "status_code": response.status_code, 
        "body": None
    }

    if content["status_code"] == 403:
        content["body"] = "Private or forbidden resource."
    if content["status_code"] == 404:
        content["body"] = "Banned or unavailable resource."
    
    if content["status_code"] == 200:
        content["body"] = response.json()

    time.sleep(1.0)
    # requestsLeft = float(response.headers["x-ratelimit-remaining"])
    # requestsUsed = float(response.headers["x-ratelimit-used"])
    # "Clients connecting via OAuth2 may make up to 60 requests per minute."
    
    return content
