import sqlite3
import telnetlib
from spider import config


class HtmlDatabase(object):
    def __init__(self):
        self.db=sqlite3.connect("proxies.db")

    def __del__(self):
        self.db.close()

    def insert(self, host, port):
        sql="INSERT INTO `proxies`.`proxy` (`id`, `host`, `port`) VALUES (NULL, '%s', '%s');"
        cur=self.db.cursor()
        cur.execute(sql % (host,port))
        self.db.commit()
        cur.close()
        print("insert %s:%s"%(host,port))

    def __checkProxy(self,host,port):
        try:
            telnetlib.Telnet(host,port=port,timeout=10)
        except:
            return False
        else:
            return True
          
    def clear(self):
        sql="TRUNCATE TABLE  `proxy`"
        cur=self.db.cursor()
        cur.execute(sql)
        self.db.commit()
        cur.close()
        print("clear ok")

    def getProxies(self):
        sql="SELECT * FROM `proxy` WHERE 1"
        cur=self.db.cursor()
        cur.execute(sql)
        lists=cur.fetchall()
        self.db.commit()
        cur.close()
        return lists


    def saveDatas(self, datas):
        for data in datas:
            if self.__checkProxy(data[0],data[1]):
                self.insert(data[0], data[1])
            else:
                print("%s:%s banned" %(data[0],data[1]))

if __name__ == '__main__':
    ht=HtmlDatabase()
    print(ht.clear())