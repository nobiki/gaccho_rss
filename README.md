# Gaccho RSS

Plug-in for subscribing to RSS feed at [gaccho](https://github.com/nobiki/gaccho)

## Setup

Setting of "gaccho.ini"

#### [FeedName] Section.

* [FeedName] (required):  
The section name displayed in the list.  
"FeedName" is an arbitrary character string set with 8 bytes  
Common setting of `type = Rss` is set in the [Rss] section

* type (required)  
Set "Rss".

* color_text (optional): [default](https://github.com/nobiki/gaccho_rss/blob/0.0.3/gaccho_rss/Rss.py#L13)
* color_back (optional): [default](https://github.com/nobiki/gaccho_rss/blob/0.0.3/gaccho_rss/Rss.py#L13)

* feeds (optional)  
Set feeds to subscribe by line break separator.

```
[Feed1]
type = Rss

color_text = [BLACK,RED,GREEN,YELLOW,BLUE,MAGENTA,CYAN,WHITE]
color_back = [BLACK,RED,GREEN,YELLOW,BLUE,MAGENTA,CYAN,WHITE]

feeds:
    https://mysite1.com/feed
    https://mysite2.com/feed

[Feed2]
type = Rss

feeds:
    https://mysite3.com/feed

    :

```

#### [Rss] Section

* [Rss] (optional):  
Common setting concerning "type = Rss"

* interval (optional)  
Set the retention period of the local cache in minutes. (default: 60 minutes)

```
[Rss]
interval = 30
```
