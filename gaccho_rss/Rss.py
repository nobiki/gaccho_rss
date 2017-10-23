import Article

import feedparser
from datetime import datetime
from time import mktime

class Rss(Article.Article):
    def color_pair(self):
        return {"text":"WHITE", "back":"GREEN"}

    def get(self):
        feed = feedparser.parse("https://qiita.com/tags/Docker/feed.atom")

        ret = []

        for i in range(len(feed.entries)):
            published = datetime.fromtimestamp(mktime(feed.entries[i].published_parsed))
            title = feed.entries[i].title
            ret.append(("Rss", title, str(published)))

        print(ret)
        return ret
