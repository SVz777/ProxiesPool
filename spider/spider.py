from spider import htmlDatabase
from spider import htmlDownloader
from spider import htmlParser


class Spiser(object):
    def __init__(self):
        self.htmlDownloader=htmlDownloader.HtmlDownloader()
        self.htmlDatabase=htmlDatabase.HtmlDatabase()
        self.htmlParser=htmlParser.HtmlParser()

    def craw(self,url):
        print("craw:"+url)
        content=self.htmlDownloader.download(url)
        datas=self.htmlParser.parser(content)
        self.htmlDatabase.saveDatas(datas)


