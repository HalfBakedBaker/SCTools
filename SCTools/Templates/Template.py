# ###########SC Tool  - HalfbakedBaker & ChatGPT
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
#####
##### need to implement a function that calls the "add button" function x amount of times at the start with a empty string in order to generate 
##### blank buttons for each space in the grid 
#####



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SCTool")
        self.attributes('-topmost', 1)
        self.attributes('-alpha', 1)
        self.geometry("600x550")
        self.configure(bg="#1E1E1E")
        self.keybind_press = False
        self.keybind = "ctrl+m"
        keyboard.add_hotkey(self.keybind, self.handle_keybind_press)
         # Bind right mouse button to drag the window
        self.bind("<ButtonPress-3>", self.start_move)
        self.bind("<ButtonRelease-3>", self.stop_move)
        self.bind("<B3-Motion>", self.on_move)

  # create a frame to hold the template buttons 
        button_frame_template = tk.Frame(self, bg="#1E1E1E")
        button_frame_template.pack(side=tk.TOP, fill=tk.X)




  # create a frame to hold the buttons for quit and debug 
        button_frame_debug_quit = tk.Frame(self, bg="#1E1E1E")
        button_frame_debug_quit.pack(side=tk.TOP, fill=tk.X)


        ###  # create a templatebutton
        self.size_toggle = 0
        template_button = tk.Button(button_frame_debug_quit, text="Template", command=self.template, bg="#7a0049", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        template_button.pack(side=tk.LEFT, padx=5)


        ###  # create a debug button
        self.size_toggle = 0
        debug_button = tk.Button(button_frame_debug_quit, text="Debug", command=self.DebugToggleSize, bg="#7a0049", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        debug_button.pack(side=tk.LEFT, padx=5)
       ## # create a quit button (Requires being clicked 5 times  for safety so check click count and update)

        self.click_count = 0
        self.quit_button = tk.Button(button_frame_debug_quit, text="EXIT GAME ({})".format(self.click_count), command=self.CheckClickCount, bg="#590000", fg="#FFFFFF", activebackground="#FF3030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        self.quit_button.pack(side=tk.RIGHT, padx=5)
       ### Add a label Ctrl+m to Show Hide 

        label = tk.Label(button_frame_debug_quit, text="CTRL+M", bg="#1E1E1E", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
        label.pack(side="left", fill="x", padx=10, pady=10)
        self.slider = tk.Scale(button_frame_debug_quit, from_=0.2, to=1, resolution=0.1, orient="horizontal", command=self.set_transparency, bg="#1E1E1E", fg="#FFFFFF", troughcolor="#565656", highlightbackground="#1E1E1E", bd=0)
        self.slider.set(1) # Set slider value to 1 by default

        self.slider.pack(side="top", fill="both", padx=1)
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

    def handle_keybind_press(self): ## Toggle Window Visibility / Show Hide SCTool Ctrl + m
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

    def template_printbuttonfunction(self, name): ## print the name of the button pressed and type to keyboard
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

    def CheckClickCount(self):
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


app = App()
app.update()
app.mainloop()



