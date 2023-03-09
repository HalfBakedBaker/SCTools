######## Tempalte For new Style GUI Using Tkinter ####### 
################################################################################################################################################################################################################################
################################################################################################################################################################################################################################
################################################################################################################################################################################################################################





## # modern format style template 


## Template for Modern Style ########

## imports 

import TKinterModernThemes as TKMT
import tkinter as tk
from TKinterModernThemes.WidgetFrame import Widget
from tkinter import ttk

## def functions to be called by the application

def buttonCMD():
        print("Button clicked!")



#### def application class #######

class App(TKMT.ThemedTKinterFrame):
        def __init__(self, theme, mode, usecommandlineargs=True, usethemeconfigfile=True):
                super().__init__(str("TITLE"), theme, mode, usecommandlineargs, usethemeconfigfile)

                # self.Button(str("Auto placed button!"), buttonCMD)  # placed at row 0, col 0

                self.button_frame = self.addLabelFrame(str("Frame Label"))  # placed at row 1, col 0
                self.button_frame.Button(str("Button Text"), buttonCMD)  # the button is dropped straight into the frame
                button = ttk.Button(self.button_frame.master, text="Button in frame!")
                button.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')


                ## switch example in a frame 
                self.switchframe = self.addLabelFrame(str("Switch Frame"))
                self.switchvar = tk.BooleanVar()
                self.switchframe.SlideSwitch("Switch", self.switchvar)



                ## toggle button 
                self.togglebuttonframe = self.addLabelFrame(str("Toggle Button Frame"))
                self.togglebuttonvar = tk.BooleanVar()
                self.togglebutton = self.togglebuttonframe.ToggleButton(text="Toggle button",variable=self.togglebuttonvar)
                

                self.debugPrint()  ## print debug application
                self.run() ## run application 

### run application ####
if __name__ == "__main__":
        App(str("park"), str("dark"))







###################################################################################################################################################################################################################################################



###################################################################################################################################################################################################################################################


###################################################################################################################################################################################################################################################



























################################################################################################################################################################################################################################