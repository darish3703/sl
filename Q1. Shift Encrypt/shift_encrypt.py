def shift_e(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char) - ord('a')
            char_code = (char_code + shift) % 26
            char_code = (char_code + 26) % 26  # Ensure the result is within [0, 25]
            char_code += ord('a')
            if is_upper:
                char_code = chr(char_code).upper()
            else:
                char_code = chr(char_code)
            encrypted_text += char_code
        else:
            encrypted_text += char
    return encrypted_text

plaintext = input("Enter the text to encrypt: ")
shift = int(input("Enter the shift value (integer): "))

encrypted_text = shift_e(plaintext, shift)
print("Encrypted text:", encrypted_text)
