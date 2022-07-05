from misc.utils import loadJSON, saveJSON
from misc.new_db_instance import new_db_instance
from config import ACCEPTABLE_MEDIAN


def handle_subparSubreddits():
    db = new_db_instance()
    subpar_subreddits = get_subparSubreddits(db)
    demote_subparSubreddits(subpar_subreddits, db)


def get_subparSubreddits(db):
    query = (
        db.collection("subreddits")
        .where("commentsMedian", "<", ACCEPTABLE_MEDIAN)
        .order_by("commentsMedian")
    )

    subpar_subreddits = []
    documents = query.stream()
    for subreddit_doc in documents:
        subpar_subreddits.append(subreddit_doc.to_dict()["name"])

    return subpar_subreddits


def demote_subparSubreddits(subpar_subreddits, db):
    accepted_subreddits = loadJSON("accepted-subreddits")
    rejected_subreddits = loadJSON("rejected-subreddits")

    if len(subpar_subreddits) > len(accepted_subreddits) / 2:
        print("Error")
        return

    for subreddit_name in subpar_subreddits:
        print(subreddit_name)
        if subreddit_name in accepted_subreddits:
            accepted_subreddits.remove(subreddit_name)
        if subreddit_name not in rejected_subreddits:
            rejected_subreddits.append(subreddit_name)
        db.collection("subreddits").document(subreddit_name).delete()

    print(len(rejected_subreddits), len(accepted_subreddits), len(subpar_subreddits))
    saveJSON(accepted_subreddits, "accepted-subreddits")
    saveJSON(rejected_subreddits, "rejected-subreddits")


if __name__ == "__main__":
    handle_subparSubreddits()
