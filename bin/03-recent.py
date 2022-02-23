import sys
import json
from prettytable import PrettyTable
import cve_module

#Get arguments
limit = 10
if len(sys.argv) > 1:
    if str(sys.argv[1]).isdigit():
        limit = int(sys.argv[1])

file = "../data/nvdcve-1.1-recent.json"
with open(file) as f:
    data = json.load(f)

table = cve_module.basic_table(data, limit)
print(table)
