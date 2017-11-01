from Article import Article

import feedparser
from datetime import datetime
from time import mktime

class Rss(Article):
    def color_pair(self):
        return {"color_text":"WHITE", "color_back":"GREEN"}

    def get(self):
        feed = feedparser.parse("https://qiita.com/tags/Docker/feed.atom")

        ret = []

        for i in range(len(feed.entries)):
            published = datetime.fromtimestamp(mktime(feed.entries[i].published_parsed))
            title = feed.entries[i].title
            url = feed.entries[i].url
            value = feed.entries[i]["content"][0]["value"]
            author = feed.entries[i].author
            ret.append(("Rss", str(published), author, title, url, self.strip_tags(value)))

        return ret
