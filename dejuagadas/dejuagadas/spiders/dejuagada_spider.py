#!/usr/bin/python
# -*- coding: utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from dejuagadas.items import DejuagadasItem

class dejugadaSpider(CrawlSpider):
    name = "dejugada"
    allowed_domains =["http://www.dejugadas.com/"]
    start_urls=["http://www.dejugadas.com/quini6.php"]
    rules = [Rule(SgmlLinkExtractor(allow=()), callback='parse_item')]
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select("*")
        items = []
        for site in sites:
            item = DejuagadasItem()
            item['name'] =site.select("*").extract()
        items.append(item)
        return items
