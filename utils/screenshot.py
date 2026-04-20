
import pyautogui
from datetime import datetime
import os

def capture_screenshot():
    os.makedirs("logs", exist_ok=True)
    filename = f"logs/screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
