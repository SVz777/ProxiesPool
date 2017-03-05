from spider import config


def getUrl(kind):
    a=[config.URL + config.KIND[kind]]
    for i in range(1, config.PAGE):
        a.append(config.URL + config.KIND[kind] + "/" + str(i))
    return a

if __name__ == '__main__':
    print(getUrl("高匿"))