# import scrapy
# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor
# from ..items import linkItem

# class LinkCrawlSpider(scrapy.Spider):
#     name = 'link_crawl'
    
#     allowed_domains = ['backmarket.co.uk']

#     start_urls = ['https://www.backmarket.co.uk/en-gb/search?page=1&q=iphone#brand=0%20%20Apple'] 


# class LinkCrawlSpider(scrapy.Spider):
#     name = 'link_crawl'
    
#     allowed_domains = ['backmarket.co.uk']


#     start_urls = ['https://www.backmarket.co.uk/en-gb/search?page=1&q=iphone#brand=0%20%20Apple'] 

#     def parse(self, response):
#         totalPage = int(response.css('section > nav > a:nth-child(5) > span::text').get().strip().replace('\n', ''))

#         all_links = response.css('section > div > div.grid.grid-cols-1.gap-4.md\:gap-7.lg\:grid-cols-\[repeat\(3\,26\.2rem\)\].md\:mx-auto.lg\:mr-4.md\:grid-cols-\[repeat\(2\,26\.2rem\)\] > div > a::attr(href)').getall()

#         for i in range(2, totalPage+1):
#             url = 'https://www.backmarket.co.uk/en-gb/search?page={}&q=iphone#brand=0%20%20Apple'.format(i)
#             response.follow(url )
#             links = response.css('section > div > div.grid.grid-cols-1.gap-4.md\:gap-7.lg\:grid-cols-\[repeat\(3\,26\.2rem\)\].md\:mx-auto.lg\:mr-4.md\:grid-cols-\[repeat\(2\,26\.2rem\)\] > div > a::attr(href)').getall()
#             all_links.extend(links)

#         for link in all_links:
#             item = linkItem()
#             if '/p/' in link:
#                 item['links'] = link
#                 yield item
                



    



