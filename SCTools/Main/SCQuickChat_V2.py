# ###########SCQuickChatTool V2 - HalfbakedBaker & ChatGPT
# ###################################################
# ## 
# ## 
# ## 
# ## 
# ## 
# ## 



import tkinter.filedialog as filedialog
import pyautogui
import math
import tkinter as tk
import keyboard
import time 
import subprocess
#####
##### need to implement a function that calls the "add button" function x amount of times at the start with a empty string in order to generate 
##### blank buttons for each space in the grid 
#####



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SCQuickChat")
        self.attributes('-topmost', 1)
        self.attributes('-alpha', 1)
        self.geometry("600x550")
        self.configure(bg="#1E1E1E")
        self.keybind_press = False
        self.keybind = "ctrl+m"
        keyboard.add_hotkey(self.keybind, self.handle_keybind_press)
        
        # Bind right mouse button to drag the window around 
        self.bind("<ButtonPress-3>", self.start_move)
        self.bind("<ButtonRelease-3>", self.stop_move)
        self.bind("<B3-Motion>", self.on_move)


##################################################################
  


# create a frame to hold the buttons for quit and debug 
        button_frame_debug_quit = tk.Frame(self, bg="#1E1E1E")
        button_frame_debug_quit.pack(side=tk.TOP, fill=tk.X)

        ###  # create a debug button
        self.size_toggle = 0
        debug_button = tk.Button(button_frame_debug_quit, text="Debug", command=self.DebugToggle, bg="#7a0049", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        debug_button.pack(side=tk.LEFT, padx=5)

       ## # create a quit button
        self.click_count = 0
        self.quit_button = tk.Button(button_frame_debug_quit, text="EXIT GAME ({})".format(self.click_count), command=self.CheckClickCount, bg="#590000", fg="#FFFFFF", activebackground="#FF3030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.quit_button.pack(side=tk.RIGHT, padx=5)
       ### Add a label Ctrl+m to Show Hide 
        label = tk.Label(button_frame_debug_quit, text="CTRL+M", bg="#1E1E1E", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        label.pack(side="left", fill="x", padx=10, pady=10)

        # #### Slider Transparency Label 
        # self.slider_label = tk.Label(button_frame_debug_quit, text="Transparency", bg="#1E1E1E", mfg="#FFFFFF", font=("Arial", 10, "bold"))
        # self.slider_label.pack(side="bottom")
        ##########slider
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
        # Create and pack the size toggle button/ side bar
        self.size_toggle = 0
        button = tk.Button(windowSettingsToggleButton, text="Toggle Sidebar", command=self.change_window_size, bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        button.pack(side="right", fill="x", padx=1, pady=1)

        #### pack the window settings button frame 
        windowSettingsToggleButton.pack(side="top", fill="x", pady=5)


#########################################################################################################

        # # Create and pack the open Quick Chat Tool button
        # self.button1 = tk.Button(windowSettingsToggleButton, text="SCTool", command=lambda: subprocess.Popen(["python", "SCTool.py"]), bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        # self.button1.pack(side="top", padx=10, pady=10)

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


    def handle_keybind_press(self): ## Toggle Window Visibility / Show Hide QuickChat Ctel
        self.keybind_press = not self.keybind_press
        if self.keybind_press:
            self.withdraw()
            x, y = self.winfo_rootx() + self.winfo_width() // 2, self.winfo_rooty() + self.winfo_height() // 2
        else:
            self.deiconify()
            self.update_idletasks()
            self.lift()
            self.focus_force()
            self.after(0, lambda: pyautogui.moveTo(self.winfo_rootx() + self.winfo_width() / 2, self.winfo_rooty() + self.winfo_height() / 2))
          
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


app = App()
app.update()
app.mainloop()


#### function to call other function 16 times 



# ########################################################