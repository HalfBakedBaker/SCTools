# ###########SCQuickChatTool V2 - HalfbakedBaker 

import tkinter.filedialog as filedialog
import pyautogui
import math
import tkinter as tk
import keyboard
import time 
import os


class App_SCQuickChat(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("SCQuickChat")
        self.attributes('-topmost', 1)
        self.attributes('-alpha', 1)
        self.geometry("600x550")
        self.configure(bg="#1E1E1E")

      
        # Get screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Set the window width and height
        window_width = 600
        window_height = 550
        

        # Set the window position to the right of the screen
        window_x_position = 1550  #screen_width - window_width
        window_y_position = 500

        # Set the geometry of the window
        self.geometry(f"{window_width}x{window_height}+{window_x_position}+{window_y_position}")


        self.keybind_press = False
        self.keybind = "<+m"
        keyboard.add_hotkey(self.keybind, self.handle_keybind_press,)
        
        # Bind right mouse button to drag the window around 
        self.bind("<ButtonPress-3>", self.start_move)
        self.bind("<ButtonRelease-3>", self.stop_move)
        self.bind("<B3-Motion>", self.on_move)

        # self.after_id = None
##################################################################  
  

# create a frame to hold the buttons for quit and debug 
        sliderwidth =  330
        DefaultSliderValue = .7
        button_frame_debug_quit = tk.Frame(self, bg="#1E1E1E")
        button_frame_debug_quit.pack(side=tk.TOP, fill=tk.X)

        self.Opacityslider = tk.Scale(button_frame_debug_quit, from_=0.2, to=1,width=10, resolution=0.1, orient="horizontal", command=self.set_transparency, showvalue=False, bg="#1E1E1E", fg="#FFFFFF", troughcolor="#565656", highlightbackground="#1E1E1E", bd=0, length=sliderwidth)
        self.Opacityslider.set(DefaultSliderValue) # Set slider value to 1 by default
        self.Opacityslider.pack(side="right",  padx=10, pady=1)



        # Pack the window settings frame
        button_frame_debug_quit.pack(side="top", fill="x", pady=2)


####    Create frame for window setting toggle buttons 
        windowSettingsToggleButton = tk.Frame(self, bg="#1E1E1E")

        # Create CloseApp button

        self.close_button = tk.Button(windowSettingsToggleButton, text="QuitApp", command=self.CloseApp, bg="#590000", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.close_button.pack(side="right", fill="x", padx=10, pady=2)
     



        # Create and pack the toggle window mode button
        self.is_borderless = False
        self.toggle_mode_button = tk.Button(windowSettingsToggleButton, text="Window Mode", command=self.toggle_mode, bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.toggle_mode_button.pack(side="right", fill="x", padx=10, pady=2)
        
  
        # ### Hide 
        # Collapsebutton = tk.Button(windowSettingsToggleButton, text="^v", command=self.CollapseMenu, bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        # Collapsebutton.pack(side="right", fill="x", padx=4, pady=1)


        #### pack the window settings button frame m,
        windowSettingsToggleButton.pack(side="top", fill="x", pady=2)
        
        
        # Create and pack the size toggle button/side bar
        self.size_toggle = 0
        self.Sidebarbutton = tk.Button(windowSettingsToggleButton, text="Sidebar", command=self.change_window_size, width=(17),bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.Sidebarbutton.pack(side="right", fill="x", padx=4, pady=2)
        
        #### pack the window settings button frame 
        windowSettingsToggleButton.pack(side="top", fill="x", pady=2)


################################### "Enter Text" ######################################################################


       # Create and pack the canvas that displays new buttons 
        self.canvas = tk.Canvas(self, width=600, height=300, bg="gray")
        self.canvas.pack(side="right", fill="both", expand=True)
        

        # Create a frame for the buttons on the left-hand side
        button_frame = tk.Frame(self, bg="#1E1E1E")
        button_frame.pack(side="left", fill="y")

        # Create and pack the "Enter Text" label
        label = tk.Label(button_frame, text="Enter Text", bg="#1E1E1E", fg="#FFFFFF", font=("Arial", 10, "bold"))
        label.pack(side="top", padx=5, pady=5)

        # Create and pack the button name entry
        self.button_name_entry = tk.Entry(button_frame, bg="#565656", fg="#FFFFFF", highlightbackground="#1E1E1E", bd=0, font=("Arial", 10))
        self.button_name_entry.pack(side="top", fill="x", padx=10, pady=10)

        ### # Create and pack the Add button
        add_button = tk.Button(button_frame, text="Add", command=self.add_button, bg="#014214", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        add_button.pack(side="top", fill="x", padx=10, pady=10)

        # Create and pack the Delete Selected button
        delete_button = tk.Button(button_frame, text="Delete Selected", command=self.delete_selected_button, bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        delete_button.pack(side="top", fill="x", padx=10, pady=10)

        # Create save button
        save_button = tk.Button(button_frame, text="Save", command=self.save, bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        save_button.pack(side="top", fill="x", padx=10, pady=10)

        # Create load button
        load_button = tk.Button(button_frame, text="Load", command=self.load, bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        load_button.pack(side="top", fill="x", padx=10, pady=10)

        # Create and pack the Delete All button
        deleteall_button = tk.Button(button_frame, text="Delete All", command=self.deleteall_buttons, bg="#520000", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        deleteall_button.pack(side="top", fill="x", padx=10, pady=10)

        # Create saveDefault button
        save_button_Default = tk.Button(button_frame, text="Save Default", command=self.saveDefault, bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        save_button_Default.pack(side="top", fill="x", padx=10, pady=10)


        # Create loadDefault button
        load_button_Default = tk.Button(button_frame, text="Load  Default", command=self.loadDefault, bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        load_button_Default.pack(side="top", fill="x", padx=10, pady=10)



        # Create and pack the listbox for the buttons
        self.button_listbox = tk.Listbox(button_frame, bg="#565656", fg="#FFFFFF", highlightbackground="#1E1E1E", bd=0, font=("Arial", 10, "bold"))
        self.button_listbox.pack(side="left", fill="both", expand=True)


###############################################################################################
        #### Define Varibles
    
        ## updates buttons added to grid
        self.current_buttons = []

        # array to store the button names
        self.button_names = []
        ### config

        self.Pos = (20,250) ### set location for mouse to move too to execute print functions in chat 



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
############### New functions to show / hide the app 
    def ShowApp(self):
        print("ShowApp")
        self.deiconify()
        self.update_idletasks()
        self.lift()
        self.focus_force()
        self.after(0, lambda: pyautogui.moveTo(self.winfo_rootx() + self.winfo_width() / 2, self.winfo_rooty() + self.winfo_height() / 2))

        
    def handle_keybind_press(self): ## Toggle Window Visibility / Show Hide
        self.keybind_press = not self.keybind_press
        if self.keybind_press:            self.withdraw(),print("QuickChatHidden")  ### Error handled by running the hub in seporate process 
 
        else:
            self.deiconify()
            self.update_idletasks()
            self.lift()
            self.focus_force()
            print("QuickChatVisible")
            self.after(0, lambda: pyautogui.moveTo(self.winfo_rootx() + self.winfo_width() / 2, self.winfo_rooty() + self.winfo_height() / 2))
          
    def change_window_size(self):
        # Toggle between two different window sizes and move the window left or right
        MoveAmount = 150
        if self.size_toggle == 0:
            self.geometry("355x550")
            self.geometry("+{}+{}".format(self.winfo_x() + MoveAmount, self.winfo_y()))
            self.size_toggle = 1
            self.Sidebarbutton.configure(bg="#565656")
          
        else:
            self.geometry("500x550")
            self.geometry("+{}+{}".format(self.winfo_x() - MoveAmount, self.winfo_y()))
            self.size_toggle = 0
            self.Sidebarbutton.configure(bg="#0d3a63")
         

    def change_window_sizeStart(self):
        # toggle between two different window sizes and move the window left or right
        if self.size_toggle == 0:
            self.geometry("355x550")
         
            self.size_toggle = 1
        else:
            self.geometry("600x550")
           
            self.size_toggle = 0

    def CollapseMenu(self):
        
                # toggle between two different window sizes and move the window left or right
        if self.size_toggle == 0:
            self.geometry("350x550")
         # Show buttons 
            self.ToggleButtonVis(True)

            self.size_toggle = 1
        else:
            self.geometry("350x50")
        # HideButtons   
            self.ToggleButtonVis(False)

            self.size_toggle = 0

    def ToggleButtonVis(self, show):
        if show:
            self.toggle_mode_button.pack(side="right", fill="x", padx=4, pady=2)
            self.Sidebarbutton.pack(side="right", fill="x", padx=4, pady=2)
            self.Opacityslider.pack(side="top",padx=10,pady=1)
        else:
            self.toggle_mode_button.pack_forget()
            self.Sidebarbutton.pack_forget()
            self.Opacityslider.pack_forget()


    def set_transparency(self, value): # Set transparanecy value from slider
        self.attributes('-alpha', float(value))

    def toggle_mode(self):# toggle borderless mode button 
        self.is_borderless = not self.is_borderless
        if self.is_borderless:
            self.overrideredirect(True)
        else:
            self.overrideredirect(False)
        self.attributes("-topmost", 1)
###############################################################################
# #############################  Add buttons Function  (quick chat )

    #################################################################################
    def add_button(self, button_name=None, max_columns=4):
        maxentry = 40 ## define max amount of buttons
        buttonwrapleng = 80 # lentgh of wrapping text 
        buttonwidth = 8 
        buttonheight = 8
        ypad = 4
        xpad = 4
        
        
        if not button_name:
            button_name = self.button_name_entry.get()
        
        if button_name:
            if len(self.current_buttons) >= maxentry:
                print("Reached Limit of", maxentry, "entries")
                return
            
            button = tk.Button(self.canvas, text=button_name, command=lambda name=button_name: self.print_button_name(name,self.Pos),
                            bg="#F8F8F8", fg="#000000", activebackground="#014214", activeforeground="#000000",
                            relief="flat", font=("Arial", 8, "bold"), width=buttonwidth, height=buttonheight,
                            wraplength=buttonwrapleng, padx=xpad, pady=ypad)
            
            button.config(width=10, height=3) ### set the uniform size for new buttons 
            
            self.current_buttons.append(button)
            self.button_listbox.insert("end", button_name)
            
            num_buttons = len(self.current_buttons)
            rows = int(math.ceil(num_buttons / max_columns))
            cols = min(num_buttons, max_columns)
            padding = 2 ## Grid padding between butttons 
            
            # Clear existing grid
            for widget in self.canvas.grid_slaves():
                widget.grid_forget()
            
            # Rebuild grid with updated number of rows and columns
            for i, b in enumerate(self.current_buttons):
                row = i // cols
                col = i % cols
                b.grid(row=row, column=col, padx=padding, pady=padding)
            
            # Make sure the canvas resizes with the window
            self.canvas.grid_rowconfigure(rows, weight=1)
            self.canvas.grid_columnconfigure(cols, weight=1)
            self.canvas.pack(side="right")


###############################################################################
    def print_button_name(self, name,pos): ## print the name of the button pressed and type to keyboard
        def type_button_name():
            # store current mouse position
            original_pos = pyautogui.position()
            # move mouse outside of window and click the left mouse button
            pyautogui.moveTo(*pos)
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
            


  ###########################################################################################
    def load(self):   ## load buttons from text file 
        # Prompt the user to select a text file
        file_path = filedialog.askopenfilename()
        if file_path == '':
            print("User Did Not Select Load File")
            return

        self.deleteall_buttons()
        # Read the button names from the file
        with open(file_path, 'r') as f:
            button_names = f.readlines()

        # Add a button for each name read from the file
        for button_name in button_names:
            button_name = button_name.strip()  # Remove newline character from end of line
            self.add_button(button_name=button_name)  # Call add_button function with button_name argument

    def loadStart(self):   ## load buttons from text file 
        # Look for the "Default" file in the "Saves" folder
        default_file_path = os.path.join("Saves", "Default.txt")
        if not os.path.exists(default_file_path):
            print("No Default Save")
            return

        # Read the button names from the "Default" file
        with open(default_file_path, 'r') as f:
            button_names = f.readlines()

        # Add a button for each name read from the file
        for button_name in button_names:
            button_name = button_name.strip()  # Remove newline character from end of line
            self.add_button(button_name=button_name)

    def loadDefault(self):   ## load buttons from text file 
        # Look for the "Default" file in the "Saves" folder
        self.deleteall_buttons()
        default_file_path = os.path.join("Saves", "Default.txt")
        if not os.path.exists(default_file_path):
            print("No Default Save")
            return

        # Read the button names from the "Default" file
        with open(default_file_path, 'r') as f:
            button_names = f.readlines()

        # Add a button for each name read from the file
        for button_name in button_names:
            button_name = button_name.strip()  # Remove newline character from end of line
            self.add_button(button_name=button_name)

  ###########################################################################################
    def save(self):  # save buttons 
        # Prompt the user for the save file path
        file_path = filedialog.asksaveasfilename(defaultextension='.txt')
        if file_path == '':
            print("User did not save")
            return

        # Open the file for writing
        with open(file_path, 'w') as f:
            # Write each button name to a new line in the file
            for button in self.current_buttons:
                f.write(button.cget('text') + '\n')
        print('Saved current buttons to file:', file_path)
    
    def saveDefault(self):  # save buttons 
        # Save the file in the "Saves" folder with the name "Default.txt"
        save_folder = "Saves"
        os.makedirs(save_folder, exist_ok=True)
        file_path = os.path.join(save_folder, "Default.txt")

        # Open the file for writing and overwrite if it already exists
        with open(file_path, 'w') as f:
            # Write each button name to a new line in the file
            for button in self.current_buttons:
                f.write(button.cget('text') + '\n')
        print('Saved Current As Default:', file_path)
  ###########################################################################################
  ###########################################################################################

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
   
    def CloseApp(self):
          print("Close SCQuickChat")
          self.destroy()
   
   ### # def update(self):   ### IDK what this was but it was wrecking performance and not needed 
   ### #     self.after(10, self.update)
  

#####################################

app = App_SCQuickChat()

app.change_window_sizeStart() # set window size
app.toggle_mode() # set window mode borderless at start 
app.loadStart() # load config 
app.update() 
app.mainloop()
