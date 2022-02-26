__author__ = "Arthur Tressuol"
__email__ = "arthur.tressuol@gmail.com"
__credits__ = "Arthur Tressuol"
__date__ = "February 2022"
__revision__ = "1.0"

import update
import stats
import last
import recent
import cve
import search
import twitter
import exploitdb
import github
import reddit
import youtube

def banner():
    print("        ___                           _  _____   _____ ")
    print("       | _ \___ _ _ ___ ___ _ _  __ _| |/ __\ \ / / __|")     
    print("       |  _/ -_) '_(_-</ _ \ ' \/ _` | | (__ \ V /| _| ")
    print("       |_| \___|_| /__/\___/_||_\__,_|_|\___| \_/ |___|")
    print("\n")

def stats_print():
    print("-------------------------------------------------------------")
    print("                          CVE Stats                          ")
    print("-------------------------------------------------------------")
    try:
        with open('../data/stats.dat') as f:
            lines = f.readlines()
            for l in lines:
                print(l[:-1])
    except IOError:
        print("No stats to print out, use the stats option to generate reports")
    print('\n\n')

def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            print('\n\n')
            return True
        if reply[0] == 'n':
            print('\n\n')
            return False

def helper():
    print("-------------------------------------------------------------")
    print("Usage: Option [Arguments]")
    print("-------------------------------------------------------------")
    print("Options and Arguments:")
    print("\tq, quit    - Quit the script")
    print("\th, help    - Print this helper")
    print("\tu, update  - Update the CVE database")
    print("\ta, stats   - Traverse the database and prints out stats")
    print("\tl, last    - Print last CVE modifications")
    print("\tr, recent  - Print recent CVE entries")
    print("\tc, cve     - Search for specific CVE id\n\t\t\tArgument: cve-id")
    print("\ts, search  - Search for arguments in CVE descriptions\n\t\t\tArguments: arg1 arg2 ...")
    print("\te, exploit - Search for specific CVE id on ExploitDB\n\t\t\tArgument: cve-id")
    print("\tt, twitter - Search for arguments on Twitter\n\t\t\tArguments: arg1 arg2 ...")
    print("\tg, github  - Search for arguments on GitHub\n\t\t\tArguments: arg1 arg2 ...")
    print("\td, reddit  - Search for arguments on Reddit\n\t\t\tArguments: arg1 arg2 ...")
    print("\ty, youtube - Search for arguments on YouTube\n\t\t\tArguments: arg1 arg2 ...")
    print("-------------------------------------------------------------")
    print('\n')

def menuChoice():
    valid = ['quit',     'q',
             'help',     'h',   'helper',
             'update',   'u',
             'stats',    'a',
             'last',     'l',
             'recent',   'r',
             'cve',      'c',
             'search',   's',
             'twitter',  't',
             'exploitDB','e',   'exploitdb',    'exploit',
             'github',   'g',
             'reddit',   'd',
             'youtube',  'y'
            ]
    reply = str(input('Command: ')).lower().strip().split(' ')
    if reply[0] in valid:
        process(reply)
        print('\n')
    else:
        print('Invalid Option')
        menuChoice()

def process(reply):
    #Check arguments
    args = ''
    if len(reply) > 2:
        args = reply.copy()
        args.pop(0)
    elif len(reply) > 1:
        args = reply[1]
    #Check command
    if reply[0] == "quit" or reply[0] == "q":
        quit()
    if reply[0] == "help" or reply[0] == "h" or reply[0] == "helper":
        helper()
    if reply[0] == "update" or reply[0] == "u":
        update.update()
    if reply[0] == "stats" or reply[0] == "a":
        stats.stats()
    if reply[0] == "last" or reply[0] == "l":
        last.last(args)
    if reply[0] == "recent" or reply[0] == "r":
        recent.recent(args)
    if reply[0] == "cve" or reply[0] == "c":
        cve.cve(args)
    if reply[0] == "search" or reply[0] == "s":
        search.search(args)
    if reply[0] == "twitter" or reply[0] == "t":
        twitter.twitter(args)
    if reply[0] == "exploitDB" or reply[0] == "exploitdb" or reply[0] == "exploit" or reply[0] == "e":
        exploitdb.exploitdb(args)
    if reply[0] == "github" or reply[0] == "git" or reply[0] == "g":
        github.github(args)
    if reply[0] == "reddit" or reply[0] == "d":
        reddit.reddit(args)
    if reply[0] == "youtube" or reply[0] == "y":
        youtube.youtube(args)

def main():
    banner()
    stats_print()
    #Update Database?
    if yes_or_no("Do you want to update the Database?"):
        update.update()
    #Print Commands
    helper()
    #Answer requests
    while 1:
        menuChoice()

if __name__ == "__main__":
    main()
