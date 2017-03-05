import multiprocessing
from spider import comment
from spider.spider import Spiser
def run(url):
    spider=Spiser()
    spider.craw(url)

if __name__ == '__main__':
    urls=comment.getUrl("高匿")
    thread=multiprocessing.Pool()
    for url in urls:
        thread.apply_async(run,args=(url,))
    thread.close()
    thread.join()

    print("done")