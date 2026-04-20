from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from config import KEY

def decrypt_log_file(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    
    iv = data[:16]
    ct = data[16:]

    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(ct), AES.block_size)
    return decrypted.decode()

# Example usage
if __name__ == "__main__":
    file_to_decrypt = input("Enter path to .bin file: ")
    try:
        output = decrypt_log_file(file_to_decrypt)
        print("\nDecrypted Log:\n" + "-"*50)
        print(output)
    except Exception as e:
        print("Error:", e)
