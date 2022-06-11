import csv
import json

data_ads = []
with open('ads.csv', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        data_ads.append(row)

json_data_ads = json.dumps(data_ads)


data_cat = []
with open('categories.csv', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        data_cat.append(row)

json_data_cat = json.dumps(data_cat)

print(json_data_cat)
