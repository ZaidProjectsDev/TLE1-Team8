import pygetwindow as gw
import psutil
import keyboard
import time

import windowdefinition
import win32gui

selected_window = None
def get_focused_window_info():
    focused_window = win32gui.GetForegroundWindow()
    print(focused_window)
    global selected_window
    if focused_window:
        window_name = win32gui.GetWindowText(focused_window)
        process_id = 000
        selected_window = focused_window
        return window_name, process_id
    else:
        return None

def arbitrary_function(shared_models):
    print(f"Selected window: {selected_window}")
    newWindow = windowdefinition.WindowDefinition(selected_window,win32gui.GetWindowText(selected_window))
    windowdefinition.update_active_window(newWindow)
    shared_models.initalizeVision()
    # Replace this function with your custom functionality
    print("Arbitrary function executed!")


def check_for_game_window(shared_models):
    # Check for key press events every 0.1 seconds
    if keyboard.is_pressed('Enter'):
        # Get focused window information
        window_info = get_focused_window_info()

        if window_info:
            window_name, process_id = window_info
            print(f"Focused Window Name: {window_name}")
            print(f"Process ID: {process_id}")

            # Execute arbitrary function
            arbitrary_function(shared_models)
        else:
            print("No focused window found.")

        # Pause for a short time to avoid repeated key presses
        time.sleep(0.5)
