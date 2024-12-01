def create_matrix(key):
  alphabet = 'AĂÂBCDEFGHIÎKLMNOPQRSȘTȚUVWXYZ'
  key = key.upper().replace('J', 'I')
  key = ''.join(dict.fromkeys(key))

  matrix_content = key
  for letter in alphabet:
    if letter not in matrix_content:
      matrix_content += letter

  matrix = []
  for i in range(0, 30, 6):
    matrix.append(list(matrix_content[i:i+6]))

  return matrix

def find_position(matrix, letter):
  letter = 'I' if letter == 'J' else letter
  for i in range(5):
    for j in range(6):
      if matrix[i][j] == letter:
        return i, j
  return -1, -1

def prepare_text(text):
  text = ''.join(text.upper().split()).replace('J', 'I')
  pairs = []
  i = 0
  while i < len(text):
    if i + 1 >= len(text):
      pairs.append((text[i], 'X'))
      i += 1
    elif text[i] == text[i+1]:
      pairs.append((text[i], 'X'))
      i += 1
    else:
      pairs.append((text[i], text[i+1]))
      i += 2
  return pairs

def encrypt_pair(matrix, pair):
  row1, col1 = find_position(matrix, pair[0])
  row2, col2 = find_position(matrix, pair[1])

  if row1 == row2:
    return matrix[row1][(col1 + 1) % 6] + matrix[row2][(col2 + 1) % 6]
  elif col1 == col2:
    return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
  else:
    return matrix[row1][col2] + matrix[row2][col1]

def decrypt_pair(matrix, pair):
  row1, col1 = find_position(matrix, pair[0])
  row2, col2 = find_position(matrix, pair[1])

  if row1 == row2:
    return matrix[row1][(col1 - 1) % 6] + matrix[row2][(col2 - 1) % 6]
  elif col1 == col2:
    return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
  else:
    return matrix[row1][col2] + matrix[row2][col1]

def playfair_cipher(key, text, mode='encrypt'):
  if len(key) < 7:
    raise ValueError('Key must have at least 7 characters')

  matrix = create_matrix(key)
  pairs = prepare_text(text)
  result = []
  for pair in pairs:
    if mode == 'encrypt':
      result.append(encrypt_pair(matrix, pair))
    else:
      result.append(decrypt_pair(matrix, pair))

  return ''.join(result)

def print_matrix(matrix):
  print('\nPlayfair matrix:')
  for row in matrix:
    print(' '.join(row))
  print()

def main():
  while True:
    print('1. Encrypt')
    print('2. Decrypt')
    print('3. View matrix')
    print('4. Exit')

    choice = input('Enter your choice: ')

    if choice == '4':
      break

    if choice == '3':
      key = input('Enter key: ')
      if len(key) < 7:
        print('Key must have at least 7 characters')
        continue
      matrix = create_matrix(key)
      print_matrix(matrix)
      continue

    key = input('Enter key: ')
    if len(key) < 7:
      print('Key must have at least 7 characters')
      continue

    text = input('Enter text: ')

    try:
      if choice == '1':
        print('Encrypted text:', playfair_cipher(key, text, 'encrypt'))
      elif choice == '2':
        print('Decrypted text:', playfair_cipher(key, text, 'decrypt'))
    except ValueError as e:
      print(e)

if __name__ == '__main__':
  main()