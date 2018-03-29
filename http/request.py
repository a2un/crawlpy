from urllib2 import urlopen
import urllib2

class request:
    def __init__(self,url):
        self.url = url
    
    def makeRequest(self):
        try:
            return urlopen(self.url)
        except urllib2.HTTPError:
            return ""

