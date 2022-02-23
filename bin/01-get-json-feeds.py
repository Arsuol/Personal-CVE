#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import wget
import os
import json

#Get NIST's feed page
url_nist_feed = "https://nvd.nist.gov/vuln/data-feeds"
page = requests.get(url_nist_feed)
soup = BeautifulSoup(page.content, 'html.parser')
##TODO: Remove when done
#file = open("../data/nist_feed.html", "r")
#content = file.read()
#soup = BeautifulSoup(content, 'html.parser')

#Parse the page: only keep urls to download rson cve zip files
tmp_l = str(soup.find(id="divJSONFeeds")).splitlines()
json_zips = []
dates = []
for i in range(len(tmp_l)):
    if ".json.zip" in tmp_l[i]:
        index = tmp_l[i].find(".json.zip")
        json_zips.append(tmp_l[i][9:index+9])
        dates.append(tmp_l[i-17])

#Create new dictionary
new_dict = {}
for i in range(len(dates)):
    new_dict[json_zips[i]] = dates[i]

#If it is not the first time using the tool: check for updates
filename = '../data/nist_feeds_logs.txt'
tmp_dict = new_dict.copy()
if os.path.isfile(filename):
    #Load data from past update
    old_dict = json.load(open(filename))
    #Keep only updated entries
    for key in old_dict:
        if old_dict[key] == tmp_dict[key]:
            tmp_dict.pop(key)

#Print data for future database update
json.dump(new_dict, open(filename,'w'))

##Get the zip files, unzip, rm the zips
for key in tmp_dict:
    file_name = key[20:]
    file_path = "../data/"
    url = "https://nvd.nist.gov/" + key
    wget.download(url)
    cmd = "unzip " + file_name
    os.system(cmd)
    cmd = "mv " + file_name[:-4] + " " + file_path
    os.system(cmd)
    cmd = "rm " + file_name
    os.system(cmd)
    json_zips[i] = file_path + file_name[:-4]

