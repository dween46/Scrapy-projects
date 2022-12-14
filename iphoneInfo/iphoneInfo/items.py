# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class IphoneinfoItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass


class BackmarketItem(scrapy.Item):
    date= scrapy.Field()
    product_name =scrapy.Field()
    product_id = scrapy.Field()
    link = scrapy.Field()
    fair = scrapy.Field()
    good = scrapy.Field()
    excellent = scrapy.Field()
    rating = scrapy.Field()
    reviews = scrapy.Field()
    provider = scrapy.Field()
    provider_link = scrapy.Field()
    storage = scrapy.Field()
    color = scrapy.Field()
