def generate_playfair_matrix(key):
    key = key.replace(" ", "").upper()
    key = key.replace("J", "I")  # Replace 'J' with 'I'
    key += "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    matrix = []
    for i in range(5):
        row = key[i * 5 : (i + 1) * 5]
        matrix.append(row)

    return matrix


def get_digraphs(plaintext):
    plaintext = plaintext.replace(" ", "").upper()
    digraphs = []
    i = 0
    while i < len(plaintext):
        if i == len(plaintext) - 1 or plaintext[i] == plaintext[i + 1]:
            digraphs.append(plaintext[i] + "X")
            i += 1
        else:
            digraphs.append(plaintext[i] + plaintext[i + 1])
            i += 2

    return digraphs


def find_position(matrix, letter):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letter:
                return i, j

    return -1, -1


def encrypt_playfair(plaintext, key):
    matrix = generate_playfair_matrix(key)
    digraphs = get_digraphs(plaintext)
    ciphertext = ""

    for digraph in digraphs:
        char1, char2 = digraph[0], digraph[1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:  # Same row
            col1 = (col1 + 1) % 5
            col2 = (col2 + 1) % 5
        elif col1 == col2:  # Same column
            row1 = (row1 + 1) % 5
            row2 = (row2 + 1) % 5
        else:  # Rectangle rule
            col1, col2 = col2, col1

        ciphertext += matrix[row1][col1] + matrix[row2][col2]

    return ciphertext


# Main program
plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")

ciphertext = encrypt_playfair(plaintext, key)
print("Ciphertext:", ciphertext)