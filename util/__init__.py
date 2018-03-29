from scrape import scrape
import re

class Scrapedata:
    def __init__(self,url,nodetype):
        self.scraper = scrape(url,nodetype)
        self.scrapdatacontent = self.scraper.nodes
    
    def cleanhtml(self):
        pass
    