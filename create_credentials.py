# Netflix Partner Report Credential Generator
# Gregg Brown - gregg.brown@sky.uk

from cryptography.fernet import Fernet
from getpass import getpass
from json import dumps
from os.path import exists

def CreateNetflixCredentialsFile(credFile):
    # Get login details from user
    email = input('Please enter your email address: ')
    while True:
        passw = getpass('Please enter your password: ')
        if getpass('Confirm password: ') != passw:
            print("Passwords don't match - try again")
        else:
            break
    
    # Create dict to hold details
    credentials = {'Netflix':{'email':f'{email}','password':f'{passw}'}}

    # Create encryption keyfile, if one doesn't already exist
    fk = 'filekey.key'
    if exists(fk):
        with open(fk, 'rb') as keyFile:
            key = keyFile.read()
    else:
        key = Fernet.generate_key()
        with open(fk, 'wb') as keyFile:
            keyFile.write(key)
    fernet = Fernet(key)

    # Encrypt and write login credentials to file
    with open(credFile, 'wb') as outFile:
        outFile.write(fernet.encrypt(dumps(credentials).encode('utf-8')))

if __name__ == '__main__':
    # Only seen if script is run directly, to create or overwrite credentials file
    credFile = 'credentials.enc'
    title = '+ NetFlix Credentials File Creator +'
    decoration = '+'*len(title)
    print(f'{decoration}\n{title}\n{decoration}\n')

    print(f'You are about to {"overwrite" if exists(credFile) else "create"} a credentials file to store Netflix partner Login details.\nPress CTRL+C at any time to cancel.\n')

    CreateNetflixCredentialsFile(credFile)