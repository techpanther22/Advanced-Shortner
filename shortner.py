#!/usr/bin/python3
# techpather
# [+]  Youtube  :  youtube.com/techpanther     [+]
# [+]  Instagram:  instagram.com/techpanther   [+]
# [+]  Facebook :  facebook.com/techpanther22  [+]
# [+]  Blog     :  techpanther.in              [+]
# [+]  github   :  github.com/techpanther22    [+]

import os
import time
import pyshorteners
from time import sleep

os.system('clear')

def Main():

    print("\033[1;31;40m ___  _               _                  ")
    print("/ __>| |_  ___  _ _ _| |_ ._ _  ___  _ _ ")
    print("\__ \| . |/ . \| '_> | |  | ' |/ ._>| '_>")
    print("<___/|_|_|\___/|_|   |_|  |_|_|\___.|_|  \033[0m")
    print("\033[1;32;40m                      [v1.0] @techpanther")
    print("\033[1;34;40m[Generate Hidden URL for Social Engineering]")
    print("--------------------------------------------")
    print("\n\033[1;36;40m[01]  Google")
    print("[02]  Youtube")
    print("[03]  Instagram")
    print("[04]  Facebook")
    print("[05]  Personalized")
    print("\n[00]  Exit")
    Selector()


def Selector():
    select = int(input("\n\033[1;33;40mAdvanced-Shortner >>> "))
    if select == 1:
        EnlaceGoogle()
    elif select == 2:
        EnlaceYoutube()
    elif select == 3:
        EnlaceInstagram()
    elif select == 4:
        EnlaceFacebook()
    elif select == 5:
        EnlacePersonalized()
    elif select == 00:
        os.system('clear')
        print("Exiting...")
        sleep(1)
        os.system('clear')
        exit()
    else:
        os.system('clear')
        print("Please Select a Valid option...")
        sleep(1)
        os.system('clear')
        Main()


def EnlaceGoogle():
    os.system('clear')
    print("You have selected Google.")
    OriginalLink = str(input("\nOriginal URL: "))

    print("\nInput something Like: this-is-an-amazing-content-you-should-see")
    Postlink = str(input("\nPost LINK: "))
    os.system('clear')
    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.chilpit.short(OriginalLink)
    Withouthttp = EndLink[7:]
    print(f"\033[1;32;40m\nYour link is: https://www.google.com-{Postlink}@{Withouthttp}")
    Other()

def EnlaceYoutube():
    os.system('clear')
    print("You have selected Youtube.")
    OriginalLink = str(input("\nOriginal URL: "))

    print("\nInput something that: this-is-an-amazing-video-your-should-watch")
    Postlink = str(input("\nPost LINK: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.chilpit.short(OriginalLink)
    Withouthttp = EndLink[7:]
    os.system('clear')
    print(f"\033[1;32;40m\nYour link is: https://www.youtube.com-video-{Postlink}@{Withouthttp}")

    Other()


def EnlaceInstagram():
    os.system('clear')
    print("You have selected Instagram.")
    OriginalLink = str(input("\nOriginal URL: "))

    print("\nInput something that: this-is-an-amazing-photo-your-should-see")
    Postlink = str(input("\nPost LINK: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.chilpit.short(OriginalLink)
    Withouthttp = EndLink[7:]
    os.system('clear')
    print(f"\033[1;32;40m\nYour link is: https://www.instagram.com-photo-{Postlink}@{Withouthttp}")

    Other()

def EnlaceFacebook():
    os.system('clear')
    print("You have selected Facebook.")
    OriginalLink = str(input("\nOriginal URL: "))

    print("\nInput something that: this-is-an-amazing-post-your-should-see")
    Postlink = str(input("\nPost LINK: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.chilpit.short(OriginalLink)
    Withouthttp = EndLink[7:]
    os.system('clear')
    print(f"\033[1;32;40m\nYour link is: https://www.facebook.com-profile-{Postlink}@{Withouthttp}")
    Other()

def EnlacePersonalized():
    os.system('clear')
    print("You have selected Personalized.")
    Domain = str(input("Example.com/es... input domain: "))
    OriginalLink = str(input("\nOriginal URL: "))

    print("\nInput something that: this-is-an-amazing-content-your-should-watch")
    Postlink = str(input("\nPost LINK: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.chilpit.short(OriginalLink)
    Withouthttp = EndLink[7:]
    os.system('clear')
    print(f"\033[1;32;40m\nYour link is: https://www.{Domain}-{Postlink}@{Withouthttp}")

    Other()

def Other():
    print("\033[93m\nDo you want to create another link?")
    print("Yes [01] \nNo  [02]")
    select=int(input("\nSelect a option: "))
    if select == 1:
        os.system('clear')
        Main()
    else:
        os.system('clear')
        exit()

#SYSCALL

Main()
