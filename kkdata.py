import urllib.request as req
import csv
from os import path

def get_dict_from_url_csv(url):
    if url.split('/')[-1][-3:] == 'csv':
        if not path.isfile(url.split('/')[-1]):
            file = req.urlretrieve(url, url.split('/')[-1])[0]
        else:
            file = url.split('/')[-1]

        stat = {}
        with open(file) as file:
            reader = csv.reader(file)
            header_row = next(reader)
            for row in reader:
                year, area, age, nationality, count = map(int, row)
                stat.setdefault(year,{}).setdefault(area,{}).setdefault(age,{})[nationality] = count
        return stat
    return {error:'wrong file type'}
