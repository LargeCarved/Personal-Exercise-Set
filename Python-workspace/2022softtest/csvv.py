import csv
def getdata(f):
    data = csv.reader(open(f,encoding='utf-8'))
    datas = []
    next(data,None)
    for i in data:
        datas.append(i)
    return datas