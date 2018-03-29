from bs4 import BeautifulSoup

class response:
    def __init__(self,reqrespdata,parseparams):
        self.responsedata = reqrespdata
        self.parseparams = parseparams

    def returnresp(self):
        return BeautifulSoup(self.responsedata,self.parseparams)