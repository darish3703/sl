def vigenere_decrypt(encrypted_text, keyword):
    keyword = keyword.upper()
    decrypted_text = ""
    keyword_repeated = (keyword * (len(encrypted_text) // len(keyword))) + keyword[:len(encrypted_text) % len(keyword)]

    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()
            shift = ord(keyword_repeated[i]) - ord('A')
            char_code = ord(char) - shift

            if char_code < ord('A'):
                char_code += 26

            if is_upper:
                decrypted_text += chr(char_code)
            else:
                decrypted_text += chr(char_code).lower()
        else:
            decrypted_text += char

    return decrypted_text

encrypted_text = input("Enter the encrypted text: ")
keyword = input("Enter the keyword: ")
decrypted_text = vigenere_decrypt(encrypted_text, keyword)
print("Decrypted text:", decrypted_text)
