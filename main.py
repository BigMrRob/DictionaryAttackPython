"""
Note: MD5 is currently outdated.
Much better algortihms such as SHA-256 are used. This is just an example project displaying a basic dictionary attack.
A quality password cracker would use SHA-256 and a much larger file for the dictionary list.
"""
import hashlib

flag = 0

pass_hash = input("Enter md5 hash: (There are three example hashes for use in the md5.txt file) ")

wordlist = input("File name: (You can add a larger, more comprehensive passlist found online. Enter passlist.txt to use 234k possible passwords) ")

try:
    pass_file = open(wordlist, "r")
except:
    print("No file found")
    quit()

for word in pass_file:
    encoded_word = word.encode('utf-8')
    digest = hashlib.md5(encoded_word.strip()).hexdigest()

    print(word)
    print(digest)
    print(pass_hash)

    if digest == pass_hash:
        print("Password has been cracked")
        print("Password is " + word)
        flag = 1
        break

if flag == 0:
    print("Password is not in the list")
