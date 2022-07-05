from misc.new_db_instance import new_db_instance
from reddit_requests.latest_comments import request_latestComments
from misc.get_commentsMetadata import get_commentsMetadata
from misc.utils import loadJSON


def handle_commentsMedian():
    accepted_subreddits = loadJSON("accepted-subreddits")
    db = new_db_instance()

    for subreddit_name in accepted_subreddits:
        print(subreddit_name)
        latest_comments = request_latestComments(subreddit_name)

        if latest_comments["status_code"] == 200:
            comments_metadata = get_commentsMetadata(latest_comments["body"])
            comments_median = comments_metadata["median"]
            if comments_median > 0:
                update_commentsMedian(comments_median, subreddit_name, db)


def update_commentsMedian(new_median, subreddit_name, db):
    doc = db.collection("subreddits").document(subreddit_name).get()
    current_median = doc.to_dict()["commentsMedian"]

    db.collection("subreddits").document(subreddit_name).update(
        {f"commentsMedian": (current_median + new_median) / 2}
    )


if __name__ == "__main__":
    handle_commentsMedian()
