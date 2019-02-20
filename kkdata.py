import urllib.request as req
import csv

def get_dict_from_url_csv(url):
    
    if url.split('/')[-1][-3:] == 'csv':
        file = req.urlretrieve(url, url.split('/')[-1])[0]

        stat = {}
        with open(file) as file:
            reader = csv.reader(file)
            header_row = next(reader)
            for row in reader:
                year, area, age, nationality, count = map(int, row)
                stat.setdefault(year,{}).setdefault(area,{}).setdefault(age,{})[nationality] = count
        return stat
    return {error:'wrong file type'}
