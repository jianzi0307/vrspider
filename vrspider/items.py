# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 列表项
class VrListItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    thumb = scrapy.Field()
    description = scrapy.Field()
    pubtime = scrapy.Field()
    author = scrapy.Field()
    infotype = scrapy.Field()
    pass

# 内容
class VrContentItem(scrapy.Item):
    pass

