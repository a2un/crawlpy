from htmltag import htmltag

class linktag(htmltag):
    def __init__(self):
        super(linktag,linktag).setname(self,"a")

    def getname(self):
        return self.name