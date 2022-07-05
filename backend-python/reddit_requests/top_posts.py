from reddit_requests.request_data import request_data


def request_topPosts(subreddit_name, TIME_LIMIT="week", POSTS_LIMIT=10):
    reddit_URL = f"https://oauth.reddit.com/r/{subreddit_name}/top?t={TIME_LIMIT}&limit={POSTS_LIMIT}"
    response = request_data(reddit_URL)

    if response["status_code"] == 200:
        response["body"] = response["body"]["data"]["children"]

    return response
