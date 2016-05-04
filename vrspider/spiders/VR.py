# - * - coding: utf-8 - * -
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from vrspider.items import VrListItem
from vrspider.items import VrContentItem
import time

class VR(CrawlSpider):
    name = 'VR'
    start_urls = [
        'http://www.leiphone.com/category/jingdu/page/1',
    ]
    def parse(self, response):
        item = VrListItem()
        selector = Selector(response)
        Infos = selector.xpath('//div[@class="artSortList-main lph-main clr"]/div[@class="inner"]/div[@class="artSortList-left lph-left category-list"]/div[@class="lph-pageList index-pageList"]/div[@class="wrap"]/ul/li')
        for info in Infos:
            title = info.xpath('div[@class="word"]/a/div[@class="tit"]/text()').extract()
            thumb = info.xpath('div[@class="img"]/a/img[@class="lazy"]/@data-original').extract()
            description = info.xpath('div[@class="word"]/div[@class="des"]/text()').extract()
            pubtime = ' '.join(info.xpath('div[@class="word"]/div[@class="info"]/div[@class="time"]/span/text()').extract())
            pubtime = time.mktime(time.strptime(pubtime,'%Y / %m / %d %H:%M'));
            author = info.xpath('div[@class="word"]/div[@class="info"]/div[@class="aut"]/a/span/text()').extract()
            infotype = ''.join(info.xpath('div[@class="img"]/a[@class="sort"]/text()').extract()).strip()
            item['title'] = ''.join(title).strip()
            item['thumb'] = ''.join(thumb).strip()
            item['description'] = ''.join(description).strip()
            item['pubtime'] = int(pubtime)
            item['author'] = ''.join(author).strip()
            item['infotype'] = infotype
            yield item
        nextLink = selector.xpath('//div[@class="lph-paging1 clr"]/a[@class="nt"]/@href').extract()
        if nextLink:
            nextLink = nextLink[0]
            print(nextLink)
            yield Request(nextLink,callback=self.parse)