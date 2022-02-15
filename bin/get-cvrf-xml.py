#!/usr/bin/env python
""" 
Downloads CVRF files from cve.org 
Get the links from a file previously generated
"""
__author__ = "Arthur Loussert"                                                   
__email__ = "arsuol@gmail.com"                                                
__credits__ = "Arthur Loussert"                                                   
__date__ = "February 2022"                                                      
__revision__ = "1.0"                                                            
__maintainer__ = "Arthur Loussert" 

import requests

with open('data/cvrf-links.txt') as f:
    links = f.read().splitlines()

#print (*links, sep = "\n")

for link in links:
    file_path = "./data/cvrf-" + link[-8:-4] + ".xml"
    print ("getting file: " + file_path)
    with open(file_path, 'w') as f:
        r = requests.get(link)
        f.write(r.text)
