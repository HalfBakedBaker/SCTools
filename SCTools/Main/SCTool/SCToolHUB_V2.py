# # # ###########SCToolHUB V2 - HalfbakedBaker & ChatGPT


# # ######## HUB 




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
        self.geometry("1050x40")
        self.create_widgets()
         # Bind right mouse button to drag the window
        self.bind("<ButtonPress-3>", self.start_move)
        self.bind("<ButtonRelease-3>", self.stop_move)
        self.bind("<B3-Motion>", self.on_move)
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
        self.button0 = tk.Button(web_buttons, text="ChatTool", command=lambda: subprocess.Popen(["python", "SCQuickChat_V2.py"]), bg="#321977", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button0.pack(side="left", padx=10, pady=10)
        # Create and pack the open SCTool button
        self.button1 = tk.Button(web_buttons, text="SCTool", command=lambda: subprocess.Popen(["python", "SCTool.py"]), bg="#321977", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button1.pack(side="left", padx=10, pady=10)




        # Create and pack the open Website 1 button
        self.button2 = tk.Button(web_buttons, text="Spectrum", command=lambda: openwebpage_process(Url="https://robertsspaceindustries.com/spectrum"), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button2.pack(side="left", padx=10, pady=10)
        # Create and pack the other website buttons 
        self.button3 = tk.Button(web_buttons, text="erkul DPS", command=lambda: openwebpage_process(Url="https://www.erkul.games"), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button3.pack(side="left", padx=10, pady=10)
        # Create and pack the other website buttons 
        self.button4 = tk.Button(web_buttons, text="Scodex", command=lambda:openwebpage_process(Url="https://scodex.garga.net"), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button4.pack(side="left", padx=10, pady=10)
        # Create and pack the other website buttons 
        self.button5 = tk.Button(web_buttons, text="SCWiki", command=lambda:openwebpage_process(Url="https://starcitizen.tools"), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button5.pack(side="left", padx=10, pady=10)
        # Create and pack the other website buttons 
        self.button6 = tk.Button(web_buttons, text="EUXTrade", command=lambda:openwebpage_process(Url="https://uexcorp.space"), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button6.pack(side="left", padx=10, pady=10)
        # # Create and pack the other website buttons 
        # self.button7 = tk.Button(web_buttons, text="IssueCouncil", command=lambda:openwebpage_process(Url="https://www.Google.com"), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        # self.button7.pack(side="left", padx=10, pady=10)

        # Create the text input and pack it
        self.text_input = tk.Entry(web_buttons, bg="#1E1E1E", fg="#FFFFFF", highlightthickness=0, bd=0, font=("Arial", 10, "bold"))
        self.text_input.insert(0, "Search Google")
        self.text_input.pack(side="left", padx=10, pady=10)
        
        # Create the Search Google Button
        self.button8 = tk.Button(web_buttons, text="Search", command=lambda:openwebpage_process(Url="https://www.google.com/search?q=" + self.text_input.get()), bg="#007E9E", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button8.pack(side="left", padx=10, pady=10)
        
        

#### Example buttons 

        # # Create and pack the other website buttons 
        # self.button9 = tk.Button(web_buttons, text="Example", command=lambda:openwebpage_process(Url="https://www.example.com"), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        # self.button9.pack(side="left", padx=10, pady=10)
        # # Create and pack the other website buttons 
        # self.button10 = tk.Button(web_buttons, text="Example", command=lambda:openwebpage_process(Url="https://www.example.com"), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        # self.button10.pack(side="left", padx=10, pady=10)



        # Create a frame for the window settings
        window_settings = tk.LabelFrame(self, text="Window Settings")
        # Pack the frame to the top
        window_settings.pack(side="top", fill="x")
        # Create the window settings frame
        window_settings = tk.LabelFrame(self, text="Window Settings", bg="#2C2C2C", fg="white", font=("Arial", 12, ))
        # Create and pack the transparency slider
        self.slider = tk.Scale(web_buttons, from_=0.2, to=1, resolution=0.1, orient="horizontal", label="",showvalue=False, command=self.set_transparency, bg="#1E1E1E", fg="#FFFFFF", troughcolor="#565656", highlightbackground="#1E1E1E", bd=0, font=("Arial", 10, "bold"))
        self.slider.set(1) # Set slider value to 1 by default
        self.slider.pack(side="top", fill="x", padx=0, pady=0)
        # Button to toggle window mode
        self.mode_button = tk.Button(web_buttons, text="Borderless", command=self.toggle_mode, bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.mode_button.pack(side="top", fill="x", padx=1, pady=1)

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
###

  
if __name__ == "__main__":
    app = App()
    app.mainloop()











##################### Search google Text Example 

# def search(query):
#     base_url = "https://www.google.com/search?q="
#     query_url = base_url + query.replace(" ", "+")
#     print(query_url)


# search(query="potato")


 #### To Do . Merge all apps into the hub instead of calling external scripts?