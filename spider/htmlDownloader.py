import requests
class HtmlDownloader(object):
    def __init__(self):
        self.rq=requests.session()
    def download(self, url):
        if url is None:
            return None
        headers={
            'Host':'www.xicidaili.com',
            'Connection':'keep-alive',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2986.0 Safari/537.36',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer':'http://www.xicidaili.com/',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Accept-Language':'zh-CN,zh;q=0.8',
        }
        content=self.rq.get(url,headers=headers)
        return content.text.encode(content.encoding).decode()
