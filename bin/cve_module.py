import json
from prettytable import PrettyTable

def insert_newlines(string, every=64):
    return '\n'.join(string[i:i+every] for i in range(0, len(string), every))

def create_table(data, limit):
    table = PrettyTable(['CVE', 'CVSS', 'Summary', 'Published', 'Updated'])
    i = 0
    for d in data['CVE_Items']:
        id_ = (d['cve']['CVE_data_meta']['ID'])
        description = (d['cve']['description']['description_data'][0]['value'])
        description = insert_newlines(description)
        if "baseMetricV3" in d['impact']:
            cvss = (d['impact']['baseMetricV3']['cvssV3']['baseScore'])
        else:
            cvss = 'NA'
        up_date = (d['lastModifiedDate'])
        pub_date = (d['publishedDate'])
        table.add_row([id_, cvss, description, pub_date[:10], up_date[:10]])
        i+=1
        if i == limit:
            break
    return table

