# # ###########SCToolHUB V2 - HalfbakedBaker & ChatGPT
# # ###################################################
# # ## Add GUI with tkinter Forced above all other windows 
# # ## Add frame " Frame A"
# # ## Add Buttons to frame  x N
# # ## add frame " Frame B"
# # ## add slider to frame - changes transparency of window
# # ## add button to frame - span full width of frame - button toggles window / frameless mode
# # ## Use Background color of "#1E1E1E" and font of font=("Arial", 10, "bold")

# ############################# Version A ###### 

# ######## HUB A 

#### Need to implement a keybind system for this similar to the Quick Chat "Ctrl T"

# Opens Websites in Python GUI & allows user to open python script(QuickChatV2)


import tkinter as tk
import subprocess
import webview
import multiprocessing as mp
import webbrowser
from tkinter import *

def openwebpage(Url):
    # Open website
    webview.create_window(Url, Url,on_top=True,frameless=False,draggable=True,resizable=True,easy_drag=True,zoomable=True)
    webview.start()
   
def openwebpage_process(Url):
    # Start a new process to open the webpage
    p = mp.Process(target=openwebpage, args=(Url,))
    p.start()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SCToolHub")
        self.is_borderless = False
        self.attributes('-topmost', 1) # Force window above all others
        self.attributes('-alpha', 1) # Set default transparency to 1
        self.create_widgets()

    def create_widgets(self):

######## SC Tool Tool Bar

        # Create a frame for the web buttons
        web_buttons = tk.Frame(self, bg="#2C2C2C")

        # Create a label for the frame
        label = tk.Label(web_buttons, text="SC Tools", fg="#FFFFFF", bg="#2C2C2C", font=("Arial", 12, "bold"))

        # Pack the label and web buttons frame
        label.pack(side="left", padx=10, pady=10)
        web_buttons.pack(side="top", fill="x")
        # Create and pack the open Quick Chat Tool button
        self.button0 = tk.Button(web_buttons, text="ChatTool", command=lambda: subprocess.Popen(["python", "SCQuickChat_V2.py"]), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button0.pack(side="left", padx=10, pady=10)
        # Create and pack the open SCTool button
        self.button1 = tk.Button(web_buttons, text="SCTool", command=lambda: subprocess.Popen(["python", "SCTool.py"]), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button1.pack(side="left", padx=10, pady=10)




        # Create and pack the open Website 1 button
        self.button2 = tk.Button(web_buttons, text="Spectrum", command=lambda: openwebpage_process(Url="https://robertsspaceindustries.com/spectrum"), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button2.pack(side="left", padx=10, pady=10)
        # Create and pack the other website buttons 
        self.button3 = tk.Button(web_buttons, text="erkul", command=lambda: openwebpage_process(Url="https://www.erkul.games"), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button3.pack(side="left", padx=10, pady=10)
        # Create and pack the other website buttons 
        self.button4 = tk.Button(web_buttons, text="Scodex", command=lambda:openwebpage_process(Url="https://scodex.garga.net"), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button4.pack(side="left", padx=10, pady=10)
        # Create and pack the other website buttons 
        self.button5 = tk.Button(web_buttons, text="SCTools", command=lambda:openwebpage_process(Url="https://starcitizen.tools"), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button5.pack(side="left", padx=10, pady=10)
        # Create and pack the other website buttons 
        self.button6 = tk.Button(web_buttons, text="Trade", command=lambda:openwebpage_process(Url="https://sc-trade.toolshome"), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button6.pack(side="left", padx=10, pady=10)
        # Create and pack the other website buttons 
        self.button7 = tk.Button(web_buttons, text="Google", command=lambda:openwebpage_process(Url="https://www.Google.com"), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button7.pack(side="left", padx=10, pady=10)
        # Create and pack the other website buttons 
        self.button8 = tk.Button(web_buttons, text="Example", command=lambda:openwebpage_process(Url="https://www.example.com"), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button8.pack(side="left", padx=10, pady=10)
        # Create and pack the other website buttons 
        self.button9 = tk.Button(web_buttons, text="Example", command=lambda:openwebpage_process(Url="https://www.example.com"), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button9.pack(side="left", padx=10, pady=10)
        # Create and pack the other website buttons 
        self.button10 = tk.Button(web_buttons, text="Example", command=lambda:openwebpage_process(Url="https://www.example.com"), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button10.pack(side="left", padx=10, pady=10)



        # Create a frame for the window settings
        window_settings = tk.LabelFrame(self, text="Window Settings")
        # Pack the frame to the top
        window_settings.pack(side="top", fill="x")
        # Create the window settings frame
        window_settings = tk.LabelFrame(self, text="Window Settings", bg="#2C2C2C", fg="white", font=("Arial", 12, ))
        # Button to toggle window mode
        self.mode_button = tk.Button(web_buttons, text="Borderless", command=self.toggle_mode, bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.mode_button.pack(side="top", fill="x", padx=1, pady=1)
        # Create and pack the transparency slider
        self.slider = tk.Scale(web_buttons, from_=0.2, to=1, resolution=0.1, orient="horizontal", label="Transparency", command=self.set_transparency, bg="#1E1E1E", fg="#FFFFFF", troughcolor="#565656", highlightbackground="#1E1E1E", bd=0, font=("Arial", 10, "bold"))
        self.slider.set(1) # Set slider value to 1 by default
        self.slider.pack(side="top", fill="x", padx=1, pady=1)
        # Pack the window settings frame
        window_settings.pack(side="top", fill="x", padx=1, pady=1)
        self.configure(background="#000000")

    def set_transparency(self, value): # Set transparanecy value 
        self.attributes('-alpha', float(value))

    def toggle_mode(self):   #Toggle window size 
        self.is_borderless = not self.is_borderless
        if self.is_borderless:
            self.overrideredirect(True)
            self.mode_button.config(text="Windowed")
        else:
            self.overrideredirect(False)
            self.mode_button.config(text="Borderless")
        self.attributes("-topmost", 1)

  
if __name__ == "__main__":
    app = App()
    app.mainloop()

