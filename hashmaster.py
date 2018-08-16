#import
import hashlib

#banner
print('''.__                  .__                             __                
|  |__ _____    _____|  |__   _____ _____    _______/  |_  ___________ 
|  |  \\\\__  \\  /  ___/  |  \\ /     \\\\__  \\  /  ___/\\   __\\/ __ \\_  __ \\
|   Y  \\/ __ \\_\\___ \\|   Y  \\  Y Y  \\/ __ \\_\\___ \\  |  | \\  ___/|  | \\/
|___|  (____  /____  >___|  /__|_|  (____  /____  > |__|  \___  >__|   
     \\/     \\/     \\/     \\/      \\/     \\/     \\/            \\/ ''')

#inputs
wlist=input("wordlist: ")
hash2crack=input("hash: ")

#read file
wlistlines=open(wlist, "r").readlines()

#loop
for i in range(0, len(wlistlines)):
    hash2comp=hashlib.md5(wlistlines[i].replace("\n","").encode()).hexdigest()
    if hash2crack == hash2comp:
        print("password found: "+wlistlines[i].replace("\n",""))
        exit()
print("password not found")
