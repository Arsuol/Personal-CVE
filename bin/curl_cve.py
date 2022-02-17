#!/usr/bin/env python
""" 
Curl individual CVE and store result as json
"""
__author__ = "Arthur Loussert"                                                   
__email__ = "arsuol@gmail.com"                                                
__credits__ = "Arthur Loussert"                                                   
__date__ = "February 2022"                                                      
__revision__ = "1.0"                                                            
__maintainer__ = "Arthur Loussert" 

from bs4 import BeautifulSoup
import requests


## Redo this part: 
##   - url need to be all url for all cve
##   - don't need to write page, it was only a test
##   - beautiful soup from page.content, dont save/open html page
#url_nist = "https://nvd.nist.gov/vuln/detail/CVE-2021-44228"
#page = requests.get(url_nist)
#soup = BeautifulSoup(page.content, 'html.parser')
#f = open("./test.txt", "w")
#f.write(page.text)


file = open("test.txt", "r")
content = file.read()
soup = BeautifulSoup(content, 'html.parser')

tmp = soup.find(class_="bs-callout bs-callout-info")
cve_id          = tmp.findChildren()[3].text
published_date  = tmp.findChildren()[7].text
last_modified   = tmp.findChildren()[11].text
cna_assigned    = tmp.findChildren()[15].text #"source" on the nist page

tmp_str = str(tmp.findChildren()[3])
index1 = tmp_str.find('href="')+6
index2 = tmp_str[index1:].find('"')
mitre_ref = tmp_str[index1 : index1+index2]





print("-----")
print("-----")




status = soup.find(class_="h4Size").text
#print(status)
description = soup.select('p[data-testid="vuln-description"]')[0].text
#print(description)
cvss_v2 = [] #base, impact, exploitability
cvss_v3 = [] #base, impact, exploitability
gained_access = " "
vul_type = " "
cwe = []
caped = [] #??
access = [] #vector, complexity, authentication
impact = [] #Confidentiality, Integrity, Availability
cvss_vector_v2 = " "
cvss_vector_v3 = " "
Last_major_update = " "
cna_score = " "
cna_vector = []
references = []
vuln_conf = []
