import json
from prettytable import PrettyTable
import cve_module

limit = 10

file = "../data/nvdcve-1.1-recent.json"
with open(file) as f:
    data = json.load(f)

table = cve_module.create_table(data, limit)
print(table)
