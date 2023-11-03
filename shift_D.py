def shift_d(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char) - ord('a')
            char_code = (char_code - shift) % 26
            char_code = (char_code + 26) % 26  # Ensure the result is within [0, 25]
            char_code += ord('a')
            if is_upper:
                char_code = chr(char_code).upper()
            else:
                char_code = chr(char_code)
            decrypted_text += char_code
        else:
            decrypted_text += char
    return decrypted_text

encrypted_text = input("Enter the encrypted text: ")
shift = int(input("Enter the shift value (integer): "))

decrypted_text = shift_d(encrypted_text, shift)
print("Decrypted text:", decrypted_text)
