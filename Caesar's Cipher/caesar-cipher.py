alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caesar_cipher(text, key, mode):
  result = ''
  for char in text:
    if char in alphabet:
      index = alphabet.index(char)
      if mode == 'encrypt':
        new_index = (index + key) % 26
      else:
        new_index = (index - key) % 26
      result += alphabet[new_index]
  return result

def get_valid_key():
  while True:
    try:
      key = int(input("Enter the key (1-25): "))
      if 1 <= key <= 25:
        return key
      else:
        print("Key must be between 1 and 25.")
    except ValueError:
      print("Enter an integer value.")

def get_valid_text():
  while True:
    text = input("Enter the message (use only A-Z, a-z): ").upper().replace(" ", "")
    if all(char in alphabet for char in text):
      return text
    else:
      print("Only use letters A-Z or a-z.")

def main():
  print("Caesar Cipher:")
  while True:
    mode = input("Choose operation (encrypt/decrypt) or 'quit' to exit: ").lower()
    if mode == 'quit':
      break
    if mode not in ['encrypt', 'decrypt']:
      print("Invalid operation. Choose 'encrypt' or 'decrypt'.")
      continue

    key = get_valid_key()
    text = get_valid_text()

    if mode == 'encrypt':
      result = caesar_cipher(text, key, 'encrypt')
      print(f"Encrypted message: {result}")
    else:
      result = caesar_cipher(text, key, 'decrypt')
      print(f"Decrypted message: {result}")

if __name__ == "__main__":
  main()