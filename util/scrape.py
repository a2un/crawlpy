from http import http

class scrape:
    def __init__(self,url,nodetype):
        self.handler = http(url)
        self.nodetype = nodetype
        self.__scrapedata()

    def __scrapedata(self):
        self.nodes = self.handler.getnodes(self.nodetype)