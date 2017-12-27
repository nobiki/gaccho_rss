# Gaccho RSS

Plug-in for subscribing to RSS feed at [gaccho](https://github.com/nobiki/gaccho)

#### setup [gaccho.ini]

* FeedName (required):  
The section name displayed in the list. Within 8 bytes.  
When "Rss" is set, it becomes common setting of the section where `type = Rss` is specified

* type (required)  
Set "Rss".

* color_text (optional): [default](https://github.com/nobiki/gaccho_rss/blob/0.0.3/gaccho_rss/Rss.py#L13)
* color_back (optional): [default](https://github.com/nobiki/gaccho_rss/blob/0.0.3/gaccho_rss/Rss.py#L13)

* feeds (optional)  
Set feeds to subscribe by line break separator.

```
[FeedName]
type = Rss

color_text = [BLACK,RED,GREEN,YELLOW,BLUE,MAGENTA,CYAN,WHITE]
color_back = [BLACK,RED,GREEN,YELLOW,BLUE,MAGENTA,CYAN,WHITE]

feeds:
    https://mysite1.com/feed
    https://mysite2.com/feed
```
