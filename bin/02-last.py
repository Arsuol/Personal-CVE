import sys
import json
from os import listdir
from os.path import isfile, join
import cve_module

#Get arguments
limit = 10
if len(sys.argv) > 1:
    if str(sys.argv[1]).isdigit():
        limit = int(sys.argv[1])

#Get json files listing
path = '../data/'
files = [f for f in listdir(path) if isfile(join(path, f)) and '.json' in f]
files = sorted(files)

#Only take the last years' CVE
file = '../data/' + files[-3]

#Open file
with open(file) as f:
    data = json.load(f)

table = cve_module.basic_table(data, limit)
print(table)
