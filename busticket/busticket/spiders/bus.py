import scrapy
from scrapy_splash import SplashRequest


class BusSpider(scrapy.Spider):
    name = "bus"
    download_delay = 5.0
    allowed_domains = ["www.payaneha.com"]
    start_urls = ["https://www.payaneha.com/busticket/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D8%A8%D9%84%DB%8C%D8%B7-%D8%A7%D8%AA%D9%88%D8%A8%D9%88%D8%B3-%D8%A7%D8%B2-%D8%A7%D8%B5%D9%81%D9%87%D8%A7%D9%86-%D8%A8%D9%87-%DA%A9%D8%B1%D9%85%D8%A7%D9%86%D8%B4%D8%A7%D9%87"]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 2})

    def parse(self, response):
        data = response.xpath('/html/body/div[1]/div/div[2]/div[2]/div/label').get()

        yield {
            'title': data
        }
