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

##CVSS Format
#Version
#CNA
#Base Score
#Severity
#Vector
#Impact Score
#Exploitability Score
#Attack Vector (AV)
#Attack Complexity (AC)
#Privileges Required (PR)
#User Interaction (UI)
#Scope (S)
#Confidentiality (C)
#Itegrity (I)
#Availability (A)

from bs4 import BeautifulSoup
import requests
import unicodedata

debug = False


## Redo this part: 
##   - url need to be all url for all cve
##   - don't need to write page, it was only a test
##   - beautiful soup from page.content, dont save/open html page
#url_nist = "https://nvd.nist.gov/vuln/detail/CVE-2021-44228"
#url_nist = "https://nvd.nist.gov/vuln/detail/CVE-2021-44228/cpes"
#page = requests.get(url_nist)
#soup = BeautifulSoup(page.content, 'html.parser')
#f = open("./log4js_cpes.txt", "w")
#f.write(page.text)

file = open("log4js.txt", "r")
#file = open("double_cvss3.txt", "r")
#file = open("test.txt", "r")
content = file.read()
soup = BeautifulSoup(content, 'html.parser')

tmp = soup.find(class_="bs-callout bs-callout-info")
cve_id          = tmp.findChildren()[3].text
published_date  = tmp.findChildren()[7].text
last_modified   = tmp.findChildren()[11].text
cna_assigned    = tmp.findChildren()[15].text #"source" on the nist page
description = soup.select('p[data-testid="vuln-description"]')[0].text

tmp_str = str(tmp.findChildren()[3])
index1 = tmp_str.find('href="')+6
index2 = tmp_str[index1:].find('"')
mitre_ref = tmp_str[index1 : index1+index2]

tmp = soup.find(class_="h4Size")
if tmp != None:
    status = soup.find(class_="h4Size").text
else:
    status = " "

cvss = []
cvss_index = 0

# CVSS v3: NVD
tmp = soup.find(id="nistV3MetricHidden")
if tmp != None:
    cvss.append([])
    tmp_str = str(tmp)
    index1 = tmp_str.find("CVSS v")
    index2 = tmp_str[index1:].find('Severity')
    cvss[cvss_index].append(tmp_str[index1+6 : index1+index2-1])
    cna = soup.find(attrs={"data-testid": "vuln-cvss3-source-nvd"})
    cvss[cvss_index].append(cna.text)
    index1 = tmp_str.find("vuln-cvssv3-base-score")
    index2 = tmp_str[index1:].find('&lt')
    cvss[cvss_index].append(tmp_str[index1+27 : index1+index2-1])
    index1 = tmp_str.find("vuln-cvssv3-base-score-severity")
    index2 = tmp_str[index1:].find('&lt')
    cvss[cvss_index].append(tmp_str[index1+36 : index1+index2])
    index1 = tmp_str.find("vuln-cvssv3-vector")
    index2 = tmp_str[index1:].find('&lt')
    cvss[cvss_index].append(tmp_str[index1+24 : index1+index2-1])
    index1 = tmp_str.find("impact-score")
    index2 = tmp_str[index1:].find('&lt')
    cvss[cvss_index].append(tmp_str[index1+18 : index1+index2-1])
    index1 = tmp_str.find("exploitability-score")
    index2 = tmp_str[index1:].find('&lt')
    cvss[cvss_index].append(tmp_str[index1+26 : index1+index2-1])
    cvss_index += 1

# CVSS v3: Source
tmp = soup.find(id="cnaV3MetricHidden")
if tmp != None:
    cvss.append([])
    tmp_str = str(tmp)
    index1 = tmp_str.find("CVSS v")
    index2 = tmp_str[index1:].find('Severity')
    cvss[cvss_index].append(tmp_str[index1+6 : index1+index2-1])
    cna = soup.find(attrs={"data-testid": "vuln-cvss3-source-cna"})
    cvss[cvss_index].append(cna.text)
    index1 = tmp_str.find("vuln-cvssv3-base-score")
    index2 = tmp_str[index1:].find('&lt')
    cvss[cvss_index].append(tmp_str[index1+27 : index1+index2-1])
    index1 = tmp_str.find("vuln-cvssv3-base-score-severity")
    index2 = tmp_str[index1:].find('&lt')
    cvss[cvss_index].append(tmp_str[index1+36 : index1+index2])
    index1 = tmp_str.find("vuln-cvssv3-vector")
    index2 = tmp_str[index1:].find('&lt')
    cvss[cvss_index].append(tmp_str[index1+24 : index1+index2-1])
    index1 = tmp_str.find("impact-score")
    index2 = tmp_str[index1:].find('&lt')
    cvss[cvss_index].append(tmp_str[index1+18 : index1+index2-1])
    index1 = tmp_str.find("exploitability-score")
    index2 = tmp_str[index1:].find('&lt')
    cvss[cvss_index].append(tmp_str[index1+26 : index1+index2-1])
    cvss_index += 1

#CVSS v2
tmp = soup.find(id="nistV2MetricHidden")
if tmp != None:
    cvss.append([])
    tmp_str = str(tmp)
    index1 = tmp_str.find("CVSS v")
    index2 = tmp_str[index1:].find('Severity')
    cvss[cvss_index].append(tmp_str[index1+6 : index1+index2-1])
    cna = soup.find(attrs={"data-testid": "vuln-cvss2-source-nvd"})
    cvss[cvss_index].append(cna.text)
    index1 = tmp_str.find("vuln-cvssv2-base-score")
    index2 = tmp_str[index1:].find('&lt')
    cvss[cvss_index].append(tmp_str[index1+27 : index1+index2-2])
    index1 = tmp_str.find("vuln-cvssv2-base-score-severity")
    index2 = tmp_str[index1:].find('&lt')
    cvss[cvss_index].append(tmp_str[index1+36 : index1+index2])
    index1 = tmp_str.find("vuln-cvssv2-vector")
    index2 = tmp_str[index1:].find('&lt')
    cvss[cvss_index].append(tmp_str[index1+24 : index1+index2-1])
    index1 = tmp_str.find("impact-subscore")
    index2 = tmp_str[index1:].find('&lt')
    cvss[cvss_index].append(tmp_str[index1+20 : index1+index2])
    index1 = tmp_str.find("exploitability-score")
    index2 = tmp_str[index1:].find('&lt')
    cvss[cvss_index].append(tmp_str[index1+25 : index1+index2])
    cvss_index += 1

#CWE
cwe = []
cwe_index = 0
while 1:
    name = "vuln-CWEs-row-" + str(cwe_index)
    tmp = soup.find(attrs={"data-testid": name})
    if tmp == None:
        break
    cwe.append([])
    tmp_str = str(tmp)
    #href to CWE
    index1 = tmp_str.find('href="')+6
    index2 = index1 + tmp_str[index1:].find('"')
    cwe[cwe_index].append(tmp_str[index1 : index2])
    #CWE ID
    index1 = index2 + tmp_str[index2:].find('>')
    index2 = index1 + tmp_str[index1:].find('<')
    cwe[cwe_index].append(tmp_str[index1+1 : index2])
    #CWE Description
    index1 = index2 + tmp_str[index2:].find('vuln-CWEs-link-')
    index1 = index1 + tmp_str[index1:].find('>')
    index2 = index1 + tmp_str[index1:].find('<')
    cwe[cwe_index].append(tmp_str[index1+1 : index2])
    cwe_index += 1
#CWE Sources
for i in range(len(cwe)):
    index = 0
    sources = []
    while 1:
        name = "vuln-cwes-assigner-" + str(i) + "-" + str(index)
        index += 1
        tmp = soup.find(attrs={"data-testid": name})
        if tmp == None:
            break
        index1 = tmp.text[2:].find('\n')
        sources.append(tmp.text[2:index1])
    cwe[i].append(sources)

#References
references = []
ref_index = 0
while 1:
    name = "vuln-hyperlinks-row-" + str(ref_index)
    tmp = soup.find(attrs={"data-testid": name})
    if tmp == None:
        break
    ref_index += 1
    tmp_l = str(tmp.text).splitlines()
    tmp_l[:] = (value for value in tmp_l if value != "") #remove empty strings
    tmp_l[:] = (value for value in tmp_l if value[0] != "\t") #remove empty strings
    for i in range(len(tmp_l)):
        tmp_l[i] = unicodedata.normalize("NFKD", tmp_l[i])
        if tmp_l[i][-1] == ' ':
            tmp_l[i] = tmp_l[i][:-1]
    references.append(tmp_l)





#vuln_conf = []


if debug == True:
    print("cve_id " + cve_id)
    print("published date " + published_date)
    print("last modified " + last_modified)
    print("cna assigned " + cna_assigned)
    print("description " + description)
    print("mitre ref " + mitre_ref)
    print("status " + status)
    print("cvss " + str(cvss))
    print("cwe " + str(cwe))
    print("references:\n")
    print(*references, sep='\n')

