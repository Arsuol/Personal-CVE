import json
from os import listdir
from os.path import isfile, join
import cve_module

limit = 10

#Get json files listing
path = '../data/'
files = [f for f in listdir(path) if isfile(join(path, f)) and '.json' in f]
files = sorted(files)

#Only take the last years' CVE
file = '../data/' + files[-3]

#Open file
with open(file) as f:
    data = json.load(f)

table = cve_module.create_table(data, limit)
print(table)