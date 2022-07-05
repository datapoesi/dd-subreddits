import statistics
from misc.get_cleanComments import get_cleanComments


def get_commentsMetadata(comments):
    metadata = {
        "median": get_median(comments),
        "num_comments": len(comments),
        "num_authors": get_num_authors(comments),
        "age_latestComment": comments[0]["data"]["created"],
        "age_oldestComment": comments[-1]["data"]["created"],
    }
    return metadata


def get_num_authors(comments):
    clean_comments = get_cleanComments(comments)

    authors = set()
    for comment in clean_comments:
        authors.add(comment["author"])
    return len(authors)


def get_median(comments):
    clean_comments = get_cleanComments(comments)

    authors = {}
    for comment in clean_comments:
        author = comment["author"]
        authors[author] = []
    for comment in clean_comments:
        author = comment["author"]
        authors[author].append(len(comment["body"]))

    authors_median = []
    for author in authors:
        authors_median.append(statistics.median(authors[author]))

    return round(statistics.median(authors_median))
