# 0x16. API advanced

A buildup of the previous project on API. This folder has tasks and exercises that scrape the Reddit API using Python


## Task 0: How many subs?

File:

	- 0-subs.py
Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.
No authentication is necessary for most features of the Reddit API. If you’re getting errors related to Too Many Requests, ensure you’re setting a custom User-Agent.

Requirements:
- Prototype: def number_of_subscribers(subreddit)
- If not a valid subreddit, return 0.



## Task 1: Top Ten

File:

	- 1-top_ten.py
Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
Requirements:
- Prototype: def top_ten(subreddit)
- If not a valid subreddit, print None.
- NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.