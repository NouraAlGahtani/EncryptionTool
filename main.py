def caesar_cipher_enc(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
        # shift the character by the given amount
         shifted_char = chr((ord(char)- 65 + shift)%26 + 65)
         ciphertext += shifted_char
        else:
            #Leave  non alphabetic char unchanged 
         ciphertext += char
        return ciphertext