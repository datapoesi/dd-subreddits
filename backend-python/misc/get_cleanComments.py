import re


def get_cleanComments(comments):
    clean_comments = []

    for comment in comments:
        autoMod = comment["data"]["author"] == "AutoModerator"
        deleted_comment = comment["data"]["body"] == "[deleted]"
        deleted_author = comment["data"]["author"] == "[deleted]"
        contains_table = "&lt;table&gt;" in comment["data"]["body_html"]
        contains_code = "&lt;code&gt;" in comment["data"]["body_html"]

        if (
            autoMod
            or deleted_comment
            or deleted_author
            or contains_table
            or contains_code
        ):
            continue

        clean_comment = {
            "author": comment["data"]["author"],
            "body": re.sub(r"http\S+", "", comment["data"]["body"]),
            "created": comment["data"]["created"],
        }

        clean_comments.append(clean_comment)

    return clean_comments
