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
        ## load config
        self.config = configparser.ConfigParser()
        self.config.read("gaccho.ini")

        regex = re.compile(
                r'^(?:http|ftp)s?://' # http:// or https://
                r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
                r'localhost|' #localhost...
                r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
                r'(?::\d+)?' # optional port
                r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        ret = []
        for c in enumerate(self.config):
            if "type" in self.config[c[1]] and "Rss" == self.config[c[1]]["type"]:
                item = c[1]
                feeds = dict(self.config[item])

                if "feeds" in feeds:
                    for url in feeds["feeds"].split("\n"):
                        if regex.search(url):
                            feed = feedparser.parse(url)
                            for i in range(len(feed.entries)):
                                name = feed.feed.title
                                published = datetime.fromtimestamp(mktime(feed.entries[i].published_parsed))
                                title = feed.entries[i].title
                                link = feed.entries[i].link
                                value = feed.entries[i]["content"][0]["value"]
                                author = feed.entries[i].author
                                ret.append((item, name, str(published), author, title, link, self.strip_tags(value)))


        self.cache_save("cache/Rss", ret)

        return ret

    def controll(self, **keywords):
        ret = {}

        if keywords["key_pair"] == "" and keywords["key"] == ord("y"):
            ret["key_trigger"] = "test"
            ret["key_pair"] = ""

        return ret
