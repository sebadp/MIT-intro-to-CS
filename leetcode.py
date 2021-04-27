def destCity(paths=[[]]):
    result = ''
    print(paths)
    # print(destiny)
    for i in paths:
        print(i)
        for j in i:
            print(j)
            result = j
    return print(result)
paths= [['a','s'],['e','u']]

if __name__ == '__main__':
    destCity([['a','s'],['e','u']])