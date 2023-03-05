# # # ###########SCToolHUB V2 - HalfbakedBaker & ChatGPT



import tkinter as tk
import subprocess
import webview
import multiprocessing 
import webbrowser
from tkinter import *
import keyboard
import pyautogui

import time 
import psutil




######################################## SC HUB Main  
def openwebpage_process(Url):
    webbrowser.open(Url) # open new tab Default


class App_HUB(tk.Tk):
    def __init__(self):
        super().__init__()
        print("Hub Ready...")

        self.title("HUB")
        self.is_borderless = False
        self.attributes('-topmost', 1) # Force window above all others
        self.attributes('-alpha', 1) # Set default transparency to 1
        self.geometry("1425x25")
        self.create_widgets()
         # Bind right mouse button to drag the window
        self.bind("<ButtonPress-3>", self.start_move)
        self.bind("<ButtonRelease-3>", self.stop_move)
        self.bind("<B3-Motion>", self.on_move)
        self.toggle_mode() # toggle window mode on start 


        self.keybind_press = False
        self.keybind = "<+m"
        keyboard.add_hotkey(self.keybind, self.handle_keybind_press)

                # Get the screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        # Calculate the x and y position for the window
        x = int((screen_width - 1050) / 3) # Center the window horizontally
        y = 0 # Place the window at the top of the screen
        
        # Set the window position
        self.geometry("1425x25+{}+{}".format(x, y))

    def handle_keybind_press(self): ## Toggle Window Visibility / Show Hide
        self.keybind_press = not self.keybind_press
        if self.keybind_press:            self.withdraw(),print("Hub Hidden")  ### Error handled by running the hub in seporate process 
 
        else:
            self.deiconify()
            self.update_idletasks()
            self.lift()
            self.focus_force()
            print("Hub Visibile ")
            # self.after(0, lambda: pyautogui.moveTo(self.winfo_rootx() + self.winfo_width() / 2, self.winfo_rooty() + self.winfo_height() / 2))

    def hideapp(self):
        print("HUBHidden")
        self.withdraw()

###########################################################################################################################################
    def create_widgets(self):

######## SC Tool Tool Bar

        # Create a frame for the web buttons
        web_buttons = tk.Frame(self, bg="#2C2C2C")

        # Create a label for the frame
        label = tk.Label(web_buttons, text="<+m", fg="#FFFFFF", bg="#2C2C2C", font=("Arial", 12, "bold"))

        # Pack the label and web buttons frame
        label.pack(side="left", padx=1, pady=1)
        web_buttons.pack(side="top", fill="x")

###############################################  Redacted to improve performance. Will Show all menus at start and then toggle visibility instead of making new instances 
        # Create and pack the open Quick Chat Tool button
        self.button0 = tk.Button(web_buttons, text="ChatTool", command=lambda: self.openquickchat(), bg="#007E9E", fg="#FFFFFF",activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
      
        self.button0.pack(side="left", padx=4, pady=1)
        # Create and pack the open SCTool button
        self.button1 = tk.Button(web_buttons, text="SCTool", command=lambda: self.openSCTool(),  bg="#007E9E", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button1.pack(side="left", padx=4, pady=1)

################################################################################################################################################

        # Create and pack the open Website 0 button
        self.button0 = tk.Button(web_buttons, text="Galactapedia", command=lambda: openwebpage_process(Url="https://robertsspaceindustries.com/galactapedia"), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button0.pack(side="left", padx=4, pady=1)

        # Create and pack the open Website 0 button
        self.button9 = tk.Button(web_buttons, text="Issue Council", command=lambda: openwebpage_process(Url="https://issue-council.robertsspaceindustries.com"), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button9.pack(side="left", padx=4, pady=1)

        # Create and pack the open Website 1 button
        self.button2 = tk.Button(web_buttons, text="Spectrum", command=lambda: openwebpage_process(Url="https://robertsspaceindustries.com/spectrum"), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button2.pack(side="left", padx=4, pady=1)
        # Create and pack the other website buttons 
        self.button_fleetyard = tk.Button(web_buttons, text="Fleetyard", command=lambda: openwebpage_process(Url="https://fleetyards.net/hangar/"), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button_fleetyard.pack(side="left", padx=4, pady=1)
        # Create and pack the other website buttons 
        self.button3 = tk.Button(web_buttons, text="erkul DPS", command=lambda: openwebpage_process(Url="https://www.erkul.games"), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button3.pack(side="left", padx=4, pady=1)
        # Create and pack the other website buttons 
        self.button4 = tk.Button(web_buttons, text="Scodex", command=lambda:openwebpage_process(Url="https://scodex.garga.net"), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button4.pack(side="left", padx=4, pady=1)
        # Create and pack the other website buttons 
        self.button5 = tk.Button(web_buttons, text="SCWiki", command=lambda:openwebpage_process(Url="https://starcitizen.tools"), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button5.pack(side="left", padx=4, pady=1)
        # Create and pack the other website buttons 
        self.button6 = tk.Button(web_buttons, text="EUXTrade", command=lambda:openwebpage_process(Url="https://uexcorp.space"), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button6.pack(side="left", padx=4, pady=1)
        # Create and pack the other website buttons 
        self.button7 = tk.Button(web_buttons, text="YouTube", command=lambda:openwebpage_process(Url="https://www.youtube.com"), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button7.pack(side="left", padx=4, pady=1)

        # Create the text input and pack it
        self.text_input = tk.Entry(web_buttons, bg="#1E1E1E", fg="#FFFFFF", highlightthickness=0, bd=0, font=("Arial", 10, "bold"))
        self.text_input.insert(0, "Search Google")
        self.text_input.pack(side="left", padx=1, pady=1)

        # Create and pack the search button
        self.button8 = tk.Button(web_buttons, text="Search", command=lambda: openwebpage_process(Url="https://www.google.com/search?q=" + self.text_input.get()), bg="#007E9E", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button8.pack(side="left", padx=4, pady=1)

        # Create a frame for the window settings
        window_settings = tk.LabelFrame(self, text="Window Settings")
        # Pack the frame to the top
        window_settings.pack(side="top", fill="x")
        # Create the window settings frame
        window_settings = tk.LabelFrame(self, text="Window Settings", bg="#2C2C2C", fg="white", font=("Arial", 12, ))
        # Create and pack the transparency slider
        DefaultSliderValue =  .7
        self.slider = tk.Scale(web_buttons, from_=0.2, to=1, resolution=0.1,width=10, orient="horizontal", label="",showvalue=False, command=self.set_transparency, bg="#1E1E1E", fg="#FFFFFF", troughcolor="#565656", highlightbackground="#1E1E1E", bd=0, font=("Arial", 10, "bold"))
        self.slider.set(DefaultSliderValue) # Set slider value to 1 by default
        self.slider.pack(side="left", fill="x", padx=0, pady=0)
        # Button to toggle window mode
        self.mode_button = tk.Button(web_buttons, text="Borderless", command=self.toggle_mode, bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.mode_button.pack(side="left", fill="x", padx=4, pady=1)

        # Button to Quit SCTools
        self.QuitSCT = tk.Button(web_buttons, text="QuitSCT", command=self.destroy, bg="#590000", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.QuitSCT.pack(side="right", fill="x", padx=4, pady=1)

    
        # Button to hide window 
        self.HideSCT = tk.Button(web_buttons, text="Hide", command=self.hideapp, bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.HideSCT.pack(side="right", fill="x", padx=4, pady=1)

    
        # Pack the window settings frame
        window_settings.pack(side="top", fill="x", padx=1, pady=1)
        self.configure(background="#000000")

    def openquickchat(self):
        print("QuickChatStarting")
        # from SCQuickChat_V2 import App_SCQuickChat
        # appSCQC = App_SCQuickChat()
        # appSCQC.mainloop()
        
        self.appQC = subprocess.Popen(["python", "SCQuickChat_V2.py"]) ## Better way of doing it, Seems to be more stable than trying to import the entire thing when the function is called. instead it will run the script (Must include scripts as this is a dependant method)
        # self.appQC.terminate()

    def openSCTool(self):
        print("OpenSCToolStarting")
        # from SCTool import App_SCTool 
        # appSCT = App_SCTool()
        # appSCT.mainloop()
        self.appSCT = subprocess.Popen(["python", "SCTool.py"]) ## Better way of doing it, Seems to be more stable than trying to import the entire thing when the function is called. instead it will run the script (Must include scripts as this is a dependant method)
        # self.appSCT.terminate()
        
    def close_quickchat(self):
        print("Close QC")
        self.appQC.terminate()
 
    def close_sctool(self):
        self.appSCT.terminate()
        print("Close SCT")

#######################################################################################################################################

    def set_transparency(self, value): # Set transparanecy value 
        self.attributes('-alpha', float(value))

    def toggle_mode(self):   #Toggle window  Borderless
        self.is_borderless = not self.is_borderless
        if self.is_borderless:
            self.overrideredirect(True)
            self.mode_button.config(text="Windowed")
        else:
            self.overrideredirect(False)
            self.mode_button.config(text="Borderless")
        self.attributes("-topmost", 1)
    ### functions to allow movemet of window when in borderless mode 
    def start_move(self, event):
        self.x = event.x
        self.y = event.y
    def stop_move(self, event):
        self.x = None
        self.y = None
    def on_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(f"+{x}+{y}")

    def close_all_subprocesses(self):
        for proc in psutil.process_iter():
            try:
                if proc.name().startswith("python"):
                    proc.terminate()
                    print(f"Subprocess {proc.pid} terminated.")
            except psutil.AccessDenied:
                print(f"Failed to terminate subprocess {proc.pid} (access denied).")

    def OpenToolStart(self):
        print("Launching...")
        self.openquickchat()
        self.openSCTool()
        print("SCTools Ready...")
        print("SCQuickChatReady...")
        print("Ready...")
   
    def destroy(self):
        print("Close SCTHub")  
        # self.close_quickchat()
        # self.close_sctool()
        self.close_all_subprocesses()
        # self.appQC.terminate()
        time.sleep(0.1)
        # self.appSCT.terminate()
        super().destroy()
    


print("SCToolHub 0.0.2")

print("24 Feb 2023")
print("init...")

if __name__ == "__main__":

    App_HUB = App_HUB()

    print("############################ Starting #################################")

    print("Mainloop Running..")
    App_HUB.OpenToolStart()
    App_HUB.mainloop()  
