from email.policy import default
import scrapy
import pandas as pd
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
#from scrapy.crawler import CrawlerProcess


#from ..items import BackmarketItem
from ..items import linkItem


class BackmarketCrawlSpider(scrapy.Spider):
    name = 'linkCrawl'
    allowed_domains = ['backmarket.co.uk']
    today = pd.to_datetime("today").strftime("%d_%b_%y")

    start_urls = ["https://www.backmarket.co.uk/en-gb/l/iphone/aabc736a-cb66-4ac0-a3b7-0f449781ed39"]

    # def parse_product(self, response):

    #     print('Here we go!!!!!!________________________________')
        
    #     item = BackmarketItem()
    #     #item = {}

    #     #div.flex.flex-col.lg\:max-w-\[38rem\] > 

    #     item['date'] = self.today
    #     try:
    #         item['product_name'] = response.css('h1::text').get().strip().replace('\n', '')
    #     except:
    #         item['product_name'] = "Title Not found"
    #     try:
    #         item['product_id'] = response.css('li.md\:block.text-link-primary.overflow-hidden.flex-shrink.min-w-\[6ch\].hidden > div::text').get().strip().replace('\n', '')
    #     except:
    #         item['product_id'] = "ID Not found"

    #     item['link']  = response.url

    #     try:
    #         item['fair'] = response.css('li:nth-child(1) > a > div > div.body-2-light.text-center.text-primary-light::text').get().strip().replace('\n', '').replace('£', '')
    #     except:
    #         item['fair'] = "Sold out"
    #     try:
    #         item['good']= response.css('li:nth-child(2) > a > div > div.body-2-light.text-center.text-primary-light::text').get().strip().replace('\n', '').replace('£', '')
    #     except:
    #         item['good'] = "Sold out"
    #     try:
    #         item['excellent'] = response.css('li:nth-child(3) > a > div > div.body-2-light.text-center.text-primary-light::text').get().strip().replace('\n', '').replace('£', '')
    #     except:
    #         item['excellent'] = "Sold out"
    #     try:
    #         item['rating'] = response.css('div.hidden.md\:flex.flex-grow.flex-col > button > div > span::text').get().strip().replace('\n', '')
    #     except:
    #         item['rating'] = "No data"
    #     try:
    #         item['reviews'] = response.css('div.hidden.md\:flex.flex-grow.flex-col > button > span::text').get().strip().replace('\n', '')
    #     except:
    #         item['reviews'] = "No data"

    #     yield item
    #     #return item

    # def parse_product(self, response):
    #     l = ItemLoader(item=BackmarketItem(), response=response)

    #     l.add_value('date', self.today)
    #     l.add_css('product_name', 'h1::text')
    #     l.add_css('product_id', 'li.md\:block.text-link-primary.overflow-hidden.flex-shrink.min-w-\[6ch\].hidden > div::text')
    #     l.add_value('link', response.url)
    #     l.add_css('fair', 'li:nth-child(1) > a > div > div.body-2-light.text-center.text-primary-light::text')
    #     l.add_css('good', 'li:nth-child(2) > a > div > div.body-2-light.text-center.text-primary-light::text')
    #     l.add_css('excellent', 'li:nth-child(3) > a > div > div.body-2-light.text-center.text-primary-light::text')
    #     l.add_css('rating', 'div.hidden.md\:flex.flex-grow.flex-col > button > div > span::text')
    #     l.add_css('reviews', 'div.hidden.md\:flex.flex-grow.flex-col > button > span::text')

    #     return l.load_item()


    # def parse_color_links(self,response):
    #     color_links = response.css('div.md\:w-2\/3.lg\:w-1\/2.lg\:flex-1.max-w-full > div > div > div:nth-child(3) > div:nth-child(3)>ul > li >a::attr(href)').getall()

    #     for c_link in color_links:
    #         item = linkItem()
    #         inside_link = 'https://www.backmarket.co.uk' + c_link
    #         print("***************************************************")
    #         #yield scrapy.Request(inside_link, callback=self.parse_product)
    #         item['link'] = inside_link
    #         yield item

    def parse_storage_links(self, response):
        #storage_links = response.css('div.md\:w-2\/3.lg\:w-1\/2.lg\:flex-1.max-w-full > div > div > div:nth-child(3) > div:nth-child(3)>ul > li >a::attr(href)').getall()
        storage_links = response.css('div > div > div:nth-child(4) > div:nth-child(2) > ul > li > a::attr(href)').getall()
        for new_link in storage_links:
            item = linkItem()
            inside_link = 'https://www.backmarket.co.uk' + new_link
            #print("***************************************************")
            #yield scrapy.Request(inside_link, callback=self.parse_product)
            item['link'] = inside_link
            yield item
            

    def parse_page_links(self, response):
        all_links = response.css('section > div > div.grid.grid-cols-1.gap-4.md\:gap-7.lg\:grid-cols-\[repeat\(3\,26\.2rem\)\].md\:mx-auto.lg\:mr-4.md\:grid-cols-\[repeat\(2\,26\.2rem\)\] > div > a::attr(href)').getall()
        
        #print(f"***************************   {len(all_links)}  ***************************")
        for link in all_links:
            p_url = 'https://www.backmarket.co.uk' + link
            yield scrapy.Request(p_url, callback=self.parse_storage_links)


    def parse(self, response):
        totalPage = int(response.css('section > nav > a:nth-child(5) > span::text').get().strip().replace('\n', ''))
        if totalPage:
            for i in range(1, totalPage+1):
                url = "https://www.backmarket.co.uk/en-gb/l/iphone/aabc736a-cb66-4ac0-a3b7-0f449781ed39?page={}".format(i)
                yield scrapy.Request(url, callback=self.parse_page_links)

        
        