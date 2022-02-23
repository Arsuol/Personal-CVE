import update
import last
import recent
import cve
import search
import twitter
import exploitdb
import github
import reddit
import youtube

def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False

def helper():
    print("This is the helper\nPossible commands = <3")
    print("TODO")

def menuChoice():
    valid = ['quit',     'q',
             'help',     'h',   'helper',
             'update',   'u',
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
    else:
        print('Invalid Option')
        helper()
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
    if reply[0] == "github" or reply[0] == "g":
        github.github(args)
    if reply[0] == "reddit" or reply[0] == "d":
        reddit.reddit(args)
    if reply[0] == "youtube" or reply[0] == "y":
        youtube.youtube(args)

def banner():
    print(" ___                           _  _____   _____ ")
    print("| _ \___ _ _ ___ ___ _ _  __ _| |/ __\ \ / / __|")
    print("|  _/ -_) '_(_-</ _ \ ' \/ _` | | (__ \ V /| _| ")
    print("|_| \___|_| /__/\___/_||_\__,_|_|\___| \_/ |___|")
    print("\n")

def main():
    banner()
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
