"""
from scrapy.crawler import Crawler
from scrapy import project, signals
from twisted.internet import reactor
from billiard import Process
from scrapy.utils.project import get_project_settings

import sys
sys.path.insert(0, '/Users/akhil/Documents/final_project/foodscraper/foodscraper/spiders')

from acm_spider import ACMSpider

class CrawlerScript(Process):
        def __init__(self, spider):
            Process.__init__(self)
            settings = get_project_settings()
            self.crawler = Crawler(settings)

            if not hasattr(project, 'crawler'):
                self.crawler.install()
                self.crawler.configure()
                self.crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
            self.spider = spider

        def run(self):
            self.crawler.crawl(self.spider)
            self.crawler.start()
            reactor.run()

def run_spider(url):
    spider = ACMSpider(url)
    crawler = CrawlerScript(spider)
    crawler.start()
    crawler.join()

"""

from twisted.internet import reactor

from scrapy import log, signals
from scrapy.crawler import Crawler
from scrapy.xlib.pydispatch import dispatcher

import sys
sys.path.insert(0, '/Users/akhil/Documents/final_project/foodscraper/foodscraper/')

from spiders.acm_spider import ACMSpider
import settings

import sys
sys.path.insert(0, '/Users/akhil/Documents/final_project/free_food/')

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'free_food.settings'

def stop_reactor():
    reactor.stop()

dispatcher.connect(stop_reactor, signal=signals.spider_closed)
spider = ACMSpider()
crawler = Crawler(settings)
crawler.configure()
crawler.crawl(spider)
crawler.start()
log.start()
log.msg('Running reactor...')
reactor.run()  # the script will block here until the spider is closed
log.msg('Reactor stopped.')