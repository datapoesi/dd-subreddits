from misc.utils import loadJSON
from misc.get_commentsMetadata import get_commentsMetadata

sample_comments = loadJSON("pytest_coverage/sample_comments")
metadata = get_commentsMetadata(sample_comments)


def test_median():
    assert metadata["median"] == 64


def test_comments():
    assert metadata["num_comments"] == 5


def test_authors():
    assert metadata["num_authors"] == 3


def test_latestComment():
    assert metadata["age_latestComment"] == 1656920962.0


def test_oldestComment():
    assert metadata["age_oldestComment"] == 1656918546.0
