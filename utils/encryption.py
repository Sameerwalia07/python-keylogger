
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from config import KEY
from datetime import datetime

def encrypt_log(data):
    cipher = AES.new(KEY, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
    return cipher.iv + ct_bytes

def save_encrypted_log(encrypted_data):
    filename = f"logs/encrypted_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bin"
    with open(filename, "wb") as f:
        f.write(encrypted_data)
