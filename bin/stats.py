import json
from os import listdir
from os.path import isfile, join
from prettytable import PrettyTable

def stats():
    ##Single thread implementation
    #Get json files listing
    path = '../data/'
    files = [f for f in listdir(path) if isfile(join(path, f)) and '.json' in f]
    #Only take the year files
    files.sort()
    files = files[:-2]
    
    #stat data
    total = 0
    cvss_total = 0
    cvss_score = [0] * 10
    
    #Open files
    for fs in files:
        with open('../data/'+fs) as f:
            data = json.load(f)
            #Look for data for stats
            for d in data['CVE_Items']:
                if "baseMetricV3" in d['impact']:
                    total += 1
                    cvss = (d['impact']['baseMetricV3']['cvssV3']['baseScore'])
                    cvss_total += cvss
                    if cvss < 1:
                        cvss_score[0] += 1
                    elif cvss < 2:
                        cvss_score[1] += 1
                    elif cvss < 3:
                        cvss_score[2] += 1
                    elif cvss < 4:
                        cvss_score[3] += 1
                    elif cvss < 5:
                        cvss_score[4] += 1
                    elif cvss < 6:
                        cvss_score[5] += 1
                    elif cvss < 7:
                        cvss_score[6] += 1
                    elif cvss < 8:
                        cvss_score[7] += 1
                    elif cvss < 9:
                        cvss_score[8] += 1
                    else:
                        cvss_score[9] += 1
    
    #Print data
    table = PrettyTable(['CVSS Score', '# of vulns', '  %'])
    table.align = "l"
    for i in range(len(cvss_score)):
        if cvss_score[i] == 0:
            percentage = 0
        else:
            percentage = round(cvss_score[i]/total * 100, 2)
        table.add_row([str(str(i) + '-' + str(i+1)), cvss_score[i], percentage])
    
    #Save stats for later
    with open('../data/stats.dat', 'w') as f:
        f.write(str(table))
        f.write('\nTotal CVE entries: ' + str(total) + '\n')
        f.write('Average CVSS score: ' + str(cvss_total/total))
