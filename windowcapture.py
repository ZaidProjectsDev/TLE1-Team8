
import numpy as np
import win32gui, win32ui, win32con
from ctypes import windll
class WindowCapture:
    w=0
    h=0
    hwnd = None
    cropped_x = 0
    cropped_y = 0
    offset_x = 0
    offset_y =0
    
    def __init__(self, window_name=None):

        if window_name is None:
            self.hwnd = win32gui.GetDesktopWindow()
        else:
            self.hwnd = win32gui.FindWindow(None, window_name)
        if not self.hwnd:
            raise Exception('Couldnt find window:{}' .format(window_name) )
        window_rect = win32gui.GetWindowRect(self.hwnd)



        self.w = window_rect[2]-window_rect[0]
        self.h = window_rect[3]-window_rect[1]

        border_pixels = 8
        titlebar_pixels = 30
        self.w = self.w-(border_pixels*2)
        self.h = self.h-titlebar_pixels-border_pixels

        self.cropped_x = border_pixels
        self.cropped_y = titlebar_pixels

        self.offset_x = window_rect[0] + self.cropped_x
        self.offset_y = window_rect[1] + self.cropped_y

    def get_screenshot(self):

        bmpfilenamename = "out.bmp" #set this
        
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj=win32ui.CreateDCFromHandle(wDC)
        cDC=dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0,0),(self.w, self.h) , dcObj, (self.cropped_x,self.cropped_y), win32con.SRCCOPY)
        #dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray,dtype='uint8')

        img.shape = (self.h,self.w,4)
        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())
        img = img[...,:3]
        img = np.ascontiguousarray(img)
        return img
    

        #function taken from stackoverflow : (https://stackoverflow.com/questions/76373625/pywin32-cannot-capture-certain-windows-giving-black-screen-python-windows)
    def capture_win_alt(self,window_name):
        # Adapted from https://stackoverflow.com/questions/19695214/screenshot-of-inactive-window-printwindow-win32gui

        windll.user32.SetProcessDPIAware()
        hwnd = win32gui.FindWindow(None, window_name)

        left, top, right, bottom = win32gui.GetClientRect(hwnd)
        w = right - left
        h = bottom - top

        hwnd_dc = win32gui.GetWindowDC(hwnd)
        mfc_dc = win32ui.CreateDCFromHandle(hwnd_dc)
        save_dc = mfc_dc.CreateCompatibleDC()
        bitmap = win32ui.CreateBitmap()
        bitmap.CreateCompatibleBitmap(mfc_dc, w, h)
        save_dc.SelectObject(bitmap)

        # If Special K is running, this number is 3. If not, 1
        result = windll.user32.PrintWindow(hwnd, save_dc.GetSafeHdc(), 3)

        bmpinfo = bitmap.GetInfo()
        bmpstr = bitmap.GetBitmapBits(True)

        img = np.frombuffer(bmpstr, dtype=np.uint8).reshape((bmpinfo["bmHeight"], bmpinfo["bmWidth"], 4))
        img = np.ascontiguousarray(img)[..., :-1]  # make image C_CONTIGUOUS and drop alpha channel

        if not result:  # result should be 1
            win32gui.DeleteObject(bitmap.GetHandle())
            save_dc.DeleteDC()
            mfc_dc.DeleteDC()
            win32gui.ReleaseDC(hwnd, hwnd_dc)
            raise RuntimeError(f"Unable to acquire screenshot! Result: {result}")

        return img
def get_screen_position(self, pos):
    return (pos[0] + self.offset_x, pos[1] + self.offset_y)



