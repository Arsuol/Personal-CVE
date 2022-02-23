from os import listdir
from os.path import isfile, join
import json
import cve_module

def cve(args):
    #Get arguments
    if args == '':
        print("usage: cve CVE-XXXX-XXXX")
        return None
    search_id = ''
    if isinstance(args, list):
        search_id = args[0].upper()
    else:
        search_id = args.upper()
    
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
