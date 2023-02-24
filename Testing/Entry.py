



#############################################################################################################
## Testing ####  This will be new foundation for new build which should be much quicker and less buggy 
print("############################## Testing ######################################")
########################################## Imports #######################################################

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





######################################Create Main window # root #########################################################
# Create the main window for App 4 "root"
root = tk.Tk()
root.title("root")
root.attributes('-topmost',1)
root.attributes('-alpha',1)
root.geometry("500x250")
############################################### setup # Main Window########################################################################
# Bind right mouse button to drag the window
# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()        
# Calculate the x and y position for the window
x = int((screen_width - 1050) / 2) # Center the window horizontally
y = 1 # Place the window at the top of the screen
# Set the window position
root.geometry("1150x150+{}+{}".format(x, y))

###########################################Create windows # app1 # app2 # <>Tempalte # app3<>##################################################
########################################### Window 1 # app1 ##################################################
# Create the three app windows for App 1
app1 = tk.Toplevel(root)
app1.title("App 1")
app1.is_borderless = False
app1.attributes('-topmost',1)
app1.attributes('-alpha',1)
app1.geometry("1080x25"),
############################################### setup # app 1 ########################################################################
# Bind right mouse button to drag the window
# Get the screen width and height
screen_width = app1.winfo_screenwidth()
screen_height = app1.winfo_screenheight()        
# Calculate the x and y position for the window
x = int((screen_width - 1050) / 2) # Center the window horizontally
y = 200 # Place the window at the top of the screen
# Set the window position
app1.geometry("1150x25+{}+{}".format(x, y))
########################################### Window 1 # app1 ##################################################



########################################### Window 2 # app2 ####################################################
# Create the three app windows for App 2
app2 = tk.Toplevel(root)
app2.is_borderless = False
app2.title("App 2")
app2.attributes('-topmost',1)
app2.attributes('-alpha',1)
app2.geometry("1080x25")
############################################### setup # app 2 ########################################################################
# Bind right mouse button to drag the window
# Get the screen width and height
screen_width = app2.winfo_screenwidth()
screen_height = app2.winfo_screenheight()        
# Calculate the x and y position for the window
x = int((screen_width - 1050) / 2) # Center the window horizontally
y =300 # Place the window at the top of the screen
# Set the window position
app2.geometry("1150x25+{}+{}".format(x, y))
########################################### Window 2 # app2 ####################################################



##################################### <>Template For More Windows # app3<> ###########################################################
# # Create the three app windows for App 3
# app3 = tk.Toplevel(root)
# app3.title("App 3")
###################################### define functions for windows ###########################################################
# Define the function for printing "Hello World"
def print_hello():
    print("Hello World")

################################# Buttons for windows ################################################################
# Create a button for each app window that prints "Hello World"
app1_button = tk.Button(app1, text="Print Hello World", command=print_hello)
app1_button.pack()
#################################################################################################
app2_button = tk.Button(app2, text="Print Hello World", command=print_hello)
app2_button.pack()
###################################### Template Button # PrintHelloWorld ##########################################################
# app3_button = tk.Button(app3, text="Print Hello World", command=print_hello)
# app3_button.pack()
####################################### Define functions for root ##########################################################
###################################### Bindings for window movement ###########################################################
def start_move(event):
    root.x = event.x
    root.y = event.y
def stop_move(event):
    root.x = None
    root.y = None
def on_move(event):
    deltax = event.x - root.x
    deltay = event.y - root.y
    x = root.winfo_x() + deltax
    y = root.winfo_y() + deltay
    root.geometry(f"+{x}+{y}")

root.bind("<ButtonPress-3>", start_move)
root.bind("<ButtonRelease-3>", stop_move)
root.bind("<B3-Motion>", on_move)

def start_move_app1(event):
    app1.x = event.x
    app1.y = event.y
def stop_move_app1(event):
    app1.x = None
    app1.y = None
def on_move_app1(event):
    deltay = event.y - app1.y
    deltax = event.x - app1.x
    x = app1.winfo_x() + deltax
    y = app1.winfo_y() + deltay
    app1.geometry(f"+{x}+{y}")

app1.bind("<ButtonPress-3>", start_move_app1)
app1.bind("<ButtonRelease-3>", stop_move_app1)
app1.bind("<B3-Motion>", on_move_app1)

def start_move_app2(event):
    app2.x = event.x
    app2.y = event.y
def stop_move_app2(event):
    app2.x = None
    app2.y = None
def on_move_app2(event):
    deltay = event.y - app2.y
    deltax = event.x - app2.x
    x = app2.winfo_x() + deltax
    y = app2.winfo_y() + deltay
    app2.geometry(f"+{x}+{y}")

app2.bind("<ButtonPress-3>", start_move_app2)
app2.bind("<ButtonRelease-3>", stop_move_app2)
app2.bind("<B3-Motion>", on_move_app2)










###################################### toggle window visibility  ###########################################################
def toggle_visibility(app):
    app_state = app.state()

    if app_state == "withdrawn":
        app.deiconify()
        
    else:
        app.withdraw()
#################################################################################################

###################################### toggle borderless###########################################################
def toggle_WindowMode(app):
    print("ToggleWindowModeOnAllWindows")
  


###################################### Buttons for Main Windw###########################################################

# Create three buttons in App 4 for toggling visibility of the app windows
toggle_button1 = tk.Button(root, text="Toggle App 1", command=lambda: toggle_visibility(app1))
toggle_button1.pack()

toggle_button2 = tk.Button(root, text="Toggle App 2", command=lambda: toggle_visibility(app2))
toggle_button2.pack()

window_mode_button = tk.Button(root, text="Toggle_WindowMode", command=lambda: toggle_WindowMode(root))
window_mode_button.pack()



# window_mode_buttonTest = tk.Button(root, text="PrintHelloTest", command=lambda: toggle_WindowMode(root))
# window_mode_buttonTest.pack()
######################################### Functions for main window #########################################################

####################################### Toggle Visibility Function Hotkey "<" # Toggle app1 app2 #########################################################

def toggle_visibility_hotkey():
    toggle_visibility(app1)  # Default to moving mouse to app2
    toggle_visibility(app2)  # Default to moving mouse to app2
    # toggle_visibility(app3)  # Default to moving mouse to app2
    pyautogui.moveTo(app2.winfo_x() + app2.winfo_width() / 2, app2.winfo_y() + app2.winfo_height() / 2)  # Move mouse to app2
    
    
#################################### keyboard listener for hotkey #############################################################

keyboard.add_hotkey("<", toggle_visibility_hotkey)

#################################################################################################
#################################################################################################


######################################### Start the main loop #########################################################
root.mainloop()