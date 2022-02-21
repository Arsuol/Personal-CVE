#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import wget
import os

##Get NIST's feed page
#url_nist_feed = "https://nvd.nist.gov/vuln/data-feeds"
#page = requests.get(url_nist_feed)
#soup = BeautifulSoup(page.content, 'html.parser')
#TODO: Remove when done
file = open("../data/nist_feed.html", "r")
content = file.read()
soup = BeautifulSoup(content, 'html.parser')

#Parse the page: only keep urls to download rson cve zip files
tmp_l = str(soup.find(id="divJSONFeeds")).splitlines()
json_zips = []
for e in tmp_l:
    if ".json.zip" in e:
        index = e.find(".json.zip")
        json_zips.append(e[9:index+9])

#Get the zip files, unzip, rm the zips
for i in range(len(json_zips)):
    file_name = json_zips[i][20:]
    file_path = "../data/"
#    url = "https://nvd.nist.gov/" + json_zips[i]
#    wget.download(url)
#    cmd = "unzip " + file_name
#    os.system(cmd)
#    cmd = "mv " + file_name[:-4] + " " + file_path
#    os.system(cmd)
#    cmd = "rm " + file_name
#    os.system(cmd)
    json_zips[i] = file_path + file_name[:-4]





