#!/usr/bin/env python
""" 
Mine for actual CVE in CVRF files and creates a list.
Create a file with last update date of each cvrf file.
"""
__author__ = "Arthur Loussert"                                                   
__email__ = "arsuol@gmail.com"                                                
__credits__ = "Arthur Loussert"                                                   
__date__ = "February 2022"                                                      
__revision__ = "1.0"                                                            
__maintainer__ = "Arthur Loussert" 

from bs4 import BeautifulSoup

file_path = []

with open('../data/cvrf-links.txt') as f:
    links = f.read().splitlines()
    for link in links:
        file_path.append("../data/cvrf-" + link[-8:-4] + ".xml")

f_cvrf_update = open("../data/cvrf-update.txt", "w")

#("./data/cvrf-2022.xml"
for e in file_path: 
    file = open(e, "r")
    content = file.read()
    soup = BeautifulSoup(content, 'xml')

    tmp = soup.find('DocumentTitle')
    update_date = tmp.text[-8:]
    f_cvrf_update.write(e[-8:-4] + " " + update_date + "\n")

    vuln = soup.find_all('Vulnerability')

    file_name = "../data/cve-ids-" + e[-8:-4] + ".txt"
    with open(file_name, 'w') as f:
        for i in range(len(vuln)):
            if ("** RESERVED ** This candidate has been reserved" not in vuln[i].text):
                cve_id = vuln[i].findChildren('CVE')
                f.write("%s\n" % cve_id[0].text)
