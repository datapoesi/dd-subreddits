from reddit_requests.request_data import request_data


def request_selectedPost(subreddit_name, post_id):
    reddit_URL = f"https://oauth.reddit.com/r/{subreddit_name}/comments/{post_id}"
    response = request_data(reddit_URL)

    if response["status_code"] == 200:
        response["body"] = {
            "post_data": response["body"][0]["data"]["children"][0]["data"],
            "comments_data": response["body"][1]["data"]["children"],
        }

    return response
