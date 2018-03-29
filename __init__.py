from crawlpy import crawlspy
from util.tags.linktag import linktag

class Spider:
    def __init__(self,url,nodes,spidername):
        self.spider = crawlspy(url,nodes,spidername)
    
    def crawl(self):
        self.spider.crawl()

if __name__ == "__main__":
    linktag = linktag()
    #url = "http://www.davidbpython.com/advanced_python/python_data/dormouse.html"
    #url = "http://www.google.co.in"
    url = raw_input("Type the url(with http://):")
    crawly = Spider(url,linktag,"crawly")       #default port 80
    crawly.crawl()