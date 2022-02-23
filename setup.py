__author__ = "Arthur Tressuol"
__email__ = "arthur.tressuol@gmail.com"
__credits__ = "Arthur Tressuol"
__date__ = "February 2022"
__revision__ = "1.0"

import os

packet_manager = 'apt-get install'

os.system(packet_manager + " python3")
os.system(packet_manager + " python3-pip")
os.system("pip3 install beautifulsoup4")
os.system("pip3 install selenium")
os.system("pip3 install webdriver-manager")
os.system("pip3 install wget")
os.system("pip3 install PrettyTable")
os.system("pip3 install praw")
os.system("pip3 install tweepy")
os.system("pip3 install google-api-python-client")
