from reddit_requests.about import request_about

def request_numSubscribers(subreddit_name):
    response = request_about(subreddit_name)
    subscribers = None

    if response["status_code"] == 200 and response["body"]["subscribers"]:
        subscribers = response["body"]["subscribers"]

    return subscribers
