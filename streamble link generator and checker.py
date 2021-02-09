import requests
import random
import time

def randomString(stringLength):
    return ''.join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for i in range(stringLength))

baselink = 'https://streamable.com/'

def generateLink(numofchar):
    return baselink + randomString(numofchar)

def checkLink():
    link_to_test = generateLink(6)
    sendrequest = requests.get(link_to_test)
    if (sendrequest.status_code == 200):
        print(f'working link found : {link_to_test}')
    elif (sendrequest.status_code == 404):
        time.sleep(.55) #so streamble doesn't limit you until I add proxy support
    elif (sendrequest.status_code == 429):
        print("sending requests too quick")
    else:
        print(sendrequest.status_code)

def main():
    print("program is running")
    while (1 == 1):
        checkLink()

main()