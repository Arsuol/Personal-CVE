import json
from os import listdir
from os.path import isfile, join
import cve_module

def search(args):
    if args == '':
        print("usage: search keyword1 [keyword2 ...]")
        return None

    #Process keywords and
    #Transform keywords to lowercase
    search_keywords = []
    if isinstance(args, list):
        for i in range(len(args)):
            search_keywords.append(args[i].lower())
    else:
        search_keywords.append(args.lower())
    
    #Get json files listing
    path = '../data/'
    files = [f for f in listdir(path) if isfile(join(path, f)) and '.json' in f]
    files = sorted(files)
    
    #Only take the year files
    files = files[:-2]
    
    l = []
    #Open files
    for fs in files:
        with open('../data/'+fs) as f:
            data = json.load(f)
            #Search for CVE with keywords
            for d in data['CVE_Items']:
                description = (d['cve']['description']['description_data'][0]['value'])
                if all(x in description.lower() for x in search_keywords):
                    l.append(d)
    
    #Process table
    table = cve_module.search_table(l)
    print(table)
