import csv

# INPUT: CSV file of all subreddits, approximately 3.5 million.
# OUTPUT: A set of approximately 35k names of subreddits where subscriber count is >=10,000.
def filter_subredditsCSV(csv_path):
    filtered_subreddits = set()

    with open(f"{csv_path}.csv", encoding="utf8", errors="replace") as csv_file:
        next(csv_file, None)  # Skips the header row of the CSV file.
        try:
            for row in csv.reader(csv_file, delimiter=","):
                subreddit_name = row[0]
                subscribers = int(row[3])
                if subscribers >= 10000:
                    filtered_subreddits.add(subreddit_name)
        except Exception as e:
            print(e)

    return filtered_subreddits
