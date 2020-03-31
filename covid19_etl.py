import requests
from contextlib import closing
import csv
import constants

def get_jhu_data():
    data = []
    with closing(requests.get(constants.URL, stream=True)) as r:
        f = (line.decode('utf-8') for line in r.iter_lines())
        for row in csv.reader(f):
            data.append(row)
    return data

print (get_jhu_data())
