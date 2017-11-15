from Article import Article

import re

import configparser
import feedparser

from datetime import datetime
from time import mktime

class Rss(Article):
    def color_pair(self):
        return {"color_text":"WHITE", "color_back":"GREEN"}

    def get(self):
        ret = []

        ## load config
        self.config = configparser.ConfigParser()
        self.config.read("gaccho.ini")
        feeds = dict(self.config["Rss"])

        regex = re.compile(
                r'^(?:http|ftp)s?://' # http:// or https://
                r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
                r'localhost|' #localhost...
                r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
                r'(?::\d+)?' # optional port
                r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        for url in feeds["feeds"].split("\n"):
            if regex.search(url):

                feed = feedparser.parse(url)

                for i in range(len(feed.entries)):
                    name = feed.title
                    published = datetime.fromtimestamp(mktime(feed.entries[i].published_parsed))
                    title = feed.entries[i].title
                    link = feed.entries[i].link
                    value = feed.entries[i]["content"][0]["value"]
                    author = feed.entries[i].author
                    ret.append((name, str(published), author, title, link, self.strip_tags(value)))

        self.cache_save("cache/Rss", ret)

        return ret

