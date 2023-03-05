####################################################### Template 2 ############################################################################################################################################################
#################################### Mouse Recorder ###############################################################################################################################################################################
import time
import tkinter as tk
import pyautogui
import keyboard

class MouseRecorder:
    def __init__(self, root):
        self.root = root
        self.root.title("Mouse Recorder")
        self.root.geometry("500x500")
        self.root.attributes("-topmost", True)

        self.recording = False
        self.recorded_position = None

        record_button = tk.Button(self.root, text="Record", command=self.record_position)
        record_button.pack(side=tk.LEFT, padx=10)

        play_button = tk.Button(self.root, text="Play", command=self.play_position)
        play_button.pack(side=tk.LEFT, padx=10)

        MacroBase_button = tk.Button(self.root, text="MacroBase", command=self.MacroBase)
        MacroBase_button.pack(side=tk.LEFT, padx=10)
###################################################################################################################################################################################################################
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
#######################################################################################################################################################################################################################################

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

    
#######################################################################################################################################################################################################################################

#######################################################################################################################################################################################################################################
root = tk.Tk()
mouse_recorder = MouseRecorder(root)
root.mainloop()
#######################################################################################################################################################################################################################################
