import scrapy
from my_table_scrapy.items import MyTableScrapyItem

class TableSpider(scrapy.Spider):
    name = 'table_spider'
    start_urls = ['https://bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=TLV']
    def parse(self, response):
        rows = response.css('tbody tr')
        for row in rows:
            item = MyTableScrapyItem()
            item['date'] = row.css('::text').get()
            item['market'] = row.css('::text').get()
            item['transactions'] = row.css('::text').get()
            item['volume'] = row.css('::text').get()
            item['value'] = row.css('::text').get()
            item['open_price'] = row.css('::text').get()
            item['min_price'] = row.css('::text').get()
            item['max_price'] = row.css('::text').get()
            item['avg_price'] = row.css('::text').get()
            item['close_price'] = row.css('::text').get()
            item['variation'] = row.css('::text').get()

            yield item

