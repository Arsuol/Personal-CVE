import json
from prettytable import PrettyTable
from prettytable import PLAIN_COLUMNS

def insert_newlines(string, every):
    return '\n'.join(string[i:i+every] for i in range(0, len(string), every))

def insert_newlines_and(string, to_add, every=64):
    return ('\n'+to_add).join(string[i:i+every] for i in range(0, len(string), every))

def basic_table(data, limit):
    table = PrettyTable(['CVE', 'CVSS', 'Summary', 'Published', 'Updated'])
    table.align = "l"
    i = 0
    for d in data['CVE_Items']:
        id_ = (d['cve']['CVE_data_meta']['ID'])
        description = (d['cve']['description']['description_data'][0]['value'])
        description = insert_newlines(description, 64)
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

def specific_table(d):
    ##Get data
    #cve id
    id_ = (d['cve']['CVE_data_meta']['ID'])
    #source
    source = (d['cve']['CVE_data_meta']['ASSIGNER'])
    #description
    description = (d['cve']['description']['description_data'][0]['value'])
    description = insert_newlines(description, 128)
    #up_date
    up_date = (d['lastModifiedDate'])
    #pub date
    pub_date = (d['publishedDate'])
    #cwe
    cwe = (d['cve']['problemtype']['problemtype_data'][0]['description'][0]['value'])
    #references
    ref = []
    for i in range(len(d['cve']['references']['reference_data'])):
        ref_e = []
        ref_e.append(d['cve']['references']['reference_data'][i]['url'])
        ref_e.append(d['cve']['references']['reference_data'][i]['name'])
        ref_e.append(d['cve']['references']['reference_data'][i]['refsource'])
        ref_e.append(d['cve']['references']['reference_data'][i]['tags'])
        ref.append(ref_e)
    cvss3 = []
    if "baseMetricV3" in d['impact']:
        cvss3.append(d['impact']['baseMetricV3']['cvssV3']['vectorString'])
        cvss3.append(d['impact']['baseMetricV3']['cvssV3']['attackVector'])
        cvss3.append(d['impact']['baseMetricV3']['cvssV3']['attackComplexity']) 
        cvss3.append(d['impact']['baseMetricV3']['cvssV3']['privilegesRequired'])
        cvss3.append(d['impact']['baseMetricV3']['cvssV3']['userInteraction'])
        cvss3.append(d['impact']['baseMetricV3']['cvssV3']['scope'])
        cvss3.append(d['impact']['baseMetricV3']['cvssV3']['confidentialityImpact'])
        cvss3.append(d['impact']['baseMetricV3']['cvssV3']['integrityImpact'])
        cvss3.append(d['impact']['baseMetricV3']['cvssV3']['availabilityImpact'])
        cvss3.append(d['impact']['baseMetricV3']['cvssV3']['baseScore'])
        cvss3.append(d['impact']['baseMetricV3']['cvssV3']['baseSeverity'])
        cvss3.append(d['impact']['baseMetricV3']['exploitabilityScore'])
        cvss3.append(d['impact']['baseMetricV3']['impactScore'])
    else:
        for i in range(13):
            cvss3.append('NA')
    cvss2 = []
    if "baseMetricV2" in d['impact']:
        cvss2.append(d['impact']['baseMetricV2']['cvssV2']['vectorString'])#
        cvss2.append(d['impact']['baseMetricV2']['cvssV2']['accessVector'])#
        cvss2.append(d['impact']['baseMetricV2']['cvssV2']['accessComplexity'])#
        cvss2.append(d['impact']['baseMetricV2']['cvssV2']['authentication'])#
        cvss2.append(d['impact']['baseMetricV2']['cvssV2']['confidentialityImpact'])#
        cvss2.append(d['impact']['baseMetricV2']['cvssV2']['integrityImpact'])#
        cvss2.append(d['impact']['baseMetricV2']['cvssV2']['availabilityImpact'])#
        cvss2.append(d['impact']['baseMetricV2']['cvssV2']['baseScore'])#
        cvss2.append(d['impact']['baseMetricV2']['severity'])#
        cvss2.append(d['impact']['baseMetricV2']['exploitabilityScore'])#
        cvss2.append(d['impact']['baseMetricV2']['impactScore'])#
        cvss2.append(d['impact']['baseMetricV2']['acInsufInfo'])
        cvss2.append(d['impact']['baseMetricV2']['obtainAllPrivilege'])#
        cvss2.append(d['impact']['baseMetricV2']['obtainUserPrivilege'])#
        cvss2.append(d['impact']['baseMetricV2']['obtainOtherPrivilege'])#
        cvss2.append(d['impact']['baseMetricV2']['userInteractionRequired'])#
    else:
        for i in range(16):
            cvss2.append('NA')

    ##Create Table
    table = PrettyTable(['a','b'])
    table.set_style(PLAIN_COLUMNS)
    table.header = False
    table.align = "l"
    table.add_row(["CVE ID:", id_])
    table.add_row(["href:", "https://cve.mitre.org/cgi-bin/cvename.cgi?name=" + id_])
    table.add_row(["Source:", source])
    table.add_row(["Description:", description])
    table.add_row(["Published:", pub_date])
    table.add_row(["Last modified:", up_date])
    table.add_row(["CWE", cwe])
    #CVSS3
    tmp_str = ''
    tmp_str = tmp_str + 'Vector:           '   + cvss3[0]
    tmp_str = tmp_str + '\nScore:            ' + str(cvss3[9])
    tmp_str = tmp_str + '\nSeverity:         ' + cvss3[10]
    tmp_str = tmp_str + '\nExploit Score:    ' + str(cvss3[11])
    tmp_str = tmp_str + '\nImpact Score:     ' + str(cvss3[12])
    tmp_str = tmp_str + '\nUser Interaction: ' + cvss3[4]
    tmp_str = tmp_str + '\nScope:            ' + cvss3[5]
    table.add_row(["CVSS v3.x:", tmp_str])
    #CVSS3 Access
    table2 = PrettyTable(['Vector','Complexity', 'Priv Req'])
    table2.add_row([ cvss3[1], cvss3[2], cvss3[3] ])
    table.add_row(["CVSS 3.x\nAcces:", table2])
    #CVSS3 Impact
    table2 = PrettyTable(['Confidentiality', 'Integrity', 'Availability'])
    table2.add_row([ cvss3[6], cvss3[7], cvss3[8] ])
    table.add_row(["CVSS 3.x\nImpact:", table2])
    #CVSS2
    tmp_str = ''
    tmp_str = tmp_str + 'Vector:           ' + cvss2[0]
    tmp_str = tmp_str + '\nScore:            ' + str(cvss2[7])
    tmp_str = tmp_str + '\nSeverity:         ' + cvss2[8]
    tmp_str = tmp_str + '\nExploit Score:    ' + str(cvss2[9])
    tmp_str = tmp_str + '\nImpact Score:     ' + str(cvss2[10])
    tmp_str = tmp_str + '\nUser Interaction: ' + str(cvss2[15])
    table.add_row(["CVSS v2.x:", tmp_str])
    #CVSS2 Access
    table2 = PrettyTable(['Vector','Complexity', 'Priv Req'])
    table2.add_row([ cvss2[1], cvss2[2], cvss2[3] ])
    table.add_row(["CVSS 2.x\nAcces:", table2])
    #CVSS2 Impact
    table2 = PrettyTable(['Confidentiality', 'Integrity', 'Availability'])
    table2.add_row([ cvss2[4], cvss2[5], cvss2[6] ])
    table.add_row(["CVSS 2.x\nImpact:", table2])
    #CVSS2 Priv Obtained
    table2 = PrettyTable(['All', 'User', 'Other'])
    table2.add_row([ cvss2[12], cvss2[13], cvss2[14] ])
    table.add_row(["CVSS v2.x\nPriv Obtained:", table2])
    #Vuln confs
    vuln_conf_url = "https://nvd.nist.gov/vuln/detail/" + id_ + "/cpes"
    table.add_row(["Vuln Confs", vuln_conf_url])
    #References
    tmp_str = ''
    for i in range(len(ref)):
        tmp_str += ( '[' + str(i).zfill(3) + ']: '
                     + 'url: ' + str(ref[i][0]) + '\n'
                     + '       name: ' + str(ref[i][1]) + '\n'
                     + '       Reference Source: ' + str(ref[i][2]) + '\n'
                     + '       Tags: ' + str(ref[i][3]) + '\n'
                    )
    table.add_row(["References: ", tmp_str])
    return table

def search_table(l):
    table = PrettyTable(['CVE', 'CVSS', 'Summary', 'Published', 'Updated'])
    table.align = "l"
    for d in l:
        id_ = (d['cve']['CVE_data_meta']['ID'])
        description = (d['cve']['description']['description_data'][0]['value'])
        description = insert_newlines(description, 64)
        if "baseMetricV3" in d['impact']:
            cvss = (d['impact']['baseMetricV3']['cvssV3']['baseScore'])
        else:
            cvss = 'NA'
        up_date = (d['lastModifiedDate'])
        pub_date = (d['publishedDate'])
        table.add_row([id_, cvss, description, pub_date[:10], up_date[:10]])
    return table
