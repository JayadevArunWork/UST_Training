#9.Secure File "Vault" with Audit Logs
import os, getpass, logging
from cryptography.fernet import Fernet, InvalidToken

logging.basicConfig(filename="audit.log",level=logging.INFO,format="%(asctime)s | %(message)s")

def log(event):
    logging.info(event)

def get_key_from_password(password):
    return Fernet.generate_key()[:32]

def encrypt_file(path, fernet):
    data = open(path, "rb").read()
    enc = fernet.encrypt(data)
    open(path + ".enc", "wb").write(enc)
    os.remove(path)

def decrypt_file(path, fernet):
    data = open(path, "rb").read()
    dec = fernet.decrypt(data)
    new = path.replace(".enc", "")
    open(new, "wb").write(dec)
    os.remove(path)

def main():
    print("Need? 1) encrypt  2) decrypt")
    choice = input("Enter choice: ")

    password = getpass.getpass("Master password: ")
    key = get_key_from_password(password)
    f = Fernet(key)

    try:
        if choice == "1":
            encrypt_file("secret.txt", f)
            print("Encrypted.")
            log("encrypt success")
        elif choice == "2":
            decrypt_file("secret.txt.enc", f)
            print("Decrypted.")
            log("decrypt success")
        else:
            print("Invalid Choice.")
            log("invalid")
    except InvalidToken:
        print("Wrong password.")
        log("decrypt failure")
    except Exception as e:
        print("Error.")
        log("error failure")

main()