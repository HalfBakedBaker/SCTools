# ###########SC Tool  
# ###################################################



import pyautogui

import tkinter as tk

import keyboard

import time

class App_SCTool(tk.Tk):
    def __init__(self):  # Add the app window wim,m,th buttons and sliders 
        super().__init__()
        self.title("SCTool")
        self.attributes('-topmost', 1)
        self.attributes('-alpha', 1)
        self.geometry("1400x30")

        # Get screen width and height,
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate x and y coordinates for the window
        x = int(screen_width/2 - 600) # 375 is half of the window width
        y = screen_height - 30 # 90 is the window height

        # Set the window position
        self.geometry("1075x30+{}+{}".format(x, y))

        self.configure(bg="#1E1E1E")


        
        # Bind right mouse button to drag the window
        self.bind("<ButtonPress-3>", self.start_move)
        self.bind("<ButtonRelease-3>", self.stop_move)
        self.bind("<B3-Motion>", self.on_move)
        #### Keybind For show/hide app
        self.keybind_press = False
        self.keybind = "<+m"
        keyboard.add_hotkey(self.keybind, self.handle_keybind_press)

        self.after_id = None

# ####################################################################################################

  # create a frame to hold the template buttons 
        WindowFrameSettings = tk.Frame(self, bg="#1E1E1E")
        WindowFrameSettings.pack(side=tk.TOP, fill=tk.X)


  # create a frame to hold the buttons for F1 F2 (Mobiglass and camera )
        WindowFrameSettings = tk.Frame(self, bg="#1E1E1E")
        WindowFrameSettings.pack(side=tk.TOP, fill=tk.X)


       ## # create a quit button for the app
      
        CloseApp = tk.Button(WindowFrameSettings, text="QuitApp", command=self.CloseApp, bg="#590000", fg="#FFFFFF", activebackground="#FF3030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        CloseApp.pack(side="right", padx=5)





       ## # create a quit button (Requires being clicked 5 times  for safety so check click count and update)
        self.click_count = 0
        self.quit_button = tk.Button(WindowFrameSettings, text="EXIT GAME ({})".format(self.click_count), command=self.CheckClickCount, bg="#590000", fg="#FFFFFF", activebackground="#FF3030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.quit_button.pack(side="right", padx=5)



        # Create and pack the toggle window mode button
        self.is_borderless = False
        self.toggle_mode_button = tk.Button(WindowFrameSettings, text="Window Mode", command=self.toggle_mode, bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.toggle_mode_button.pack(side="right", fill="x", padx=4, pady=2)
        
        
 
        # Create and pack the toggle Hide Button
        self.is_borderless = False
        self.toggle_mode_button = tk.Button(WindowFrameSettings, text="Hide - '<+m'", command=self.handle_keybind_press, bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.toggle_mode_button.pack(side="right", fill="x", padx=4, pady=2)
        
       
        ###Slider 
        DefaultSliderValue = .7
        self.slider = tk.Scale(WindowFrameSettings, from_=0.2, to=1, resolution=0.1,width=10, orient="horizontal", command=self.set_transparency,showvalue=False, bg="#1E1E1E", fg="#FFFFFF", troughcolor="#565656", highlightbackground="#1E1E1E", bd=0, length=100)
        self.slider.set(DefaultSliderValue) # Set slider value to 1 by default
        self.slider.pack(side="right", fill="x", padx=1)

        # create the debug buttons
        debug_names = ["debug 0", "debug 1", "debug 2", "debug 3", "debug 4", "Session 1", "Session 0", "Screenshot"]
        debug_commands = ["r_displayinfo 0", "r_displayinfo 1", "r_displayinfo 2", "r_displayinfo 3", "r_displayinfo 4", "r_displaySessionInfo 1", "r_displaySessionInfo 0", "r_getScreenShot 1"]
        for name, command in zip(debug_names, debug_commands):
            debug_button = tk.Button(WindowFrameSettings, text=name, command=lambda cmd=command: self.DebugButtons(cmd), bg="#922178", fg="#FFFFFF", activebackground="#922178", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
            debug_button.pack(side=tk.RIGHT, padx=5)



# Pack the window settings frame
        WindowFrameSettings.pack(side="top", fill="x", pady=5)
#########################################################################

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

    def CloseApp(self):
        print("CloseAppSCTool")
        self.destroy()

## Is Called when Ctrl + M is pressed  ( will replace with M + RMB )

    def handle_keybind_press(self): ## Toggle Window Visibility / Show Hide SCTool Ctrl + m
        self.keybind_press = not self.keybind_press
        if self.keybind_press:  
            self.withdraw(),print("SCToolHidden")  ### Error handled by running the hub in seporate process 
        else:
            self.deiconify()
            self.update_idletasks()
            self.lift()
            self.focus_force()
            print("SCToolVisible") 
            # self.after(0, lambda: pyautogui.moveTo(self.winfo_rootx() + self.winfo_width() / 2, self.winfo_rooty() + self.winfo_height() / 2))

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
         pyautogui.moveTo(20, 250)
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
            pyautogui.moveTo(20,250)
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
            pyautogui.moveTo(20, 250)
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
            pyautogui.moveTo(20, 250)
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
            pyautogui.moveTo(20, 250)
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
            pyautogui.moveTo(20,250)
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
            pyautogui.moveTo(20,250)
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


    def CheckClickCount(self):  ## allows quit button to be activated after 3 clicks
        if self.click_count < 3:
            self.click_count += 1
            self.quit_button.config(text="EXIT GAME ({})".format(3 - self.click_count))
        else:
            self.QuitGame()
            self.click_count = 0

    def QuitGame(self):
            self.print_button_quit(name="quit")
    
    def template(self):
            self.template_printbuttonfunction(name="Template = mouse move To (500,50) ,click, 'enter', type>Template, 'enter', returnmouse")
      
    # def update(self):  # Not needed 
    #     self.after(10, self.update)
   
app = App_SCTool()

app.toggle_mode()
app.update()
app.mainloop()







   




































#############################################################################################
#############################################################################################