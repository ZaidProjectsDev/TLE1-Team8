import os
import time
import pyautogui
import keyboard
import win32gui
import win32con


def get_active_window_title():
    # Get the handle of the active window
    hwnd = win32gui.GetForegroundWindow()

    # Get the window title
    window_title = win32gui.GetWindowText(hwnd)

    # Remove invalid characters from the title to use as a folder name
    folder_name = "".join(c for c in window_title if c.isalnum() or c in [' ', '_'])

    return folder_name.strip()


def capture_screen(interval=2, num_captures=999):
    try:
        # Main capture loop
        for i in range(1, num_captures + 1):
            # Get the current active window title as the folder name
            folder_name = get_active_window_title()

            # Create the folder if it doesn't exist
            folder_path = os.path.join(os.getcwd(), folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Capture the screen
            screenshot = pyautogui.screenshot()

            # Generate the filename
            filename = f"{folder_name}_{i:03d}.png"
            file_path = os.path.join(folder_path, filename)

            # Save the screenshot
            screenshot.save(file_path)
            print(f"Saved {filename}")

            # Wait for the specified interval
            time.sleep(interval)
    except KeyboardInterrupt:
        pass


def main():
    # Set the hotkey
    hotkey = "ctrl+alt+c"

    # Register the hotkey
    keyboard.add_hotkey(hotkey, capture_screen)

    print(f"Press {hotkey} to start capturing. Press Ctrl+C to stop.")

    try:
        # Keep the script running
        keyboard.wait("ctrl+c")
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
