from urlparse import urlparse

def gethostname(url):
    return urlparse(url).hostname