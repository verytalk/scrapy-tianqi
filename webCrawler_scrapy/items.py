# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class WebcrawlerScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field()
    max_tempe = scrapy.Field()
    min_tempe = scrapy.Field()
    weather = scrapy.Field()
    wind = scrapy.Field()
    wind_power = scrapy.Field()
    address = scrapy.Field()
    address_code = scrapy.Field()

