from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

def generate_key(password, salt):
    """
    Generuje klucz na podstawie hasła i soli za pomocą algorytmu PBKDF2HMAC.
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=salt,
        length=32,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return key

def encrypt_file(input_file, output_file, key):
    """
    Szyfruje plik za pomocą klucza symetrycznego.
    """
    with open(input_file, 'rb') as file:
        plaintext = file.read()

    iv = os.urandom(16)  # Inicjalizacja wektorowa

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    with open(output_file, 'wb') as file:
        file.write(iv + ciphertext)

def decrypt_file(input_file, output_file, key):
    """
    Deszyfruje plik za pomocą klucza symetrycznego.
    """
    with open(input_file, 'rb') as file:
        data = file.read()

    iv = data[:16]  # Pobieranie wektora inicjalizacyjnego
    ciphertext = data[16:]

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    with open(output_file, 'wb') as file:
        file.write(plaintext)

def main():
    password = input("Podaj hasło do szyfrowania/odszyfrowania pliku: ")
    salt = os.urandom(16)  # Generowanie losowej soli

    key = generate_key(password, salt)

    input_file = input("Podaj nazwę pliku wejściowego: ")
    output_file = input("Podaj nazwę pliku wyjściowego: ")

    encrypt_file(input_file, output_file, key)
    print("Plik zaszyfrowano.")

    decrypt_file(output_file, "decrypted_" + input_file, key)
    print("Plik odszyfrowano.")

if __name__ == "__main__":
    main()

