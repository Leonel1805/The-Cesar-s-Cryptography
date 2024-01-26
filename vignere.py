def encrypt_vigenere(message, key):
    encrypted_message = ''
    key = key.upper()
    key_index = 0

    for char in message:
        if char.isalpha():
            if char.isupper():
                encrypted_message += chr((ord(char) + ord(key[key_index]) - 2 * 65) % 26 + 65)
            else:
                encrypted_message += chr((ord(char) + ord(key[key_index]) - 2 * 97) % 26 + 97)
            key_index = (key_index + 1) % len(key)
        else:
            encrypted_message += char

    return encrypted_message

def decrypt_vigenere(encrypted_message, key):
    decrypted_message = ''
    key = key.upper()
    key_index = 0

    for char in encrypted_message:
        if char.isalpha():
            if char.isupper():
                decrypted_message += chr((ord(char) - ord(key[key_index]) + 26) % 26 + 65)
            else:
                decrypted_message += chr((ord(char) - ord(key[key_index]) + 26) % 26 + 97)
            key_index = (key_index + 1) % len(key)
        else:
            decrypted_message += char

    return decrypted_message

def main():
    option = input("Seleccione una opción:\n1) Encriptar palabra\n2) Desencriptar palabra\n")

    if option == '1':
        message = input("Ingrese el mensaje a encriptar (solo letras, sin espacios): ").upper()
        key = input("Ingrese la palabra clave: ").upper()

        encrypted_result = encrypt_vigenere(message, key)
        print(f"Mensaje cifrado: {encrypted_result}")

    elif option == '2':
        encrypted_message = input("Ingrese el mensaje a desencriptar (solo letras, sin espacios): ").upper()
        key = input("Ingrese la palabra clave: ").upper()

        decrypted_result = decrypt_vigenere(encrypted_message, key)
        print(f"Mensaje descifrado: {decrypted_result}")

if __name__ == "__main__":
    main()
