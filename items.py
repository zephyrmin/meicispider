# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class MeiciItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class JsArticleItem(scrapy.Item):
    brand = scrapy.Field()
    productitle = scrapy.Field()
    price = scrapy.Field()
    color = scrapy.Field()
    szie = scrapy.Field()
    proimg = scrapy.Field()
    prodata = scrapy.Field()
    brandstory = scrapy.Field()
    brandimg = scrapy.Field()
    meiciid = scrapy.Field()

