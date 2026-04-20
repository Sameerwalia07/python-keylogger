
import pyperclip

def get_clipboard_data():
    try:
        return pyperclip.paste()
    except Exception as e:
        return f"Clipboard error: {e}"
