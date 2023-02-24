###################### Entry Backup Legacy 

# # ##### Entry Point to SCHub

# import win32gui
# import win32con
# from SCToolHUB_V2 import App_HUB
# # from SCQuickChat_V2 import App_SCQuickChat
# # from SCTool import App_SCTool
# if __name__ == '__main__':
#     print("SCToolHub - 0.0.1 ")
#     print("Build : Wed 22 Feb 2023 ")

#     # Find the console window and minimize it
#     hwnd = win32gui.GetForegroundWindow()
#     win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

#     # Start the main application
#     App_HUB().mainloop()  #1













# better format for hub //////////////////////////////////////////////

import tkinter as tk
import multiprocessing
# ###########SCQuickChatTool V2 - HalfbakedBaker 

import tkinter.filedialog as filedialog
import pyautogui
import math
import tkinter as tk
import keyboard
import time 
import webbrowser
import subprocess
import threading




def openwebpage_process(Url):
    webbrowser.open(Url)

class App1(tk.Tk):# Hub
    def __init__(self):
        super().__init__()

        self.title("SCT")
        self.is_borderless = False
        self.attributes('-topmost', 1) # Force window above all others
        self.attributes('-alpha', 1) # Set default transparency to 1
        self.geometry("1080x25")
        self.create_widgets()
        # Bind right mouse button to drag the window
        self.bind("<ButtonPress-3>", self.start_move)
        self.bind("<ButtonRelease-3>", self.stop_move)
        self.bind("<B3-Motion>", self.on_move)
        self.toggle_mode() # toggle window mode on start 
                # Get the screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        # Calculate the x and y position for the window
        x = int((screen_width - 1050) / 2) # Center the window horizontally
        y = 0 # Place the window at the top of the screen
        
        # Set the window position
        self.geometry("1150x25+{}+{}".format(x, y))


    def create_widgets(self):

######## SC Tool Tool Bar

        # Create a frame for the web buttons
        web_buttons = tk.Frame(self, bg="#2C2C2C")

        # Create a label for the frame
        label = tk.Label(web_buttons, text="<+m", fg="#FFFFFF", bg="#2C2C2C", font=("Arial", 12, "bold"))

        # Pack the label and web buttons frame
        label.pack(side="left", padx=1, pady=1)
        web_buttons.pack(side="top", fill="x")

################################################
#         # Create and pack the open Quick Chat Tool button
#         self.button0 = tk.Button(web_buttons, text="ChatTool", command=lambda: subprocess.Popen(["python", "SCQuickChat_V2.py"]), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
    
#         self.button0.pack(side="left", padx=4, pady=1)
#         # Create and pack the open SCTool button
#         self.button1 = tk.Button(web_buttons, text="SCTool", command=lambda: subprocess.Popen(["python", "SCTool.py"]), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
#         self.button1.pack(side="left", padx=4, pady=1)
# ##############################

        # Create and pack the open Website 0 button
        self.button9 = tk.Button(web_buttons, text="Issue Council", command=lambda: openwebpage_process(Url="https://issue-council.robertsspaceindustries.com"), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button9.pack(side="left", padx=4, pady=1)

        # Create and pack the open Website 1 button
        self.button2 = tk.Button(web_buttons, text="Spectrum", command=lambda: openwebpage_process(Url="https://robertsspaceindustries.com/spectrum"), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button2.pack(side="left", padx=4, pady=1)
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
        # # Create and pack the other website buttons 
        # self.button7 = tk.Button(web_buttons, text="IssueCouncil", command=lambda:openwebpage_process(Url="https://www.Google.com"), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        # self.button7.pack(side="left", padx=10, pady=10)

        # Create the text input and pack it
        self.text_input = tk.Entry(web_buttons, bg="#1E1E1E", fg="#FFFFFF", highlightthickness=0, bd=0, font=("Arial", 10, "bold"))
        self.text_input.insert(0, "Search Google")
        self.text_input.pack(side="left", padx=1, pady=1)
        
        # Create the Search Google Button
        self.button8 = tk.Button(web_buttons, text="Search", command=lambda:openwebpage_process(Url="https://www.google.com/search?q=" + self.text_input.get()), bg="#007E9E", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.button8.pack(side="left", padx=4, pady=1)
        
        

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
        self.slider.pack(side="right", fill="x", padx=0, pady=0)
        # Button to toggle window mode
        self.mode_button = tk.Button(web_buttons, text="Borderless", command=self.toggle_mode, bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.mode_button.pack(side="right", fill="x", padx=4, pady=1)


        # # Button to toggle window mode
        # self.QuitSCT = tk.Button(web_buttons, text="QuitSCT", command=self.destroy, bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        # self.QuitSCT.pack(side="right", fill="x", padx=4, pady=1)


        # Pack the window settings frame
        window_settings.pack(side="top", fill="x", padx=1, pady=1)
        self.configure(background="#000000")



    def HideApp(self):
        print("Hideapp1")
        # App1.withdraw(app1)
        # App2.withdraw(app2)
        # App3.withdraw(app3)

    def ShowApp(self):
        print("ShowApp1")
        # App1.lift(app1)
        # App2.lift(app2)
        # App3.lift(app3)


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

    def destroy(self):
        print("Close")
        super().destroy()

class App2(tk.Tk):# Quick Chat
    def __init__(self):
        super().__init__()
        self.title("SCQuickChat")
        self.attributes('-topmost', 1)
        self.attributes('-alpha', 1)
        self.geometry("600x550")
        self.configure(bg="#1E1E1E")
        # self.keybind_press = False
        # self.keybind = "<+m"
        # keyboard.add_hotkey(self.keybind, self.handle_keybind_press)
        
        # Bind right mouse button to drag the window around 
        self.bind("<ButtonPress-3>", self.start_move)
        self.bind("<ButtonRelease-3>", self.stop_move)
        self.bind("<B3-Motion>", self.on_move)

        self.after_id = None
##################################################################
  
# create a frame to hold the buttons for quit and debug 
        button_frame_debug_quit = tk.Frame(self, bg="#1E1E1E")
        button_frame_debug_quit.pack(side=tk.TOP, fill=tk.X)
        self.slider = tk.Scale(button_frame_debug_quit, from_=0.2, to=1, resolution=0.1, orient="horizontal", command=self.set_transparency, showvalue= False, bg="#1E1E1E", fg="#FFFFFF", troughcolor="#565656", highlightbackground="#1E1E1E", bd=0)
        self.slider.set(1) # Set slider value to 1 by default
        self.slider.pack(side="top", fill="both", padx=10, pady=10)

        # Pack the window settings frame
        button_frame_debug_quit.pack(side="top", fill="x", pady=5)



####    Create frame for window setting toggle buttons 
        windowSettingsToggleButton = tk.Frame(self, bg="#1E1E1E")

        # Create and pack the toggle window mode button
        self.is_borderless = False
        self.toggle_mode_button = tk.Button(windowSettingsToggleButton, text="Toggle Window Mode", command=self.toggle_mode, bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.toggle_mode_button.pack(side="left", fill="x", padx=1, pady=1)
        
        # # Create close
        # closebbutton= tk.Button(windowSettingsToggleButton, text="close", command=self.Close, bg="#565656", fg="#FFFFFF", activebackground="#FF8C00", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        # closebbutton.pack(side="left", fill="x", padx=10, pady=10)
     
        
        
        # Create and pack the size toggle button/ side bar
        self.size_toggle = 0
        button = tk.Button(windowSettingsToggleButton, text="Toggle Sidebar", command=self.change_window_size, bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        button.pack(side="left", fill="x", padx=1, pady=1)

        #### pack the window settings button frame 
        windowSettingsToggleButton.pack(side="top", fill="x", pady=5)


#########################################################################################################


       # Create and pack the canvas that displays new buttons 
        self.canvas = tk.Canvas(self, width=300, height=300, bg="gray")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Create and pack the "Enter Text" label
        label = tk.Label(self, text="Enter Text", bg="#1E1E1E", fg="#FFFFFF", font=("Arial", 10, "bold"))
        label.pack(side="top", padx=5, pady=5)

        # Create and pack the button name entry
        self.button_name_entry = tk.Entry(self, bg="#565656", fg="#FFFFFF", highlightbackground="#1E1E1E", bd=0, font=("Arial", 10))
        self.button_name_entry.pack(side="top", fill="x", padx=10, pady=10)

        ### # Create and pack the Add button
        add_button = tk.Button(self, text="Add", command=self.add_button, bg="#014214", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        add_button.pack(side="top", fill="x", padx=10, pady=10)

        # Create and pack the Delete All button
        deleteall_button = tk.Button(self, text="Delete All", command=self.deleteall_buttons, bg="#520000", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        deleteall_button.pack(side="top", fill="x", padx=10, pady=10)

        # Create and pack the Delete Selected button
        delete_button = tk.Button(self, text="Delete Selected", command=self.delete_selected_button, bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        delete_button.pack(side="top", fill="x", padx=10, pady=10)

        # Create save button
        save_button = tk.Button(self, text="Save", command=self.save, bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        save_button.pack(side="top", fill="x", padx=10, pady=10)

        # Create load button
        load_button = tk.Button(self, text="Load", command=self.load, bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        load_button.pack(side="top", fill="x", padx=10, pady=10)

     
        # Create and pack the listbox for the buttons
        self.button_listbox = tk.Listbox(self, bg="#565656", fg="#FFFFFF", highlightbackground="#1E1E1E", bd=0, font=("Arial", 10, "bold"))
        self.button_listbox.pack(side="left", fill="both", expand=True)
        
        #### Define Varibles
    
        ## updates buttons added to circle 
        self.current_buttons = []

        # array to store the button names
        self.button_names = []
        ### config
        self.toggle_mode() # set window mode borderless at start 



        # self.loadStart() # load config 

############### New functions to show / hide the app 
    def ShowApp(self):
        print("ShowApp2")
        self.lift()

    def HideApp(self):
        print("Hideapp2")
        self.withdraw()



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


    def change_window_size(self): ## Toggle window size button
        # button_name = ""
        # toggle between two different window sizes
        if self.size_toggle == 0:
            self.geometry("470x450")
            self.size_toggle = 1
            ################################
        else:
            self.geometry("600x550")
            self.size_toggle = 0

    def set_transparency(self, value): # Set transparanecy value from slider
        self.attributes('-alpha', float(value))

    def toggle_mode(self):# toggle Window mode button 
        self.is_borderless = not self.is_borderless
        if self.is_borderless:
            self.overrideredirect(True)
        else:
            self.overrideredirect(False)
        self.attributes("-topmost", 1)
###############################################################################
#############################  #Original Add button Function 

    def add_button(self, button_name=None, max_columns=4):#### add new button to grid 
        maxentry = 40 ## define max amount of buttons
        if not button_name:
            button_name = self.button_name_entry.get()
        if button_name:
            if len(self.current_buttons) >= maxentry:
                print("Reached Limit of", maxentry, "entries")
                return
            button = tk.Button(self.canvas, text=button_name, command=lambda name=button_name: self.print_button_name(name),
                           bg="#F8F8F8", fg="#000000", activebackground="#014214", activeforeground="#000000",
                            relief="flat", font=("Arial", 8, "bold"), width=8, height=4, wraplength=80, padx= 10,pady=10) # set wraplength to 80 pixels
            button.config(width=10, height=3) ### set the uniform size for new buttons 
            self.current_buttons.append(button)
            self.button_listbox.insert("end", button_name)
            num_buttons = len(self.current_buttons)
            rows = int(math.ceil(num_buttons / max_columns))
            cols = min(num_buttons, max_columns)
            padding = 10
            for i, b in enumerate(self.current_buttons):
                row = i // cols
                col = i % cols
                b.grid(row=row, column=col, padx=padding, pady=padding)

    #################################################################################

    def print_button_name(self, name): ## print the name of the button pressed and type to keyboard
        def type_button_name():
            # store current mouse position
            original_pos = pyautogui.position()
            # move mouse outside of window and click the left mouse button
            pyautogui.moveTo(500,50)
            pyautogui.click(button='left')
            # press enter
            keyboard.press_and_release('enter')
            # add a delay of 1 second
            time.sleep(0.02)
            # type out the name of the button (type out the letters)
            pyautogui.typewrite(name)
            # add a delay of 1 second
            time.sleep(0.02)
            keyboard.press_and_release('enter')
            # move mouse back to original position
            pyautogui.moveTo(original_pos)

        self.after(1, type_button_name)

    def print_button_debug(self, name): ## Enables Debugging in SC 
        def print_button_debug():
            # store current mouse position
            original_pos = pyautogui.position()
            # move mouse outside of window and click the left mouse button
            pyautogui.moveTo(500,50)
            pyautogui.click(button='left')
            # press ``
            keyboard.press_and_release('`')
            # add a delay of 1 second
            time.sleep(0.02)
            # type out the name of the button (type out the letters)
            pyautogui.typewrite(name)
            # add a delay of 1 second
            time.sleep(0.02)
            keyboard.press_and_release('enter')
            # add a delay of 1 second
            time.sleep(0.02)
            # press ``
            keyboard.press_and_release('`')
            # move mouse back to original position
            pyautogui.moveTo(original_pos)

        self.after(1, print_button_debug)

    def print_button_quit(self,name): ## Quickly Quits the game Need to implement a counter so it exits after multiple clicks to avoid mistakes 
        
        def print_button_quit():
          # store current mouse position
            original_pos = pyautogui.position()
            # move mouse outside of window and click the left mouse button
            pyautogui.moveTo(500,50)
            pyautogui.click(button='left')
            # press ``
            keyboard.press_and_release('`')
            # add a delay of 1 second
            time.sleep(0.02)
            # type out the name of the button (type out the letters)
            pyautogui.typewrite(name)
            # add a delay of 1 second
            time.sleep(0.02)
            keyboard.press_and_release('enter')
            # move mouse back to original position           
            pyautogui.moveTo(original_pos)
        self.after(1, print_button_quit)

    def deleteall_buttons(self): ### delete all buttons 
        for button in self.current_buttons:
            button.destroy()
        self.current_buttons = []
        self.button_listbox.delete(0, "end")

    def delete_selected_button(self): ## delete selected button 
        selected_index = self.button_listbox.curselection()
        if selected_index:
            button_to_delete = self.current_buttons[selected_index[0]]
            button_to_delete.destroy()
            self.current_buttons.remove(button_to_delete)
            self.button_listbox.delete(selected_index)
            
    def load(self):   ## load buttons from text file 
        # Prompt the user to select a text file
        file_path = filedialog.askopenfilename()
        self.deleteall_buttons()
        # Read the button names from the file
        with open(file_path, 'r') as f:
            button_names = f.readlines()

        # Add a button for each name read from the file
        for button_name in button_names:
            button_name = button_name.strip()  # Remove newline character from end of line
            self.add_button(button_name=button_name)  # Call add_button function with button_name argument

    def loadStart(self):   ## load buttons from text file 
        # Prompt the user to select a text file
        file_path = filedialog.askopenfilename()
        if file_path != '':
            # self.deleteall_buttons()
            # Read the button names from the file
            with open(file_path, 'r') as f:
                button_names = f.readlines()

            # Add a button for each name read from the file
            for button_name in button_names:
                button_name = button_name.strip()  # Remove newline character from end of line
                self.add_button(button_name=button_name)

    def save(self):  # save buttons 
        # Prompt the user for the save file path
        file_path = filedialog.asksaveasfilename(defaultextension='.txt')

        # Open the file for writing
        with open(file_path, 'w') as f:
            # Write each button name to a new line in the file
            for button in self.current_buttons:
                f.write(button.cget('text') + '\n')
        print('Saved current buttons to file:', file_path)

    def DebugToggle(self):
        if hasattr(self, 'hello_printed') and self.hello_printed:
            # print("Goodbye")
            # self.print_button_name(name="r_displayinfo 0")
            self.print_button_debug(name="r_displayinfo 0")
            self.hello_printed = False
        else:
            # print("Hello")
            # self.print_button_name(name="r_displayinfo 4")
            self.print_button_debug(name="r_displayinfo 4")
            self.hello_printed = True

    def CheckClickCount(self):
        if self.click_count < 4:
            self.click_count += 1
            self.quit_button.config(text="EXIT GAME ({})".format(5 - self.click_count))
        else:
            self.QuitGame()
            self.click_count = 0

    def QuitGame(self):

            self.print_button_quit(name="quit")
   
    def update(self):
        self.after(10, self.update)

class App3(tk.Tk):# SCTool
    def __init__(self):
        super().__init__()
        self.title("SCTool")
        self.attributes('-topmost', 1)
        self.attributes('-alpha', 1)
        self.geometry("750x90")

        # Get screen width and heightm,
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate x and y coordinates for the window
        x = int(screen_width/2 - 375) # 375 is half of the window width
        y = screen_height - 90 # 90 is the window height

        # Set the window position
        self.geometry("650x90+{}+{}".format(x, y))

        self.configure(bg="#1E1E1E")


        
        # Bind right mouse button to drag the window
        self.bind("<ButtonPress-3>", self.start_move)
        self.bind("<ButtonRelease-3>", self.stop_move)
        self.bind("<B3-Motion>", self.on_move)
        # self.keybind_press = False
        # self.keybind = "<+m"
        # keyboard.add_hotkey(self.keybind, self.handle_keybind_press)

        self.after_id = None

####################################################################################################
####    Create frame for window setting toggle buttons 
        WindowFrameSettings = tk.Frame(self, bg="#1E1E1E")

 #### pack the window settings button frame 
        WindowFrameSettings.pack(side="top", fill="x", pady=5)

  # create a frame to hold the template buttons 
        button_frame_template = tk.Frame(self, bg="#1E1E1E")
        button_frame_template.pack(side=tk.TOP, fill=tk.X)




  # create a frame to hold the buttons for F1 F2 (Mobiglass and camera )
        WindowFrameSettings = tk.Frame(self, bg="#1E1E1E")
        WindowFrameSettings.pack(side=tk.TOP, fill=tk.X)

####    ### Create Label for window settings frame 
        title_label = tk.Label(WindowFrameSettings, text="<+M", bg="#1E1E1E", fg="#FFFFFF", font=("Arial", 12, "bold"))
        title_label.pack(side="left", padx=0)
##### F1 = MobiGlass Button 
        self.size_toggle = 0
        mobiglass_button = tk.Button(WindowFrameSettings, text="Mobiglass", command=self.mobiglass, bg="#7a0049", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        mobiglass_button.pack(side=tk.LEFT, padx=5)
##### F2 = Star Map 

        self.size_toggle = 0
        map_button = tk.Button(WindowFrameSettings, text="Map", command=self.map, bg="#7a0049", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        map_button.pack(side=tk.LEFT, padx=5)
### comlink
# create a Comlink button
        comlink_button = tk.Button(WindowFrameSettings, text="Comlink", command=self.comlink, bg="#7a0049", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        comlink_button.pack(side=tk.LEFT, padx=5)
   
#### Camera 
        self.size_toggle = 0
        camera_button = tk.Button(WindowFrameSettings, text="Camera", command=self.camera, bg="#7a0049", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        camera_button.pack(side=tk.LEFT, padx=5)





       ## # create a quit button (Requires being clicked 5 times  for safety so check click count and update)
        self.click_count = 0
        self.quit_button = tk.Button(WindowFrameSettings, text="EXIT GAME ({})".format(self.click_count), command=self.CheckClickCount, bg="#590000", fg="#FFFFFF", activebackground="#FF3030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.quit_button.pack(side="right", padx=5)



        # Create and pack the toggle window mode button
        self.is_borderless = False
        self.toggle_mode_button = tk.Button(WindowFrameSettings, text="Window Mode", command=self.toggle_mode, bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.toggle_mode_button.pack(side="right", fill="x", padx=1, pady=1)
        
        
        # # create a button to Close the app 
        # self.HideButton = tk.Button(WindowFrameSettings, text="Close",command=self.destroy, bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        # self.HideButton.pack(side="left", padx=5, pady=5)
        
        
        
        ###Slider 
        self.slider = tk.Scale(WindowFrameSettings, from_=0.2, to=1, resolution=0.1, orient="horizontal", command=self.set_transparency,showvalue=False, bg="#1E1E1E", fg="#FFFFFF", troughcolor="#565656", highlightbackground="#1E1E1E", bd=0, length=100)
        self.slider.set(1) # Set slider value to 1 by default
        self.slider.pack(side="right", fill="x", padx=1)

        # # Create and pack the size toggle button/ side bar
        # self.size_toggle = 0
        # button = tk.Button(WindowFrameSettings, text="Toggle Sidebar", command=self.change_window_size, bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        # button.pack(side="left", fill="x", padx=1, pady=1)


        self.toggle_mode()

      #################

# Pack the window settings frame
        WindowFrameSettings.pack(side="top", fill="x", pady=5)
#########################################################################




      ################# New Debug Buttons 0 - 7 
        # create New debug buttons 
        # create a frame for the debug buttons
        button_frame_debug = tk.Frame(self, bg="#1F1F1F", height=50)
        button_frame_debug.pack(side=tk.TOP, fill=tk.X, pady=(5,0))

        # create a new frame for the debug buttons
        debug_button_frame = tk.Frame(button_frame_debug, bg="#1F1F1F", height=50)
       
        # create the debug buttons
        debug_names = ["debug 0", "debug 1", "debug 2", "debug 3", "debug 4", "Session 1", "Session 0", "Screenshot"]
        debug_commands = ["r_displayinfo 0", "r_displayinfo 1", "r_displayinfo 2", "r_displayinfo 3", "r_displayinfo 4", "r_displaySessionInfo 1", "r_displaySessionInfo 0", "r_getScreenShot 1"]
        for name, command in zip(debug_names, debug_commands):
            debug_button = tk.Button(debug_button_frame, text=name, command=lambda cmd=command: self.DebugButtons(cmd), bg="#922178", fg="#FFFFFF", activebackground="#922178", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
            debug_button.pack(side=tk.LEFT, padx=5)

        ### pack the debug button frame 
        debug_button_frame.pack(side=tk.LEFT, fill=tk.X, padx=(5,0))
    
    ##### new function to show / hide the app 
    def ShowApp(self):
        print("ShowApp3")
        self.lift()
        

    def HideApp(self):
        print("HideApp3")
        self.withdraw()


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


    def change_window_size(self): ## Toggle window size button
        # button_name = ""
        # toggle between two different window sizes
        if self.size_toggle == 0:
            self.geometry("470x450")
            self.size_toggle = 1
            ################################
        else: # Default Size 
            self.geometry("600x550")
            self.size_toggle = 0

    def set_transparency(self, value): # Set transparanecy value from slider
        self.attributes('-alpha', float(value))

    def toggle_mode(self):# toggle Window mode button 
        self.is_borderless = not self.is_borderless
        if self.is_borderless:
            self.overrideredirect(True)
        else:
            self.overrideredirect(False)
        self.attributes("-topmost", 1)

    def mobiglass(self):
     def type_mobiglass():
         # store current mouse position
         original_pos = pyautogui.position()
         # move mouse to mobiglass button position and click the left mouse button
         pyautogui.moveTo(100, 100)
         pyautogui.click(button='left')
         # add a delay of 0.1 second
         time.sleep(0.1)
         # press F1 key
         keyboard.press_and_release('f1')
         # add a delay of 0.1 second
         time.sleep(0.1)
         # move mouse back to original position
         pyautogui.moveTo(original_pos)

     self.after(1, type_mobiglass)

    def map(self):
        def type_mobiglass():
            # store current mouse position
            original_pos = pyautogui.position()
            # move mouse to mobiglass button position and click the left mouse button
            pyautogui.moveTo(100, 100)
            pyautogui.click(button='left')
            # add a delay of 0.1 second
            time.sleep(0.1)
            # press F2 key
            keyboard.press_and_release('f2')
            # add a delay of 0.1 second
            time.sleep(0.1)
            # move mouse back to original position
            pyautogui.moveTo(original_pos)
    
        self.after(1, type_mobiglass)

    def camera(self):
        def type_button_name():
            # store current mouse position
            original_pos = pyautogui.position()
            # move mouse to mobiglass button position and click the left mouse button
            pyautogui.moveTo(100, 100)
            pyautogui.click(button='left')
            # add a delay of 0.1 second
            time.sleep(0.1)
            # press F2 key
            keyboard.press_and_release('f4')
            # add a delay of 0.1 second
            time.sleep(0.1)
            # move mouse back to original position
            pyautogui.moveTo(original_pos)
    
        self.after(1, type_button_name)
        
    def comlink(self):
        def activate_comlink():
            # store current mouse position
            original_pos = pyautogui.position()
            # move mouse to comms button position and click the left mouse button
            pyautogui.moveTo(200, 200)
            pyautogui.click(button='left')
            # add a delay of 0.1 second
            time.sleep(0.1)
            # press F11 key
            keyboard.press_and_release('f11')
            # add a delay of 0.1 second
            time.sleep(0.1)
            # move mouse back to original position
            pyautogui.moveTo(original_pos)
    
        self.after(1, activate_comlink)
    
    def template_printbuttonfunction(self, name): ## print the name of the button pressed and type to keyboard
        def type_button_name():
            # store current mouse position
            original_pos = pyautogui.position()
            # move mouse to mobiglass button position and click the left mouse button
            pyautogui.moveTo(100, 100)
            pyautogui.click(button='left')
            # add a delay of 0.1 second
            time.sleep(0.1)
            # press F2 key
            keyboard.press_and_release('f')
            # add a delay of 0.1 second
            time.sleep(0.1)
            # move mouse back to original position
            pyautogui.moveTo(original_pos)
    
        self.after(1, type_button_name)

    def print_button_debug(self, name): ## Enables Debugging in SC 
        def print_button_debug():
            # store current mouse position
            original_pos = pyautogui.position()
            # move mouse outside of window and click the left mouse button
            pyautogui.moveTo(500,50)
            pyautogui.click(button='left')
            # press ``
            keyboard.press_and_release('`')
            # add a delay of 1 second
            time.sleep(0.02)
            # type out the name of the button (type out the letters)
            pyautogui.typewrite(name)
            # add a delay of 1 second
            time.sleep(0.02)
            keyboard.press_and_release('enter')
            # add a delay of 1 second
            time.sleep(0.02)
            # press ``
            keyboard.press_and_release('`')
            # move mouse back to original position
            pyautogui.moveTo(original_pos)

        self.after(1, print_button_debug)

    def print_button_quit(self,name): ## Quickly Quits the game after 5 clicks6
        
        def print_button_quit():
          # store current mouse position
            original_pos = pyautogui.position()
            # move mouse outside of window and click the left mouse button
            pyautogui.moveTo(500,50)
            pyautogui.click(button='left')
            # press ``
            keyboard.press_and_release('`')
            # add a delay of 1 second
            time.sleep(0.02)
            # type out the name of the button (type out the letters)
            pyautogui.typewrite(name)
            # add a delay of 1 second
            time.sleep(0.02)
            keyboard.press_and_release('enter')
            # move mouse back to original position           
            pyautogui.moveTo(original_pos)
        self.after(1, print_button_quit)

    def DebugToggleSize(self):
        if hasattr(self, 'hello_printed') and self.hello_printed:
            # print("Goodbye")
            # self.template_printbuttonfunction(name="r_displayinfo 0")
            self.print_button_debug(name="r_displayinfo 0")
            self.hello_printed = False
        else:
            # print("Hello")
            # self.template_printbuttonfunction(name="r_displayinfo 4")
            self.print_button_debug(name="r_displayinfo 4")
            self.hello_printed = True
   
   
   ########new debugging buttons x 7 
    def DebugButtons(self,SCCommand):
        name = SCCommand
        self.print_button_debug(name)


    def CheckClickCount(self):  ## allows quit button to be activated after 5 presses
        if self.click_count < 4:
            self.click_count += 1
            self.quit_button.config(text="EXIT GAME ({})".format(5 - self.click_count))
        else:
            self.QuitGame()
            self.click_count = 0

    def QuitGame(self):
            self.print_button_quit(name="quit")
    
    def template(self):
            self.template_printbuttonfunction(name="Template = mouse move To (500,50) ,click, 'enter', type>Template, 'enter', returnmouse")
      
    def update(self):
        self.after(10, self.update)
   



class KeybindClass():
    def __init__(self):
        # self.app1 = App1()
        # self.app2 = App2()
        # self.app3 = App3()
        # self.window = control_window

        self.keybind_press = False
        self.keybind = "<+m"
        keyboard.add_hotkey(self.keybind, self.handle_keybind_press)

    def handle_keybind_press(self):
        # print("Keybind Pressed")
        self.keybind_press = not self.keybind_press
        if self.keybind_press:
            App1.HideApp(app1)
            App2.HideApp(app2)
            App3.HideApp(app3)
           

            print("KeybindPressHello")
            return
        ###########  Runtime error main thread is not in main loop when trying to use functions to toggle visibility of windows with keybind. Works fine with button Not got a clue why because i suck at programming 
        ###### SUFFERING 
        else:
            print("KeybindPressBye")
            App1.ShowApp(app1)
            App2.ShowApp(app2)
            App3.ShowApp(app3)
       
            return
      




def listen_for_keybind():
    KeybindClass()
    keyboard.wait()

def toggle_app1():
        global app1
        if app1.winfo_viewable():
            app1.withdraw()
        else:
            app1.deiconify()
            app1.lift()
            app1.focus_force()

def toggle_app2():
    global app2
    if app2.winfo_viewable():
        app2.withdraw()
    else:
        app2.deiconify()
        app2.lift()
        app2.focus_force()

def toggle_app3():
    global app3
    if app3.winfo_viewable():
        app3.withdraw()
    else:
        app3.deiconify()
        app3.lift()
        app3.focus_force()

def toggleall():
    toggle_app1()
    toggle_app2()
    toggle_app3()

def exitALL():
    print("CloseAllApps")
    app1.quit()
    app2.quit()
    app3.quit()


if __name__ == "__main__":
    print("#################### Start Entry ##################")
    print("OpenEntryPoint")



    app1 = App1()
    print("OpenApp1")
    # app1.HideApp()

    app2 = App2()
    print("OpenApp2")
    app2.HideApp()
    
    app3 = App3()
    print("OpenApp3")
    app3.HideApp()
    
    KeybindCL = KeybindClass()

    KeybindCL.handle_keybind_press



### Make Window for toggle visibility / quit ///  Replace hub with this and migrate contents of Hub over ?
    Alpha = 1
    Background = "#1E1E1E"
    WindowSize = "800x100"
    BorderlessMode = True


    control_window = tk.Tk()
    control_window.title("SCQuickChat")
    control_window.attributes('-topmost', 1)
    control_window.attributes('-alpha', Alpha)
    control_window.geometry(WindowSize)
    control_window.configure(bg=Background)
    is_borderless = not BorderlessMode






    def start_move(event):
        # print("StartMove")
        control_window.x = event.x
        control_window.y = event.y

    def stop_move(event):
        # print("StopMove")
        control_window.x = None
        control_window.y = None

    def on_move(event):
        # print("OnMove")
        deltax = event.x - control_window.x
        deltay = event.y - control_window.y
        x = control_window.winfo_x() + deltax
        y = control_window.winfo_y() + deltay
        control_window.geometry(f"+{x}+{y}")

    control_window.bind("<ButtonPress-3>", start_move)
    control_window.bind("<ButtonRelease-3>", stop_move)
    control_window.bind("<B3-Motion>", on_move)

    button1 = tk.Button(control_window, text="Hub", command=toggle_app1)
    button1.pack(side=tk.LEFT, padx=10, pady=10)

    button2 = tk.Button(control_window, text="QuickChat", command=toggle_app2)
    button2.pack(side=tk.LEFT, padx=10, pady=10)

    button3 = tk.Button(control_window, text="SCTool", command=toggle_app3)
    button3.pack(side=tk.LEFT, padx=10, pady=10)

    button4 = tk.Button(control_window, text="ToggleAll", command=toggleall)
    button4.pack(side=tk.LEFT, padx=10, pady=10)

    button5 = tk.Button(control_window, text="Close All", command=exitALL, bg="#590000",fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
    button5.pack(side=tk.LEFT, padx=10, pady=10)

    def toggle_mode():
        global is_borderless
        is_borderless = not is_borderless
        if is_borderless:
            control_window.overrideredirect(True)
            mode_button.config(text="Windowed")
        else:
            control_window.overrideredirect(False)
            mode_button.config(text="Borderless")
        control_window.attributes("-topmost", 1)

    mode_button = tk.Button(control_window, text="Borderless", command=toggle_mode, bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
    mode_button.pack(side="left", fill="x", padx=4, pady=1)












    toggle_mode()   ## toggles window mode for the new entry hub
    control_window.mainloop()








