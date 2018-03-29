from request import request
from response import response

# from urllib2 import urlopen
# from bs4 import BeautifulSoup

class http:
    def __init__(self,url):
        self.url = url
        self.req = request(url)
        self.resp = response(self.req.makeRequest(),"html.parser")

    def __getdata(self):
        return self.req.makeRequest()
    
    def __convertdata(self):
        return self.resp.returnresp()

    def getnodes(self,nodetype):
        soup = self.__convertdata()
        if not(nodetype=="html"):
            return soup.find_all(nodetype)
        else:
            soup = self.cleansoup(soup)
            return soup.get_text().encode("utf-8")
    
    def cleansoup(self,soup):
        for elements in soup(["script","style"]):
            elements.decompose()
        return soup