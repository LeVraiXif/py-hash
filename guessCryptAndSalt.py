#!/usr/bin/python3

import crypt
from termcolor import colored

mycryptWord = crypt.crypt("testtest", "HI")

print(mycryptWord)

def main():
    filename = input("Enter the name of the file containing the usernames and hashes: ")
    passFile = open(filename, 'r')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptWord = line.split(':')[1].strip('.........’')
            crackPass(cryptWord)

def crackPass(cryptWord):
    salt = cryptWord[0:2]
    filename = input("Enter the name of the dictionary file: ")
    dictionary = open(filename, 'r')
    for word in dictionary.readlines():
        word = word.strip('\n')
        cryptPass = crypt.crypt(word, salt)
        if (cryptWord == cryptPass):
            print(colored("[+] Found Password: " + word, 'red'))
            return

if __name__ == "__main__":
    main()
