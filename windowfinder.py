import psutil
import win32gui
import tkinter as tk
import windowdefinition
def is_game(title):
    # Add conditions to identify games based on the window title
    game_keywords = ['game', 'play', 'gaming', 'steam', 'epic', 'assasins', 'clank', 'evil', 'gta', 'grand', 'halo', ': source','mario', 'sonic','netflix', 'YouTube', 'Raider', 'dx11' , 'dx12', 'dx9',' dx10', 'vk', 'vulkan', 'gl', 'shipping', 'build', 'debug']
    return any(keyword in title.lower() for keyword in game_keywords)

def get_all_windows():
    windows = []

    def enum_windows_callback(hwnd, windows):
        title = win32gui.GetWindowText(hwnd)
        if title and is_game(title):  # Check if the window has a title and is a game
            windows.append((hwnd, title))

    win32gui.EnumWindows(enum_windows_callback, windows)
    return windows

def on_button_click(hwnd,root):
    # Do something with the selected window (hwnd)
    print(f"Selected window: {hwnd}")
    newWindow = windowdefinition.WindowDefinition(hwnd,win32gui.GetWindowText(hwnd))
    print(newWindow.pid, newWindow.title)
    windowdefinition.activeWindow = newWindow
    root.destroy()



def create_window_list(root, canvas):
    window_list = get_all_windows()

    label = tk.Label(canvas, text="Select a window:")
    label.grid(row=0, column=0, columnspan=2, pady=10)  # Adjust columnspan and pady as needed

    row_index = 1  # Start from the second row to leave space for the label

    for hwnd, window_title in window_list:
        button = tk.Button(root, text=window_title, command=lambda hwnd=hwnd: on_button_click(hwnd,root))
        button.grid(row=row_index, column=0, sticky="ew", pady=5)

        # Increase row_index for the next row
        row_index += 1

    root.mainloop()

# if __name__ == "__main__":
#     root = tk.Tk()
#     canv= tk.Canvas(root, width=400, height=300, bg="white")  # Set canvas background color
#     create_window_list(root,canv)
