from misc.new_db_instance import new_db_instance
from reddit_requests.about import request_about
from misc.utils import loadJSON


def update_subredditsMetadata():
    accepted_subreddits = loadJSON("accepted-subreddits")
    db = new_db_instance()

    for subreddit_name in accepted_subreddits:
        print(subreddit_name)
        response = request_about(subreddit_name)
        if response["status_code"] == 200:
            try:
                subreddit_metadata = response["body"]
                update_firestore_metadata(subreddit_name, db, subreddit_metadata)
            except Exception as e:
                print(e)


def update_firestore_metadata(subreddit_name, db, metadata):
    db.collection("subreddits").document(subreddit_name).update(
        {
            "name": metadata["display_name"],
            "created": metadata["created"],
            "desc": metadata["public_description"],
            "numSubscribers": metadata["subscribers"],
        }
    )


if __name__ == "__main__":
    update_subredditsMetadata()
