from misc.filter_subredditsCSV import filter_subredditsCSV

sample_csv = "pytest_coverage/sample_csv"


def test_filter10k():
    filtered = filter_subredditsCSV(sample_csv)
    assert len(filtered) == 11
