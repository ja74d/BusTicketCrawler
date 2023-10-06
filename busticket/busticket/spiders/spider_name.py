import scrapy


class SpiderNameSpider(scrapy.Spider):
    name = "spider_name"
    allowed_domains = ["domain.com"]
    start_urls = ["https://domain.com"]

    def parse(self, response):
        pass
