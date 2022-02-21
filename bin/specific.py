import json
from os import listdir
from os.path import isfile, join
import cve_module

search_id = 'CVE-2021-44228'

#Get json files listing
path = '../data/'
files = [f for f in listdir(path) if isfile(join(path, f)) and '.json' in f]
files = sorted(files)

#Only take the right year files
for f in files:
    if search_id[4:8] in f:
        with open('../data/'+files[-4]) as f:
            data = json.load(f)
        break

#Search for CVE id
table = ''
for d in data['CVE_Items']:
    if (d['cve']['CVE_data_meta']['ID']) == search_id:
        table = cve_module.specific_table(d)
        break
print(table)
