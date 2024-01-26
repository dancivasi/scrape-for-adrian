import scrapy

class MyTableScrapyItem(scrapy.Item):
    date = scrapy.Field()
    market = scrapy.Field()
    transactions = scrapy.Field()
    volume = scrapy.Field()
    value = scrapy.Field()
    open_price = scrapy.Field()
    min_price = scrapy.Field()
    max_price = scrapy.Field()
    avg_price = scrapy.Field()
    close_price = scrapy.Field()
    variation = scrapy.Field()