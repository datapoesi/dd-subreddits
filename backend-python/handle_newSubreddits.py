from misc.get_newSubreddits import get_newSubreddits
from misc.filter_subredditsCSV import filter_subredditsCSV
from misc.new_db_instance import new_db_instance
from reddit_requests.about import request_about
from update_subredditsMetadata import update_firestore_metadata
from misc.utils import loadJSON, saveJSON
from reddit_requests.latest_comments import request_latestComments
from misc.get_commentsMetadata import get_commentsMetadata
from config import LATEST_CSV, ACCEPTABLE_MEDIAN


def handle_newSubreddits():
    accepted_subreddits = loadJSON("accepted-subreddits")
    rejected_subreddits = loadJSON("rejected-subreddits")

    filtered_subreddits = filter_subredditsCSV(LATEST_CSV)
    new_subreddits = get_newSubreddits(filtered_subreddits)

    db = new_db_instance()

    for subreddit_name in new_subreddits:
        latest_comments = request_latestComments(subreddit_name)
        if latest_comments["status_code"] == 200:
            comments_metadata = get_commentsMetadata(latest_comments["body"])

            acceptable = comments_metadata["median"] >= ACCEPTABLE_MEDIAN
            if acceptable:
                accepted_subreddits.append(subreddit_name)
                subreddit_metadata = request_about(subreddit_name)["body"]
                update_firestore_metadata(subreddit_name, db, subreddit_metadata)
            else:
                rejected_subreddits.append(subreddit_name)

    saveJSON(accepted_subreddits, "accepted-subreddits")
    saveJSON(rejected_subreddits, "rejected-subreddits")


if __name__ == "__main__":
    handle_newSubreddits()
