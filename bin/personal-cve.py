import os

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
    valid = ['quit', 'q',
             'help', 'h', 'helper',
             'last', 'l'
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
    if len(reply) > 1:
        args = reply[1]
    #Check command
    if reply[0] == "quit" or reply[0] == "q":
        quit()
    if reply[0] == "help" or reply[0] == "h" or reply[0] == "helper":
        helper()
    if reply[0] == "last" or reply[0] == "l":
        os.system("python3 ./02-last.py " + args)

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
        print("TODO")
    #Print Commands
    helper()
    #Answer requests
    while 1:
        menuChoice()

if __name__ == "__main__":
    main()
