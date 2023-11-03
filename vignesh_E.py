def vigenere_encrypt(plaintext, keyword):
    keyword = keyword.upper()
    encrypted_text = ""
    keyword_repeated = (keyword * (len(plaintext) // len(keyword))) + keyword[:len(plaintext) % len(keyword)]

    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()
            shift = ord(keyword_repeated[i]) - ord('A')
            char_code = ord(char) + shift

            if char_code > ord('Z'):
                char_code -= 26

            if is_upper:
                encrypted_text += chr(char_code)
            else:
                encrypted_text += chr(char_code).lower()
        else:
            encrypted_text += char

    return encrypted_text

plaintext = input("Enter the plaintext: ")
keyword = input("Enter the keyword: ")

encrypted_text = vigenere_encrypt(plaintext, keyword)
print("Encrypted text:", encrypted_text)
