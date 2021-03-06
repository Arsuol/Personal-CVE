__author__ = "Arthur Tressuol"
__email__ = "arthur.tressuol@gmail.com"
__credits__ = "Arthur Tressuol"
__date__ = "February 2022"
__revision__ = "1.0"

import sys
import json
from prettytable import PrettyTable
import cve_module

def recent(args):
    #Get arguments
    limit = 10
    if isinstance(args, list):
        if args[0].isdigit():
            limit = int(args[0])
    else:
        if args.isdigit():
            limit = int(args)
    
    file = "../data/nvdcve-1.1-recent.json"
    with open(file) as f:
        data = json.load(f)
    
    table = cve_module.basic_table(data, limit)
    print(table)
