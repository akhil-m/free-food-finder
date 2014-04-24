from scrapy.crawler import Crawler
from foodscraper.spiders.acm_spider import ACMSpider
from scrapy import project, signals
from twisted.internet import reactor
from billiard import Process
from scrapy.utils.project import get_project_settings

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