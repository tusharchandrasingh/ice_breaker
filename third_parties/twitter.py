import json
import logging
from datetime import datetime, timezone

logger = logging.getLogger("twitter")

data = [
    {
        "edit_history_tweet_ids": ["1659558198649470977"],
        "id": "1659558198649470977",
        "text": "@LangChainAI  has tons of more stuff on it, making our lives so much easier when developing LLM powered applications and IMO is the go to open source framework for developing LLM applications. \nhttps://t.co/Il4HMgDVcI",
    },
    {
        "edit_history_tweet_ids": ["1659558196577443840"],
        "id": "1659558196577443840",
        "text": "8/8 And here's where @LangChainAI  \ud83e\udd9c\ud83d\udd17shines - it automates this entire process and does all the heavy lifting for us \ud83d\udcaa\nWith one line of code, you can invoke a RetrievalQA chain that takes care of all those tasks. https://t.co/Q5XDNtD9Ce",
    },
    {
        "edit_history_tweet_ids": ["1659558190843846657"],
        "id": "1659558190843846657",
        "text": "6/8: Now we retrieve these vectors. They contain the context required to answer our query \ud83d\udd75\ufe0f\u200d\u2642\ufe0f and represent the text that we need to base our answer on. https://t.co/180EXiQbAr",
    },
]


def scrape_user_tweets(username, num_tweets=5):
    """Scrapes a Twitter users's original tweets (i.e., not retweets or
    replies) and returns them as a list of dictionaries.Each dictionary has
    three fields: "time_posted" (relative to now), "text", and "url".
    """
    print("log: ", "requested user tweets for user ", username)

    # build tweet list from stub twitter data to avoid using Twitter API
    tweet_list = []
    for tweet in data:
        if "RT @" not in tweet["text"] and not tweet["text"].startswith("@"):
            tweet_dict = {
                "text": tweet["text"],
                "url": f"https://twitter.com/{username}/status/{tweet['id']}",
            }
            tweet_list.append(tweet_dict)
    print("log: ", "returning stub user tweets to bypass twitter api calls")
    return tweet_list


# # Debug
# if __name__ == "__main__":
#     print(scrape_user_tweets(username='elonmusk'))
