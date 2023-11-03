def generate_playfair_matrix(key):
    key = key.replace(" ", "").upper()
    key = key.replace("J", "I")  # Replace 'J' with 'I'
    key += "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    matrix = []
    for i in range(5):
        row = key[i * 5 : (i + 1) * 5]
        matrix.append(row)

    return matrix


def find_position(matrix, letter):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letter:
                return i, j

    return -1, -1


def decrypt_playfair(ciphertext, key):
    matrix = generate_playfair_matrix(key)
    plaintext = ""

    # Ensure that the length of the ciphertext is even
    if len(ciphertext) % 2 != 0:
        ciphertext += 'X'

    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:  # Same row
            col1 = (col1 - 1) % 5
            col2 = (col2 - 1) % 5
        elif col1 == col2:  # Same column
            row1 = (row1 - 1) % 5
            row2 = (row2 - 1) % 5
        else:  # Rectangle rule
            col1, col2 = col2, col1

        plaintext += matrix[row1][col1] + matrix[row2][col2]

    return plaintext


# Main program
ciphertext = input("Enter the ciphertext: ")
key = input("Enter the key: ")

plaintext = decrypt_playfair(ciphertext, key)
print("Plaintext:", plaintext)
