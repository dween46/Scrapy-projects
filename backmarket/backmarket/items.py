# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags

def remove_currency(value):
    return value.replace('£', '').strip()

def remove_newline(value):
    return value.replace('\n', '').strip()

def remove_brackets(value):
    return value.replace('(', '').replace(')', '').strip()

def remove_slashfive(value):
    return value.replace('/5', '').strip()


# class linkItem(scrapy.Item):
#     # define the fields for your item here like:
#     link = scrapy.Field()
    

class BackmarketItem(scrapy.Item):
    date= scrapy.Field()
    product_name =scrapy.Field(input_processor=MapCompose(remove_tags, remove_newline), output_processor=TakeFirst())
    product_id = scrapy.Field(input_processor=MapCompose(remove_tags, remove_newline), output_processor=TakeFirst())
    link = scrapy.Field()
    fair = scrapy.Field(input_processor=MapCompose(remove_tags, remove_newline, remove_currency), output_processor=TakeFirst())
    good = scrapy.Field(input_processor=MapCompose(remove_tags, remove_newline, remove_currency), output_processor=TakeFirst())
    excellent = scrapy.Field(input_processor=MapCompose(remove_tags, remove_newline, remove_currency), output_processor=TakeFirst())
    rating = scrapy.Field(input_processor=MapCompose(remove_tags, remove_newline, remove_slashfive), output_processor=TakeFirst())
    reviews = scrapy.Field(input_processor=MapCompose(remove_tags, remove_newline, remove_brackets), output_processor=TakeFirst())


