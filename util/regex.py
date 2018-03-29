import re


class Pattern:
    def __init__(self):
        pass
    
    @staticmethod
    def match(pattern,string):
        return re.match(pattern,string)