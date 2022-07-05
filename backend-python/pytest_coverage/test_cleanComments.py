from misc.get_cleanComments import get_cleanComments
from misc.utils import loadJSON

sample_comments = loadJSON("pytest_coverage/sample_comments")
clean_comments = get_cleanComments(sample_comments)

# the length of sample_comments is 5, but cleanup_comments should only return 3 because one comment has &lt;code&gt; in it, and the other was authored by AutoModerator.
def test_length():
    assert len(clean_comments) == 3


def test_composition():
    assert clean_comments[0]["author"] == "teambob"
