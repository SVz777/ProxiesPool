from bs4 import BeautifulSoup

class HtmlParser(object):
    def parser(self, content):
        bs=BeautifulSoup(content,'html.parser')
        lists=bs.find('table',id='ip_list').find_all('tr')
        datas=[]
        for i in lists[1:]:
            ls=i.find_all('td')
            datas.append([ls[1].string,ls[2].string])
        return datas



if __name__ == '__main__':
    content=open('../test/item.html','r',encoding='utf8').read()
    ht=HtmlParser()
    print(ht.parser(content))