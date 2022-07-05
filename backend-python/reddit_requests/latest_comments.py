from reddit_requests.request_data import request_data


def request_latestComments(subreddit_name):
    reddit_URL = f"https://oauth.reddit.com/r/{subreddit_name}/comments?limit=100"
    response = request_data(reddit_URL)

    if response["status_code"] == 200:
        response["body"] = response["body"]["data"]["children"]

    return response
