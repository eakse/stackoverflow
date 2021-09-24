import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
import json
from pprint import pprint
from time import sleep


class SpiderClass(scrapy.Spider):
    name = 'spider_name'

    custom_settings = {
        "FEED_FORMAT": 'csv',
        "FEED_URI": 'dataset.csv'
    }

    def __init__(self) -> None:
        self.api_json = {'html': 'dummy'}
        self.html_list = []
        super().__init__()


    def start_requests(self):
        links_list = ['https://10times.com/company/informa-knect']
        for link in links_list:
            yield scrapy.Request(url=link, callback=self.parse)

    
    def parse(self, response):
        ids = response.xpath('//input[@id="companyId"]/@value').get()
        company_name = response.xpath('//h1/text()').get()

        main_data = {
            "Links": response.url,
            "CompanyName": company_name,
        }

        off_set = 1
        api_url = f'https://10times.com/ajax?for=companyEvents&id={ids}&by=&offset={off_set * 5}&pastHit=0&calValue=upcoming'
        yield response.follow(url=api_url, meta=main_data,callback=self.parse_api)


        while self.api_json['html'].strip() != '':
            off_set += 1
            off_set_number = off_set * 5
            api_url = f'https://10times.com/ajax?for=companyEvents&id={ids}&by=&offset={off_set_number}&pastHit=0&calValue=upcoming'

            yield response.follow(url=api_url, meta=main_data,callback=self.parse_api)
            sleep(0.5)


    def parse_api(self, response):
        self.api_json = json.loads(response.body)
        if self.api_json['html'].strip() != '':
            self.html_list.append(self.api_json['html'])


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(SpiderClass)
    process.start()
    process.spiders
    
