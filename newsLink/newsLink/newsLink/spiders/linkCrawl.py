import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class LinkcrawlSpider(CrawlSpider):
    name = 'linkCrawl'
    allowed_domains = ['prothomalo.com']
    start_urls = ['https://www.prothomalo.com/']

    rules = (
        Rule(LinkExtractor(), callback='parse_item'),
    )
    def parse_item(self, response):
        yield {
            'link': response.url
        }
