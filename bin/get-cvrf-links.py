#!/usr/bin/env python
""" 
Get links to CVRF files from cve.org 
"""
__author__ = "Arthur Loussert"                                                   
__email__ = "arsuol@gmail.com"                                                
__credits__ = "Arthur Loussert"                                                   
__date__ = "February 2022"                                                      
__revision__ = "1.0"                                                            
__maintainer__ = "Arthur Loussert" 

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://www.cve.org/Downloads")

links = driver.find_elements(By.TAG_NAME, "a")
with open('./data/cvrf-links.txt', 'w') as f:
    for e in links:
        tmp = e.get_attribute("href")
        if "cvrf-year" in tmp:
            f.write("%s\n" % tmp)

driver.quit()
