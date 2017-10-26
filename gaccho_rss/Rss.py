from Article import Article

import feedparser
from datetime import datetime
from time import mktime

class Rss(Article):
    def color_pair(self):
        return {"text":"WHITE", "back":"GREEN"}

    def get(self):
        feed = feedparser.parse("https://qiita.com/tags/Docker/feed.atom")

        ret = []

        for i in range(len(feed.entries)):
            published = datetime.fromtimestamp(mktime(feed.entries[i].published_parsed))
            value = feed.entries[i].title+"\n"+feed.entries[i]["content"][0]["value"]
            author = feed.entries[i].author
            ret.append(("Rss", str(published), author, self.strip_tags(value)))

        return ret
