from mainFunctions import *
import users

def main():
    choice = -1
    userList = users.users()
    option = [login,register]
    while(choice!="3"):
        try:
            print(logo)
            choice = input()
            option[int(choice) - 1](userList)
        except:
            choice = '3'


    return None

if(__name__ == "__main__"):
    main()
