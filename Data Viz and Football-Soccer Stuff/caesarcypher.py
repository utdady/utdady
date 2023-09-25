def encrypt(text,s):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

def decrypt(text):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    translated = text
    solutions = dict()
    for key in range(len(LETTERS)):
        solutions[str(key)] = translated
        translated = ''
        for symbol in text:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num -= key
                if num < 0:
                    num += len(LETTERS)
                translated += LETTERS[num]
            else:
                translated += symbol
    return solutions

text = input("Plain Text: ")
num = int(input("Shift pattern: "))
ciphered = encrypt(text,num).upper()
print(f"Cipher Text: {ciphered}")

print(decrypt(ciphered))
