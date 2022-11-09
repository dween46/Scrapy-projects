import scrapy
import pandas as pd

from ..items import BackmarketItem

class ExampleSpider(scrapy.Spider):
    name = 'infoScraper'
    allowed_domains = ['backmarket.co.uk']
    today = pd.to_datetime("today").strftime("%d_%b_%y")
    df = pd.read_csv("././csv/links/{}_backmarket_iphone_links.csv".format(today))
    #df = pd.read_csv("./csv/07_nov_22_backmarket_iphone_links.csv".format(today))

    start_urls = list(df['link'].str.split('#', expand = True)[0].unique())

    def parse(self, response):
        #print("***********************************")
        item = BackmarketItem()
        item['date'] = self.today
        try:
            item['product_name'] = response.css('h1::text').get().strip().replace('\n', '')
        except:
            item['product_name'] = "Title Not found"
        try:
            item['product_id'] = response.css('li.md\:block.text-link-primary.overflow-hidden.flex-shrink.min-w-\[6ch\].hidden > div::text').get().strip().replace('\n', '')
        except:
            item['product_id'] = "ID Not found"

        item['link']  = response.url

        try:
            item['fair'] = response.css('li:nth-child(1) > a > div > div.body-2-light.text-center.text-primary-light::text').get().strip().replace('\n', '').replace('£', '')
        except:
            item['fair'] = "-1"
        try:
            item['good']= response.css('li:nth-child(2) > a > div > div.body-2-light.text-center.text-primary-light::text').get().strip().replace('\n', '').replace('£', '')
        except:
            item['good'] = "-1"
        try:
            item['excellent'] = response.css('li:nth-child(3) > a > div > div.body-2-light.text-center.text-primary-light::text').get().strip().replace('\n', '').replace('£', '')
        except:
            item['excellent'] = "-1"
        try:
            item['rating'] = response.css('div.hidden.md\:flex.flex-grow.flex-col > button > div > span::text').get().strip().replace('\n', '').replace('/5', '')
        except:
            item['rating'] = "N/A"
        try:
            item['reviews'] = response.css('div.hidden.md\:flex.flex-grow.flex-col > button > span::text').get().strip().replace('\n', '').replace('(', '').replace(')', '').replace(' reviews', '').replace(',', '')
        except:
            item['reviews'] = "N/A"
        try:
            item['provider'] = response.css('p.body-1-bold.mb-1.overflow-hidden > a::text').get().strip().replace('\n', '')
        except:
            item['provider'] = "N/A"

        try:
            item['provider_link'] = 'https://www.backmarket.co.uk' + response.css('p.body-1-bold.mb-1.overflow-hidden > a::attr(href)').get()
        except:
            item['provider_link'] = "N/A"

        try:
            item['storage'] = response.css('span.text-center.body-2-bold.text-primary::text').getall()[1].strip().replace('\n', '').replace(' GB', '')
        except:
            item['storage'] = "N/A"
        
        try:
            item['color'] = response.css('span.text-center.body-2-bold.text-primary::text').getall()[2].strip().replace('\n', '')
        except:
            item['color'] = "N/A"


        yield item

