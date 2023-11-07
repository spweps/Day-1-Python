import scrapy
from NewsCrawler.items import NewsItem

class NewsSpider(scrapy.Spider):
    name = "news_spider"
    start_urls = [
        "https://www.example-news-website.com"  # Replace with the actual URL
    ]

    def parse(self, response):
        for article in response.xpath("//div[@class='article']"):  # Adjust this XPath according to the website structure
            item = NewsItem()
            item['title'] = article.xpath(".//h2/a/text()").get()
            item['link'] = article.xpath(".//h2/a/@href").get()
            yield item
