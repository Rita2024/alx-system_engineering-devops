#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""
import re
import requests


def add_title(dictionary, hot_posts):
    """ Adds item into a list """
    if not hot_posts:
        return

    title = hot_posts[0]['data']['title'].split()
    for word in title:
        for key in dictionary.keys():
            c = re.compile("^{}$".format(key), re.I)
            if c.findall(word):
                dictionary[key] += 1
    hot_posts.pop(0)
    add_title(dictionary, hot_posts)


def recurse(subreddit, dictionary, after=None):
    """ Queries the Reddit API """
    user_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': user_agent
    }

    params = {
        'after': after
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)

    if res.status_code != 200:
        return None

    dic = res.json()
    hot_posts = dic['data']['children']
    add_title(dictionary, hot_posts)
    after = dic['data']['after']
    if not after:
        return
    recurse(subreddit, dictionary, after=after)


def count_words(subreddit, word_list):
    """ Initialization function """
    dictionary = {}

    for word in word_list:
        dictionary[word] = 0

    recurse(subreddit, dictionary)

    l = sorted(dictionary.items(), key=lambda kv: kv[1], reverse=True)

    if l:
        for item in l:
            if item[1] != 0:
                print("{}: {}".format(item[0], item[1]))
    else:
        print("")

if __name__ == '__main__':
    count_words(subreddit, keywords)
