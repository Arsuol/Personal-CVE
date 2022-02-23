__author__ = "Arthur Tressuol"
__email__ = "arthur.tressuol@gmail.com"
__credits__ = "Arthur Tressuol"
__date__ = "February 2022"
__revision__ = "1.0"

import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from cve_module import insert_newlines

def github(cve_id):
    #Get search page
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    url = "https://github.com/search?o=desc&q=" + cve_id + "&s=stars&type=Repositories"
    driver.get(url)
    time.sleep(5)

    #Parse with beautiful soup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    
    #Get relevant information
    table = PrettyTable(['url', 'Description', 'Stars', 'Upadated', 'Tags'])
    table.align = "l"
    tmp = soup.find_all("div", {"class": "mt-n1 flex-auto"})
    
    for e in tmp:
        tmp_str = str(e)
        #url
        index1 = tmp_str.find('"url":')
        index2 = index1 + tmp_str[index1:].find('"}')
        url = tmp_str[index1+7:index2].lstrip(' ').rstrip()
        #description
        index1 = tmp_str.find('<p class="mb-1">')
        index2 = index1 + tmp_str[index1:].find('</p>')
        description = tmp_str[index1+17:index2].lstrip(' ').rstrip()
        description = description.replace('<em>', '')
        description = description.replace('</em>', '')
        description = insert_newlines(description, 50)
        #stars
        index1 = tmp_str.find('/svg')
        index2 = index1 + tmp_str[index1:].find('</a>')
        stars = tmp_str[index1+6:index2].lstrip(' ').rstrip()
        #language
        #print('lang: ' + language)
        #licence
        #print('licence: ' + licence)
        #update
        index1 = tmp_str.find('datetime')
        index1 += tmp_str[index1:].find('title')
        index2 = tmp_str[index1:].find('>')
        update = tmp_str[index1+7:index1+index2-1].lstrip(' ').rstrip()
        index1 = update.find(',')
        index1 += update[index1+1:].find(',')
        update = update[:index1+1]
        #tags
        tags = []
        while 1:
            index1 = tmp_str.find('title="Topic:')
            if index1 == -1:
                break
            index2 = index1 + tmp_str[index1:].find('">')
            tags.append(tmp_str[index1+14:index2])
            tmp_str = tmp_str[index1+5:]
        string = '' 
        if len(tags) > 0: 
            tags[0] = tags[0] + '; '
        for i in range(len(tags[1:])):
            if i%2 == 0:
                tags[i+1] = tags[i+1] + ';\n'
            else:
                tags[i+1] = tags[i+1] + '; '
            string = string + tags[i]
        table.add_row([url, description, stars, update, string])
    
    print(table)
