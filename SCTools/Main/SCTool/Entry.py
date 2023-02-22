# ##### Entry Point to SCHub

import win32gui
import win32con
from SCToolHUB_V2 import App_HUB

if __name__ == '__main__':
    print("SCToolHub - 0.0.1 ")
    print("Build : Wed 22 Feb 2023 ")

    # Find the console window and minimize it
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

    # Start the main application
    App_HUB().mainloop()
