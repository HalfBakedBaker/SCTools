# #
# #
# # Implement a button on each app that can toggle its own visibility 
# # fix error emerging when you close an app and try to use hotkey 
# #
# #
# #
# ############################################,,##########################################################
# #############################################################################################################
# ## Testing ####  This will be new foundation for new build which should be much quicker and less buggy 
# print("############################## Testing ######################################")
# ########################################## Imports #######################################################

# import tkinter as tk
# import keyboard
# import pyautogui

# ######################################Create Main window # root #########################################################
# # Create the main window for App 4 "root"
# root = tk.Tk()
# root.title("App 4")
# root.deiconify()
# root.attributes('-topmost', 1)
# root.attributes('-alpha', 1)
# root.geometry("350x60")
              
# ###########################################Create windows # app1 # app2 # <>Tempalte # app3<>##################################################
# ########################################### Window 1 # app1 ##################################################

# # Create the three app windows for App 1
# app1 = tk.Toplevel(root)
# app1.title("App 1")
# ########################################### Window 2 # app2 ####################################################
# # Create the three app windows for App 2
# app2 = tk.Toplevel(root)
# app2.title("App 2")

# ##################################### <>Template For More Windows # app3<> ###########################################################
# # # Create the three app windows for App 3
# # app3 = tk.Toplevel(root)
# # app3.title("App 3")

# ###################################### define functions for windows ###########################################################

# # Define the function for printing "Hello World"
# def print_hello():
#     print("Hello World")


# ################################# Buttons for windows ################################################################

# # Create a button for each app window that prints "Hello World"
# app1_button = tk.Button(app1, text="Print Hello World", command=print_hello)
# app1_button.pack()

# #################################################################################################
# app2_button = tk.Button(app2, text="Print Hello World", command=print_hello)
# app2_button.pack()

# ###################################### Template Button # PrintHelloWorld ##########################################################
# # app3_button = tk.Button(app3, text="Print Hello World", command=print_hello)
# # app3_button.pck()


# ####################################### Define functions for root ##########################################################


# def toggle_visibility(app):     #### Toggle Vis Hotkey is the function that "app" is replaced with appx in the toggle vis hotkey function 
#     app_state = app.state()

#     if app_state == "withdrawn":
#         app.deiconify()
#         app.attributes('-topmost', 1)

        
#     else:
#         app.withdraw()
# ###################################### Buttons for Main Windw###########################################################

# # Create three buttons in App 4 for toggling visibility of the app windows
# toggle_button1 = tk.Button(root, text="Toggle App 1", command=lambda: toggle_visibility(app1))
# toggle_button1.pack(side="left")

# toggle_button2 = tk.Button(root, text="Toggle App 2", command=lambda: toggle_visibility(app2))
# toggle_button2.pack(side="left")

# toggle_button3 = tk.Button(root, text="PrintHelloTest", command=lambda: print_hello())
# toggle_button3.pack(side="left")
# ####################################### Functions for main window #########################################################

# ####################################### Toggle Visibility Function Hotkey "<" # Toggle app1 app2 #########################################################

# def toggle_visibility_hotkey():
#     # toggle_visibility(app1)  # Default to moving mouse to app2
#     toggle_visibility(app2)  # Default to moving mouse to app2
#     # toggle_visibility(app3)  # Default to moving mouse to app2
#     pyautogui.moveTo(app2.winfo_x() + app2.winfo_width() / 2, app2.winfo_y() + app2.winfo_height() / 2)  # Move mouse to app2
    
    
# #################################### keyboard listener for hotkey #############################################################

# keyboard.add_hotkey("<", toggle_visibility_hotkey)

# #################################################################################################


# ######################################### Start the main loop #########################################################
# root.mainloop()















# #################################################################################################
# #################################################################################################
# #################################################################################################
# # 
# # # import tkinter as tk
# # 
# # 
# # # class OverlayApp(tk.Tk):
# # #     def __init__(self):
# # #         super().__init__()
# #         
# # #         # Set the window to be borderless and fullscreen
# # #         # self.overrideredirect(True)
# # #         self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
# #         
# # #         # Make the window 50% transparent
# # #         self.attributes("-alpha", 1)
# # #         self.attributes("-topmost", 1)
# # #         # self.attributes("-topmost", 1)
# # #         # self.geometry("400x300")
# # 
# # #         # Add a slider to adjust the transparency
# # #         self.slider = tk.Scale(self, from_=0.0, to=1.0, resolution=0.01, orient=tk.HORIZONTAL, command=self.set_opacity)
# # #         self.slider.set(0.5)
# # #         self.slider.pack(side=tk.TOP, fill=tk.X)
# #         
# # #         # Add frames for buttons#
# #         
# # #         WindowFrame = tk.Frame(self, bd=2, relief=tk.GROOVE, bg="#ab34eb")
# # #         WindowFrame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
# #    
# # #         WindowFrame.pack(fill="both",expand=True)
# #         
# # 
# # #         button_frame1 = tk.Frame(self, bd=2, relief=tk.GROOVE)
# # #         button_frame1.place(relx=0.5, rely=1.0, anchor=tk.S)
# # #         button_frame2 = tk.Frame(self, bd=2, relief=tk.GROOVE)
# # #         button_frame2.place(relx=0.0, rely=0.5, anchor=tk.W)
# # #         button_frame3 = tk.Frame(self, bd=2, relief=tk.GROOVE)
# # #         button_frame3.place(relx=1.0, rely=0.5, anchor=tk.E)
# #             
# # 
# # 
# # 
# # 
# # 
# # #         # Add buttons to the frames
# # #         button1 = tk.Button(button_frame1, text="Hello, world!", command=lambda: print("Hello, world!"))
# # #         button1.pack()
# # #         button2 = tk.Button(button_frame2, text="Hello, world!", command=lambda: print("Hello, world!"))
# # #         button2.pack()
# # #         button3 = tk.Button(button_frame3, text="Hello, world!", command=lambda: print("Hello, world!"))
# # #         button3.pack()
# #         
# # 
# # 
# # #     def set_opacity(self, value):
# # #         self.attributes("-alpha", float(value))
# # 
# # 
# # 
# # #     def on_click(self, event):
# # #         x, y = event.x, event.y
# # #         widget = self.winfo_containing(x, y)
# # #         if widget == self:
# # #             self.lower()
# # #         else:
# # #             widget.event_generate("<Button-1>", x=x, y=y)
# # 
# # # if __name__ == "__main__":
# # #     app = OverlayApp()
# # #     app.mainloop()
# # # #
# #################################################################################################
# #######################################Version using "Visual TK ##########################################################
###       http://www.python-gui-builder.com/index.html
###       https://visualtk.com/
# #################################################################################################

########################################################################################







# #################################################################################################