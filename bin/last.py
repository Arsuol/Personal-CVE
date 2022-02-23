__author__ = "Arthur Tressuol"
__email__ = "arthur.tressuol@gmail.com"
__credits__ = "Arthur Tressuol"
__date__ = "February 2022"
__revision__ = "1.0"

import sys
import json
from os import listdir
from os.path import isfile, join
import cve_module

def last(args):
    #Get arguments
    limit = 10
    if isinstance(args, list):
        if args[0].isdigit():
            limit = int(args[0])
    else:
        if args.isdigit():
            limit = int(args)
    
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
