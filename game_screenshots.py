import os
import time
import keyboard
import win32gui
import win32ui
import numpy as np
from PIL import Image
from ctypes import windll


def get_active_window_title():
    hwnd = win32gui.GetForegroundWindow()
    window_title = win32gui.GetWindowText(hwnd)
    folder_name = "".join(c for c in window_title if c.isalnum() or c in [' ', '_'])
    return folder_name.strip()


def capture_screen(interval=0.5, num_captures=999):
    try:
        for i in range(1, num_captures + 1):
            windll.user32.SetProcessDPIAware()
            hwnd = win32gui.GetForegroundWindow()
            left, top, right, bottom = win32gui.GetClientRect(hwnd)
            w = right - left
            h = bottom - top

            if w >= 320 and h >= 240:
                hwnd_dc = win32gui.GetWindowDC(hwnd)
                mfc_dc = win32ui.CreateDCFromHandle(hwnd_dc)
                save_dc = mfc_dc.CreateCompatibleDC()
                bitmap = win32ui.CreateBitmap()
                bitmap.CreateCompatibleBitmap(mfc_dc, w, h)
                save_dc.SelectObject(bitmap)

                # If Special K is running, this number is 3. If not, 1
                result =windll.user32.PrintWindow(hwnd, save_dc.GetSafeHdc(), 3)

                bmpinfo = bitmap.GetInfo()
                bmpstr = bitmap.GetBitmapBits(True)

                img = np.frombuffer(bmpstr, dtype='uint8').reshape((bmpinfo["bmHeight"], bmpinfo["bmWidth"], 4))
                img = np.ascontiguousarray(img)[..., :-1]
                # Convert to PIL Image and save

                # Get the current active window title as the application name
                application_name = get_active_window_title()

                # Create the folder structure
                base_folder = os.path.join(os.getcwd(), "training_captures", application_name)
                if not os.path.exists(base_folder):
                    os.makedirs(base_folder)

                # Generate the filename
                filename = f"{application_name}_{i:03d}.png"
                file_path = os.path.join(base_folder, filename)

                # Reorder the channels to RGB
                img_rgb = img[..., ::-1]

                # Save the unedited version
                pil_image_base = Image.fromarray(img_rgb)
                pil_image_base.save(file_path)
                print(f"Saved {filename}.png")

                # Save the rotated versions
                for angle in [90, 180, 270]:
                    filename_rotated = f"{application_name}_{i:03d}_r_{angle}.png"
                    file_path_rotated = os.path.join(base_folder, filename_rotated)
                    pil_image_rotated = pil_image_base.rotate(angle)
                    pil_image_rotated.save(file_path_rotated)
                    print(f"Saved {filename_rotated} (rotated {angle} degrees)")



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
        keyboard.wait("ctrl+alt+v")
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
