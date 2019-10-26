from scrapy import Spider,Selector,Request
from scrapy_splash import SplashRequest

from ximalaya.items import XimalayaItem


class XimalayaSpider(Spider):
    name = 'ximalaya'
    start_urls = ['https://www.ximalaya.com/youshengshu/wenxue/p{}/']

    def start_requests(self):
        for page in range(1, 38):
            url = self.start_urls[0].format(page)

            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        sel = Selector(response)
        book_lists = sel.xpath('//*[@id="award"]/main/div[1]/div/div[3]/div[1]/div/div[2]/ul/li')
        for li in book_lists:

            href = li.xpath('./div/a[1]/@href').extract_first()
            detail_href = 'https://www.ximalaya.com'+href

            yield Request(url=detail_href,callback=self.parse_detail)


    def parse_detail(self,response):
        sel = Selector(response)
        pages_list = sel.xpath('//*[@id="anchor_sound_list"]/div[2]/div/nav/ul/li')
        if pages_list:
            total_page_sel = pages_list[-2]
            total_page = int(total_page_sel.xpath('./a/span/text()').extract_first())
        else:
            total_page = 1

        urls_chapter = response.url+'p{}'

        for page in range(1,total_page+1):
            url = urls_chapter.format(page)

            yield Request(url=url, callback=self.parse_chapter)


    def parse_chapter(self,response):
        sel = Selector(response)
        item = XimalayaItem()
        item['title'] = sel.xpath(
            '//*[@id="award"]/main/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/h1/text()').extract_first()
        item['zhubo'] = sel.xpath(
            '//*[@id="award"]/main/div[1]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div/p/a/text()').extract_first()
        item['detail_href'] = response.url
        chapter_list = sel.xpath('//*[@id="anchor_sound_list"]/div[2]/ul/li')
        result = []
        for chapter in chapter_list:
            data = {
                'title': chapter.xpath('./div[2]/a/span/text()').extract_first(),
                'metia_href': 'https://www.ximalaya.com' + chapter.xpath('./div[2]/a/@href').extract_first()
            }

            result.append(data)
        item['chapter'] = result
        yield item










