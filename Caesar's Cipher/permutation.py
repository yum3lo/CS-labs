alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def generate_permuted_alphabet(key2):
  # remove duplicates and convert to uppercase
  unique_key = ''.join(dict.fromkeys(key2.upper()))
  permuted_alphabet = unique_key + ''.join(char for char in alphabet if char not in unique_key)
  return permuted_alphabet

def enhanced_caesar_cipher(text, key1, key2, mode):
  permuted_alphabet = generate_permuted_alphabet(key2)
  result = ''
  for char in text:
    if char in permuted_alphabet:
      index = permuted_alphabet.index(char)
      if mode == 'encrypt':
        new_index = (index + key1) % 26
      else:
        new_index = (index - key1) % 26
      result += permuted_alphabet[new_index]
  return result

def get_valid_numeric_key():
  while True:
    try:
      key = int(input("Enter the first key (1-25): "))
      if 1 <= key <= 25:
        return key
      else:
        print("Key must be between 1 and 25.")
    except ValueError:
      print("Enter an integer value.")

def get_valid_alphabetic_key():
  while True:
    key = input("Enter the second key (at least 7 letters, A-Z only): ").upper()
    if len(key) >= 7 and all(char in alphabet for char in key):
      return key
    else:
      print("Key must be at least 7 letters long and contain only A-Z.")

def get_valid_text():
  while True:
    text = input("Enter the message (A-Z only): ").upper().replace(" ", "")
    if all(char in alphabet for char in text):
      return text
    else:
      print("Use only letters A-Z.")

def main():
  print("Enhanced Caesar Cipher with Two Keys")
  while True:
    mode = input("Choose operation (encrypt/decrypt) or 'quit' to exit: ").lower()
    if mode == 'quit':
      break
    if mode not in ['encrypt', 'decrypt']:
      print("Invalid operation. Choose 'encrypt' or 'decrypt'.")
      continue

    key1 = get_valid_numeric_key()
    key2 = get_valid_alphabetic_key()
    text = get_valid_text()

    if mode == 'encrypt':
      result = enhanced_caesar_cipher(text, key1, key2, 'encrypt')
      print(f"Encrypted message: {result}")
    else:
      result = enhanced_caesar_cipher(text, key1, key2, 'decrypt')
      print(f"Decrypted message: {result}")

if __name__ == "__main__":
  main()