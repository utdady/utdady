# assignment: programming assignment 4
# author: (Aditya Bhaskar)
# date: (2nd December 2020)
# file: cipher.py is a program that encrypts and decrypts strings by shifting the alphabet based on the user's choice.
# input: (file)
# output: (encrypted/decrypted text)
def make_alphabet():
    alphabet=()
    for i in range(26):
        char=i+65
        alphabet+=(chr(char),)
    return alphabet

def encode(rfilename, wfilename):
    try:
        fr=open(rfilename, "r")
    except FileNotFoundError:
        print("\nFILE Not FOUND!\n")
    else:
        fr.seek(0,0)
        plaintext=fr.read()
        fr.close()
        print(f"\nPlaintext:\n\n{plaintext}")
        plaintext=plaintext.upper()
        shift=3
        ciphertext=[]
        alphabet=make_alphabet()
        length=len(alphabet)
        for char in plaintext:
            found=False
            for i in range(length):
                if char==alphabet[i]:
                    letter=alphabet[(i+shift)%length]
                    ciphertext.append(letter)
                    found=True
                    break
            if not found:
                ciphertext.append(char)
        c=to_string(ciphertext)
        fw=open(wfilename, "w+")
        fw.write(c)
        print(f"\nCiphertext:\n\n{c}\n")

def decode(rfilename, wfilename):
    try:
        fr=open(rfilename, "r")
    except FileNotFoundError:
        print("\nFILE Not FOUND!\n")
    else:
        fr.seek(0,0)
        ciphertext=fr.read()
        fr.close()
        print(f"\nCiphertext:\n\n{ciphertext}")
        ciphertext=ciphertext.upper()
        shift=-3
        plaintext=[]
        alphabet=make_alphabet()
        length=len(alphabet)
        for char in ciphertext:
            found=False
            for i in range(length):
                if char==alphabet[i]:
                    letter=alphabet[(i+shift)%length]
                    plaintext.append(letter)
                    found=True
                    break
            if not found:
                plaintext.append(char)
        p=to_string(plaintext)
        fw=open(wfilename, "w+")
        fw.write(p)
        print(f"\nPlaintext:\n\n{p}\n")

def to_string(text):
    s=""
    for char in text:
        s+=char
    return s

done=False
while not done:
    print("Would you like to encode or decode the message?")
    io=input("Type E to encode, D to decode, or Q to quit: ")
    
    if io=='E' or io=='e':
        readfil=input("\nPlease enter a file for reading: ")
        writefil=input("Please enter a file for writing: ")
        encode(readfil,writefil)
        done=False
    elif io=='D' or io=='d':
        readfil=input("\nPlease enter a file for reading: ")
        writefil=input("Please enter a file for writing: ")
        decode(readfil,writefil)
        done=False
    elif io=='Q' or io=='q':
        done=True
        print("\nGoodbye!")
    else:
        print("\nWrong Input! Please try again.\n")
        done=False
