#!/usr/bin/python3
import hashlib
from urllib.request import urlopen
from termcolor import colored

# Step 1: Get user input for SHA1 hash to crack
sha1hash = input("Donner la valeur de Sha1 hash pour essayer de le casser: ")

# Step 2: Open URL containing password list and read it into a variable
passwordList = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read(), 'utf-8')

# Step 6: Split password list into individual words
for i in passwordList.split('\n'):
    # Step 8: Hash each word and store it in a variable
    hashGuess = hashlib.sha1(bytes(i, 'utf-8')).hexdigest()

    # Step 9: Compare each hash with the user's input hash
    if hashGuess == sha1hash:
        print(colored("[+] Password est " + str(i), 'green'))
        quit()
    else:
        print(colored("[-] Essaie " + str(i) + " pas valable, le suivant...", "yellow"))

# Step 10: If no match is found, print a message saying the password is not in the list
print(colored("Password pas dans la liste", "red"))
