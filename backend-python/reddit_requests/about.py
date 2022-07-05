from reddit_requests.request_data import request_data

def request_about(subreddit_name):
    reddit_URL = f'https://oauth.reddit.com/r/{subreddit_name}/about'
    response = request_data(reddit_URL)

    if response["status_code"] == 200:
        response["body"] = response["body"]["data"]
        
    return response