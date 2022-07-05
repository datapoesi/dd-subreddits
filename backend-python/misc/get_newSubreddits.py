from misc.utils import loadJSON

# OUTPUT: Names of subreddits that are not in the accepted nor in the rejected collections of subreddits.
def get_newSubreddits(subreddits_set):
    not_filtered = len(subreddits_set) > 123456
    if not_filtered:
        print("Set contains full dataset.")
        return

    accepted_subreddits = loadJSON("accepted-subreddits")
    rejected_subreddits = loadJSON("rejected-subreddits")
    new_subreddits = set()

    for name in subreddits_set:
        not_accepted = name not in accepted_subreddits
        not_rejected = name not in rejected_subreddits
        if not_accepted and not_rejected:
            new_subreddits.add(name)

    return new_subreddits
