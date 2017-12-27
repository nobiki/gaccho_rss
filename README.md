# Gaccho RSS

plugin for [Gaccho](https://github.com/nobiki/gaccho)

#### setup [gaccho.ini]

* color_text (optional): [default](https://github.com/nobiki/gaccho_rss/blob/1484fff49b29e3bf7126323f6ccc8454948e6227/gaccho_rss/Rss.py#L13)  

* color_back (optional): [default](https://github.com/nobiki/gaccho_rss/blob/1484fff49b29e3bf7126323f6ccc8454948e6227/gaccho_rss/Rss.py#L13)  

* FeedName (required):  
The section name displayed in the list. Within 8 bytes.  
When "Rss" is set, it becomes common setting of the section where B is specified

* type (required)  

* feeds (optional)  

example:  
```
[FeedName]
type = Rss

feeds:
    https://mysite1.com/feed
    https://mysite2.com/feed

color_text = [BLACK,RED,GREEN,YELLOW,BLUE,MAGENTA,CYAN,WHITE]
color_back = [BLACK,RED,GREEN,YELLOW,BLUE,MAGENTA,CYAN,WHITE]
```
