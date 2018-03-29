from util import Scrapedata
from util.tags.htmltag import htmltag
from util.tags.linktag import linktag
from util.regex import Pattern
from util import utilurlparse
import os

class crawlspy:
    def __init__(self,url,nodetype,spidername):
        self.name = spidername
        self.url = url
        self.nodetype = nodetype
        self.crawlrule= "default"
        self.scrapedcontent = ""
        self.linknodes = []
        self.count = 1
        
    def crawl(self):
        self.__crawl(self.url)
        print "crawling.... " + self.url
        for link in self.linknodes:
            linktagtype = linktag()
            linktagtype.setname()
            if Pattern.match("^http",link.get('href')):
                print link.get('href')
                self.__crawl(link.get('href'))

        #return self.scrapedcontent

    def __crawl(self,url):
        self.crawlcomplete = False

        htmltagtype = htmltag()
        htmltagtype.setname()
        html = Scrapedata(url,htmltagtype.getname()).scrapdatacontent

        for x in Scrapedata(url,self.nodetype.getname()).scrapdatacontent:
            self.linknodes.append(x)
        
        self.scrapedcontent = html

        self.__writedata(url)

        self.crawlcomplete = True

    def __writedata(self,url):
        #print 'writing to file...'
        filemode = 'w'

        if not(os.path.isdir('./crawlrepo')):
            os.mkdir('./crawlrepo')
        
        with open('./crawlrepo/scrapecontent-'+ utilurlparse.gethostname(url)+'.txt',filemode) as f:
                f.write(str(self.scrapedcontent))

        self.count +=1