import csv
import itertools
from  pprint import pprint
import os

def get_data_directory():
    ROOT_DIR =  os.path.abspath(os.path.join(__file__ ,"../../.."))
    return os.path.join(ROOT_DIR, 'data/')

def create_txt_directory():
    if not os.path.exists(get_data_directory()+'txts'):
        os.mkdir(get_data_directory()+'txts')

create_txt_directory()
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
combinations = [1, 2, 3, 4, 5, 6, 7]
with open(get_data_directory()+'txts/day_unions.txt', 'wt',encoding='utf8') as out:
    for c in combinations:
        x = {}
        k = 0
        for i in itertools.combinations(DAYS, c):
            x[tuple(sorted(i))] = 0
        with open(get_data_directory() +'teams.csv', newline='', encoding='utf-8') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                days = row[1].replace(" ", "").split("+")
                for i in itertools.combinations(DAYS, c):
                    # print(i, days)
                    if  any(item in i for item in days):
                            x[tuple(sorted(i))] = x[tuple(sorted(i))] + 1
        output = sorted(x.items(), key=lambda x: x[1], reverse=True)
        pprint(output, stream=out)