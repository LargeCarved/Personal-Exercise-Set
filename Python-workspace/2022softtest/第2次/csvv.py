import csv
def get_data(file):
    rows = []
    data = csv.reader(open(file,encoding="utf-8"))
    next(data,None)
    for i in data:
        rows.append(i)
    return rows