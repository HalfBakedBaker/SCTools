




# ####################################################################################################
# #
# #                           Much Better Example for a "HUB" Template 
# #
# ##
# ####################################################################################################
import tkinter as tk
import time 
import keyboard 
import pyautogui

############################################## Main App ###############################################
class Application:
   def __init__(self):
       # Create 3 top-level windows
       self.root1 = tk.Tk()
       self.root2 = tk.Tk()
       self.root3 = tk.Tk()
     
       self.recording = False
       self.recorded_position = None
       # Set window properties
       for root in [self.root1, self.root2, self.root3]:
           root.overrideredirect(False)  ## Window / borderless mode 
           root.geometry("+0+0")
           root.wm_attributes("-topmost", 1)
           root.config(bg="#282828")
           root.attributes("-alpha", 0.7)
       self.root1.title("Hub")
       self.root2.title("App2")
       self.root3.title("App2")
       # Create buttons for each window
       self.button_colors = ["blue", "green", "yellow", "orange", "red"]
       # Functions for bulk buttons 
       self.functions = [self.Print1, self.Print2, self.Print3, self.Print4, self.Print5]
       self.create_buttons()
       self.root = root
     
       # Add toggle buttons to window 1
       self.toggle_button2 = tk.Button(self.root1, text="MacroBase", bg="#383838", fg="white", command=self.MacroBase)
       self.toggle_button2.pack(side="left", padx=5, pady=5)

       self.toggle_button2 = tk.Button(self.root1, text="PlayMouse", bg="#383838", fg="white", command=self.play_position)
       self.toggle_button2.pack(side="left", padx=5, pady=5)

       self.toggle_button2 = tk.Button(self.root1, text="RecordMousePos", bg="#383838", fg="white", command=self.record_position)
       self.toggle_button2.pack(side="left", padx=5, pady=5)

       self.toggle_button2 = tk.Button(self.root1, text="Show/Hide Window 2", bg="#383838", fg="white", command=self.toggle_visibility2)
       self.toggle_button2.pack(side="left", padx=5, pady=5)

       self.toggle_button3 = tk.Button(self.root1, text="Show/Hide Window 3", bg="#383838", fg="white", command=self.toggle_visibility3)
       self.toggle_button3.pack(side="left", padx=5, pady=5)

       self.toggle_window = tk.Button(self.root1, text="Window/Borderless", bg="#383838", fg="white", command=self.toggle_mode)
       self.toggle_window.pack(side="left", padx=5, pady=5)

       self.toggle_window = tk.Button(self.root1, text="Quit", bg="red", fg="white", command=self.QuitApp)
       self.toggle_window.pack(side="left", padx=5, pady=5)

       # Start mainloop
       self.is_borderless = False
       self.root1.mainloop()
  ################################################## Global Buttons ###################################
   def create_buttons(self): # bulk button maker
       ButtonCount = 5   # Define how many buttons to add to each root Makes x amount of buttons for each window Functions are assigned above 
       for i in range(ButtonCount):
           # root 1 buttons 
           button = tk.Button(self.root1, text="Button {}".format(i+1), bg="#383838", fg="white", activebackground=self.button_colors[i], command=self.functions[i])
           button.pack(side="left", padx=5, pady=5)
           # root 2
           button = tk.Button(self.root2, text="Button {}".format(i+1), bg="#383838", fg="white", activebackground=self.button_colors[i], command=self.functions[i])
           button.pack(side="left", padx=5, pady=5)
           # root 3
           button = tk.Button(self.root3, text="Button {}".format(i+1), bg="#383838", fg="white", activebackground=self.button_colors[i], command=self.functions[i])
           button.pack(side="left", padx=5, pady=5)    
############################################# Functions Main App ######################################
   def toggle_mode(self):
       # Check current mode of windows
       current_mode = self.root1.overrideredirect()
       # Toggle mode for all windows
       self.root1.overrideredirect(not current_mode)
       self.root2.overrideredirect(not current_mode)
       self.root3.overrideredirect(not current_mode)
   def QuitApp(self):
       try:
           self.root1.destroy()
       except tk.TclError:
           pass
       try:
           self.root2.destroy()
       except tk.TclError:
           pass
       try:
           self.root3.destroy()
       except tk.TclError:
           pass
   def record_position(self):
       self.recording = True
       t = 3
       for i in range(t, 0, -1):
           print(i)
           time.sleep(1)
       self.recorded_position = self.root.winfo_pointerxy()
       print("Recorded position:", self.recorded_position)
       self.recording = False
   def play_position(self):
       if self.recorded_position is not None:
           x, y = self.recorded_position
           original_pos = pyautogui.position()
           pyautogui.moveTo(x,y)
           pyautogui.click(button='left')
           # add a delay of 0.1 second
           time.sleep(0.1)
           # move mouse back to original position
           pyautogui.moveTo(original_pos)
       else:
           print("No recorded position found")       
   def MacroBase(self):
       if self.recorded_position is not None:
           x, y = self.recorded_position
           original_pos = pyautogui.position()
           name = 'hello' # thing that is typed out after mouse has focused on chosen location 
           PR1 = 'enter' # key that is pressed then released before the typrewrite 
           PR2 = 'emter' #key that is pressed then released after the typrwrite 
           # location mouse returns to after completing the action 
           pyautogui.moveTo(x,y)
           # left click to focus on window 
           pyautogui.click(button='left')
           # Press Release Button 1 
           keyboard.press_and_release(PR1)
           # typewite something 
           pyautogui.typewrite(name)
           # Press Release Button 1 
           keyboard.press_and_release(PR2)
           # move mouse back to original position
           pyautogui.moveTo(original_pos)
       else:
           print("No recorded position found")
   def toggle_visibility2(self):
       if self.root2.winfo_viewable():
           self.root2.withdraw()
       else:
           self.root2.deiconify()
   def toggle_visibility3(self):
       if self.root3.winfo_viewable():
           self.root3.withdraw()
       else:
           self.root3.deiconify()
#######################################################################################################
################################# Global Functions all windows can call################################
   def Print1(self):
       print("Button 1 was clicked.")
 
   def Print2(self):
       print("Button 2 was clicked.")
 
   def Print3(self):
       print("Button 3 was clicked.")
 
   def Print4(self):
       print("Button 4 was clicked.")
 
   def Print5(self):
       print("Button 5 was clicked.")
app=Application()
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
###########SC Tool  - HalfbakedBaker & ChatGPT
###################################################
## 
## 
## 
## 
## 
# ## 
# import tkinter.filedialog as filedialog
# import pyautogui
# import math
# import tkinter as tk
# import keyboard
# import time 
# ### 
# ### need to implement a function that calls the "add button" function x amount of times at the start with a empty string in order to generate 
# ### blank buttons for each space in the grid 
# ###
# class App(tk.Tk):
#      def __init__(self): # Create main window 
#          super().__init__()
#          self.title("SCTool")
#          self.attributes('-topmost', 1)
#          self.attributes('-alpha', 1)
#          self.geometry("600x550")
#          self.configure(bg="#1E1E1E")
#          self.keybind_press = False
#          self.keybind = "ctrl+m"
#          keyboard.add_hotkey(self.keybind, self.handle_keybind_press)
#           # Bind right mouse button to drag the window
#          self.bind("<ButtonPress-3>", self.start_move)
#          self.bind("<ButtonRelease-3>", self.stop_move)
#          self.bind("<B3-Motion>", self.on_move)

#    # create a frame to hold the template buttons 
#          button_frame_template = tk.Frame(self, bg="#1E1E1E")
#          button_frame_template.pack(side=tk.TOP, fill=tk.X)




#    # create a frame to hold the buttons for quit and debug 
#          button_frame_debug_quit = tk.Frame(self, bg="#1E1E1E")
#          button_frame_debug_quit.pack(side=tk.TOP, fill=tk.X)


#          ###  # create a templatebutton
#          self.size_toggle = 0
#          template_button = tk.Button(button_frame_debug_quit, text="Template", command=self.template, bg="#7a0049", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
#          template_button.pack(side=tk.LEFT, padx=5)


#          ###  # create a debug button
#          self.size_toggle = 0
#          debug_button = tk.Button(button_frame_debug_quit, text="Debug", command=self.DebugToggleSize, bg="#7a0049", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
#          debug_button.pack(side=tk.LEFT, padx=5)
#         ## # create a quit button (Requires being clicked 5 times  for safety so check click count and update)

#          self.click_count = 0
#          self.quit_button = tk.Button(button_frame_debug_quit, text="EXIT GAME ({})".format(self.click_count), command=self.CheckClickCount, bg="#590000", fg="#FFFFFF", activebackground="#FF3030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
#          self.quit_button.pack(side=tk.RIGHT, padx=5)
#         ### Add a label Ctrl+m to Show Hide 

#          label = tk.Label(button_frame_debug_quit, text="CTRL+M", bg="#1E1E1E", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
#          label.pack(side="left", fill="x", padx=10, pady=10)
#          self.slider = tk.Scale(button_frame_debug_quit, from_=0.2, to=1, resolution=0.1, orient="horizontal", command=self.set_transparency, bg="#1E1E1E", fg="#FFFFFF", troughcolor="#565656", highlightbackground="#1E1E1E", bd=0)
#          self.slider.set(1) # Set slider value to 1 by default

#          self.slider.pack(side="top", fill="both", padx=1)
#  # Pack the window settings frame

#          button_frame_debug_quit.pack(side="top", fill="x", pady=5)


#  ####    Create frame for window setting toggle buttons 
#          windowSettingsToggleButton = tk.Frame(self, bg="#1E1E1E")

#          # Create and pack the toggle window mode button
#          self.is_borderless = False
#          self.toggle_mode_button = tk.Button(windowSettingsToggleButton, text="Toggle Window Mode", command=self.toggle_mode, bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
#          self.toggle_mode_button.pack(side="left", fill="x", padx=1, pady=1)

#          # Create and pack the size toggle button/ side bar
#          self.size_toggle = 0
#          button = tk.Button(windowSettingsToggleButton, text="Toggle Sidebar", command=self.change_window_size, bg="#565656", fg="#FFFFFF", activebackground="#303030", activeforeground="#FFFFFF", relief="flat", bd=0, font=("Arial", 10, "bold"))
#          button.pack(side="right", fill="x", padx=1, pady=1)

#   #### pack the window settings button frame 
#          windowSettingsToggleButton.pack(side="top", fill="x", pady=5)

#  ### functions to allow movemet of window when in borderless mode 
#      def start_move(self, event):
#          self.x = event.x
#          self.y = event.y
#      def stop_move(self, event):
#          self.x = None
#          self.y = None
#      def on_move(self, event):
#          deltax = event.x - self.x
#          deltay = event.y - self.y
#          x = self.winfo_x() + deltax
#          y = self.winfo_y() + deltay
#          self.geometry(f"+{x}+{y}")
 

#      def handle_keybind_press(self): ## Toggle Window Visibility / Show Hide SCTool Ctrl + m
#          self.keybind_press = not self.keybind_press
#          if self.keybind_press:
#              self.withdraw()
#              x, y = self.winfo_rootx() + self.winfo_width() // 2, self.winfo_rooty() + self.winfo_height() // 2
#          else:
#              self.deiconify()
#              self.update_idletasks()
#              self.lift()
#              self.focus_force()
#              self.after(0, lambda: pyautogui.moveTo(self.winfo_rootx() + self.winfo_width() / 2, self.winfo_rooty() + self.winfo_height() / 2))

#      def change_window_size(self): ## Toggle window size button
#          # button_name = ""
#          # toggle between two different window sizes
#          if self.size_toggle == 0:
#              self.geometry("470x450")
#              self.size_toggle = 1
#              ################################
#          else:
#              self.geometry("600x550")
#              self.size_toggle = 0

#      def set_transparency(self, value): # Set transparanecy value from slider
#          self.attributes('-alpha', float(value))

#      def toggle_mode(self):# toggle Window mode button 
#          self.is_borderless = not self.is_borderless
#          if self.is_borderless:
#              self.overrideredirect(True)
#          else:
#              self.overrideredirect(False)
#          self.attributes("-topmost", 1)

#      def template_printbuttonfunction(self, name): ## print the name of the button pressed and type to keyboard
#          def type_button_name():
#              # store current mouse position
#              original_pos = pyautogui.position()
#              # move mouse outside of window and click the left mouse button
#              pyautogui.moveTo(500,50)
#              pyautogui.click(button='left')
#              # press enter
#              keyboard.press_and_release('enter')
#              # add a delay of 1 second
#              time.sleep(0.02)
#              # type out the name of the button (type out the letters)
#              pyautogui.typewrite(name)
#              # add a delay of 1 second
#              time.sleep(0.02)
#              keyboard.press_and_release('enter')
#              # move mouse back to original position
#              pyautogui.moveTo(original_pos)

#          self.after(1, type_button_name)
  
#      def template(self):
#              self.template_printbuttonfunction(name="Template = mouse move To (500,50) ,click, 'enter', type>Template, 'enter', returnmouse")

#      def print_button_debug(self, name): ## Enables Debugging in SC 
#          def print_button_debug():
#              # store current mouse position
#              original_pos = pyautogui.position()
#              # move mouse outside of window and click the left mouse button
#              pyautogui.moveTo(500,50)
#              pyautogui.click(button='left')
#              # press ``
#              keyboard.press_and_release('`')
#              # add a delay of 1 second
#              time.sleep(0.02)
#              # type out the name of the button (type out the letters)
#              pyautogui.typewrite(name)
#              # add a delay of 1 second
#              time.sleep(0.02)
#              keyboard.press_and_release('enter')
#              # add a delay of 1 second
#              time.sleep(0.02)
#              # press ``
#              keyboard.press_and_release('`')
#              # move mouse back to original position
#              pyautogui.moveTo(original_pos)

#          self.after(1, print_button_debug)

#      def print_button_quit(self,name): ## Quickly Quits the game after 5 clicks6
#      # 
#          def print_button_quit():
#            # store current mouse position
#              original_pos = pyautogui.position()
#              # move mouse outside of window and click the left mouse button
#              pyautogui.moveTo(500,50)
#              pyautogui.click(button='left')
#              # press ``
#              keyboard.press_and_release('`')
#              # add a delay of 1 second
#              time.sleep(0.02)
#              # type out the name of the button (type out the letters)
#              pyautogui.typewrite(name)
#              # add a delay of 1 second
#              time.sleep(0.02)
#              keyboard.press_and_release('enter')
#              # move mouse back to original position           
#              pyautogui.moveTo(original_pos)
#          self.after(1, print_button_quit)

#      def DebugToggleSize(self):
#          if hasattr(self, 'hello_printed') and self.hello_printed:
#              # print("Goodbye")
#              # self.template_printbuttonfunction(name="r_displayinfo 0")
#              self.print_button_debug(name="r_displayinfo 0")
#              self.hello_printed = False
#          else:
#              # print("Hello")
#              # self.template_printbuttonfunction(name="r_displayinfo 4")
#              self.print_button_debug(name="r_displayinfo 4")
#              self.hello_printed = True

#      def CheckClickCount(self):
#          if self.click_count < 4:
#              self.click_count += 1
#              self.quit_button.config(text="EXIT GAME ({})".format(5 - self.click_count))
#          else:
#              self.QuitGame()
#              self.click_count = 0

#      def QuitGame(self):

#              self.print_button_quit(name="quit")
  
#      def update(self):
#          self.after(10, self.update)


#  # 

# app = App()
# app.update()
# app.mainloop()
# # 
# # ###################################################################################################################################################################################################################

# ####################import tkinter as tk
# import time
# import tkinter as tk
# import pyautogui

# class MouseRecorder:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Mouse Recorder")
#         self.root.geometry("500x500")
#         self.root.attributes("-topmost", True)
#         self.recording = False
#         self.recorded_position = None

#         record_button = tk.Button(self.root, text="Record", command=self.record_position)
#         record_button.pack(side=tk.LEFT, padx=10)

#         play_button = tk.Button(self.root, text="Play", command=self.play_position)
#         play_button.pack(side=tk.LEFT)

#     def record_position(self):
#         self.recording = True
#         for i in range(5, 0, -1):
#             print(i)
#             time.sleep(1)
#         self.recorded_position = self.root.winfo_pointerxy()
#         print("Recorded position:", self.recorded_position)
#         self.recording = False

#     def play_position(self):
#         if self.recorded_position is not None:
#             x, y = self.recorded_position
#             pyautogui.moveTo(x,y)
#             pyautogui.click(button='left')
#         else:
#             print("No recorded position found")


# root = tk.Tk()
# mouse_recorder = MouseRecorder(root)
# root.mainloop()

# ############################################# Record mouse location, Use to set location x for mouse to move to for the print commands inside the main apps ## move location x and click then type y ####################################################################################################################################################################
# #######################################################################################################################################################################################################################################
# import time
# import tkinter as tk
# import pyautogui

# class MouseRecorder:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Mouse Recorder")
#         self.root.geometry("500x500")
#         self.root.attributes("-topmost", True)
#         self.recording = False
#         self.recorded_position = None

#         self.record_button = tk.Button(self.root, text="Record", command=self.record_position)
#         self.record_button.pack(side=tk.LEFT, padx=10)

#         play_button = tk.Button(self.root, text="Play", command=self.play_position)
#         play_button.pack(side=tk.LEFT)

#     def record_position(self):
#         self.recording = True
#         for i in range(5, 0, -1):
#             print(i)
#             self.record_button.config(text=f"Record ({i}s)")
#             time.sleep(1)
#         self.record_button.config(text="Record")
#         self.recorded_position = self.root.winfo_pointerxy()
#         print("Recorded position:", self.recorded_position)
#         self.recording = False

#     def play_position(self):
#         if self.recorded_position is not None:
#             x, y = self.recorded_position
#             pyautogui.moveTo(x,y)
#             pyautogui.click(button='left')
#         else:
#             print("No recorded position found")


# root = tk.Tk()
# mouse_recorder = MouseRecorder(root)
# root.mainloop()
#############################################################################
