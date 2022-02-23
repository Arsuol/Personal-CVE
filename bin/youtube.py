__author__ = "Arthur Tressuol"
__email__ = "arthur.tressuol@gmail.com"
__credits__ = "Arthur Tressuol"
__date__ = "February 2022"
__revision__ = "1.0"

from googleapiclient.discovery import build
import json
from prettytable import PrettyTable
from cve_module import insert_newlines

def get_api_key(json_file = '../conf/youtube_conf.json'):
    with open(json_file) as f:
        data = json.load(f)
    api_key = (data['ApiKey'])
    youtube = build('youtube', 'v3', developerKey=api_key)
    return youtube

def youtube(cve_id):
    youtube = get_api_key()
    request = youtube.search().list(part='snippet', q=cve_id, type='video', maxResults=10)
    response = request.execute()
    
    #Table creation
    table = PrettyTable(['Channel', 'Title', 'Description', 'Published'])
    table.align = "l"
    
    #Get relevant information
    for e in response['items']:
        title           = insert_newlines(e['snippet']['title'], 50)
        description     = insert_newlines(e['snippet']['description'], 50)
        publish_date    = e['snippet']['publishedAt'][:10]
        channel         = e['snippet']['channelTitle']
        table.add_row([channel, title, description, publish_date])
    
    print(table)
