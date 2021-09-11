import csv
import itertools
from  pprint import pprint
import os

def get_data_directory():
    ROOT_DIR =  os.path.abspath(os.path.join(__file__ ,"../../.."))
    return os.path.join(ROOT_DIR, 'data/')

DAYS = ['21:00', '22:00', '23:00', '20:00', '13:00έως16:00']
combinations = [2, 3, 4, 5]
with open(get_data_directory()+'txts/time_combinations.txt', 'wt',encoding='utf8') as out:
    for c in combinations:
        x = {}
        k = 0
        for i in itertools.combinations(DAYS, c):
            x[tuple(sorted(i))] = 0
        with open(get_data_directory() +'teams.csv', encoding='utf-8') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                days = row[2].replace(" ", "").split("+")
                for i in itertools.combinations(days, c):
                    x[tuple(sorted(i))] = x[tuple(sorted(i))] + 1
        output = sorted(x.items(), key=lambda x: x[1], reverse=True)
        pprint(output, stream=out)
 