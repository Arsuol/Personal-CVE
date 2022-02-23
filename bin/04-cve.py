import sys
from os import listdir
from os.path import isfile, join
import json
import cve_module

#Get arguments
if len(sys.argv) > 1:
    search_id = str(sys.argv[1]).upper()
else:
    print("usage: cve CVE-XXXX-XXXX")
    quit()

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
if table == "":
    print('CVE Not Found!')
else:
    print(table)
