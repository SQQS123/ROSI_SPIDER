# -*- coding: utf-8 -*-
import hashlib
import os
import requests
import scrapy


class RosiSpiderSpider(scrapy.Spider):
    name = 'rosi_spider'
    # 永久域名:www.rosmm.cc
    allowed_domains = ['rosmm8.cc']
    start_urls = ['http://rosmm8.cc/']

    def parse(self, response):
        img = response.xpath("//p[@id='imgString']")
        for i in img.xpath("./img/@src").extract():
            # 去掉点我加载更多的东西
            if i[-10:] == "smpimg.jpg":
                continue
            try:
                file_name = hashlib.sha224(i.encode('utf-8')).hexdigest()[:10] + '.jpg'
                file_path = os.path.join('pics', file_name)
                if os.path.exists(file_path):
                    self.logger.warning("Ignore: {} has existed".format(file_path))
                    break
                resp = requests.get(i ,headers = {
                        'User-Agent':'JUC (Linux; U; 2.3.7; zh-cn; MB200; 320*480) UCWEB7.9.3.103/139/999'
                        }, timeout=8)
                print("保存图片")
                with open(file_path,"wb") as f:
                    f.write(resp.content)
                    self.logger.info("Filename: {}".format(file_name))
            except Exception as e:
                self.logger.error(e)
                return

            # print(i)
        for a in response.css('a::attr(href)').extract():
            if not a:
                continue

            if response.urljoin(a)[:8] != "https://":
                continue
            next_page = response.urljoin(a)
            # print("下一页:" + next_page)

            yield  scrapy.Request(next_page,callback=self.parse)
