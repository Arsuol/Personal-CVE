__author__ = "Arthur Tressuol"
__email__ = "arthur.tressuol@gmail.com"
__credits__ = "Arthur Tressuol"
__date__ = "February 2022"
__revision__ = "1.0"

import json
from os import listdir
from os.path import isfile, join
import threading
import cve_module

th_number = 4
th_return = []

def thread_func(args):
    print(args)
    l = []
    for i in range(len(args[1])):
        with open('../data/'+args[1][i]) as f:
            data = json.load(f)
            #Search for CVE with keywords
            for d in data['CVE_Items']:
                description = (d['cve']['description']['description_data'][0]['value'])
                if all(x in description.lower() for x in args[2]):
                    l.append(d)
    #Process table
    table = cve_module.search_table(l)
    #return
    th_return.append(table)


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
    files.sort(reverse=True)
    #Only take the year files
    files = files[2:]
    
    ##Single thread implementation
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

    ##Threaded implementation: NOT FASTER, TODO: Debug
    #Distribute work to threads
    #remain = len(files)
    #th_load = []
    #for i in range(th_number, 0, -1):
    #    if remain % i == 0:
    #        load = int(remain / i)
    #    else:
    #        load = int(remain / i) + 1
    #    remain -= load
    #    th_load.append(load)
    #limit = 0
    #th_args = []
    #for i in range(th_number):
    #    file_list = []
    #    for j in range(limit, limit+th_load[i]):
    #        file_list.append(files[j])
    #    limit += th_load[i]
    #    th_args.append((i, file_list, search_keywords))

    ##Launch threads
    #jobs = []
    #for i in range(th_number):
    #    x = threading.Thread(target=thread_func, args=(th_args[i],))
    #    jobs.append(x)
    #for j in jobs:
    #    j.start()
    #for j in jobs:
    #    j.join()
    #
    ##Print results
    #for i in range(th_number):
    #    print(th_return[i])
