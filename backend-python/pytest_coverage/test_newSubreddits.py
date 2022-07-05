from misc.get_newSubreddits import get_newSubreddits

sample_subreddits = {"newSubreddit123", "Python", "science"}
new_subreddits = get_newSubreddits(sample_subreddits)


def test_isNew():
    assert "newSubreddit123" in new_subreddits


def test_notNew():
    assert "Python" not in new_subreddits
