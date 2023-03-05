################################################################################################################################################################################################

import math
import tkinter as tk
import tkinter.simpledialog as sd

class ClockFace:
    def __init__(self, root, button_size=50, num_buttons=12):
        self.root = root
        self.button_size = button_size
        self.num_buttons = num_buttons
        self.buttons = []

        self.canvas = tk.Canvas(root, width=500, height=500)
        self.canvas.pack(side=tk.TOP)

        self.draw_clock_face()
        self.create_add_button_button()
        self.create_remove_button_button()
        self.create_button_list()

    def draw_clock_face(self):
        cx, cy = 250, 250
        r = 200
        angle = (2 * math.pi) / self.num_buttons

        for i in range(self.num_buttons):
            x = cx + r * math.cos(angle * i - math.pi / 2)
            y = cy + r * math.sin(angle * i - math.pi / 2)
            button = tk.Button(self.canvas, text=str(i), command=lambda i=i: self.button_clicked(i))
            self.buttons.append(button)
            self.canvas.create_window(x, y, window=button)

    def create_add_button_button(self):
        add_button = tk.Button(self.root, text="Add New Button", command=self.add_button)
        add_button.pack(side=tk.LEFT)

    def create_remove_button_button(self):
        remove_button = tk.Button(self.root, text="Remove Selected Button", command=self.remove_button)
        remove_button.pack(side=tk.RIGHT)

    def create_button_list(self):
        self.button_list = tk.Listbox(self.root)
        self.button_list.pack(side=tk.BOTTOM, fill=tk.BOTH)

        for button in self.buttons:
            self.button_list.insert(tk.END, button['text'])

    def button_clicked(self, i):
        print("Hello World " + str(i))

    def add_button(self):
        name = sd.askstring("Add New Button", "Enter button name:")
        if name:
            cx, cy = 250, 250
            r = 200
            angle = (2 * math.pi) / (len(self.buttons) + 1)
            x = cx + r * math.cos(angle * len(self.buttons) - math.pi / 2)
            y = cy + r * math.sin(angle * len(self.buttons) - math.pi / 2)
            button = tk.Button(self.canvas, text=name, command=lambda i=len(self.buttons): self.button_clicked(i))
            self.buttons.append(button)
            self.canvas.create_window(x, y, window=button)
            self.button_list.insert(tk.END, name)

    def remove_button(self):
        selected = self.button_list.curselection()
        if selected:
            button_index = selected[0]
            button = self.buttons.pop(button_index)
            self.button_list.delete(button_index)

            self.canvas.delete(button)

            cx, cy = 250, 250
            r = 200
            angle = (2 * math.pi) / len(self.buttons)
            for i, button in enumerate(self.buttons):
                x = cx + r * math.cos(angle * i - math.pi / 2)
                y = cy + r * math.sin(angle * i - math.pi / 2)
                self.canvas.coords(button, x, y)



root = tk.Tk()
root.title("Clock Face")
app = ClockFace(root)
root.mainloop()








#################################################################  clock Face Buttons ###############################################################################################################################
# import tkinter as tk
# import math

# class ClockFace(tk.Canvas):
#     def __init__(self, master=None, num_buttons=12, radius=100, **kwargs):
#         super().__init__(master, **kwargs)
#         self.num_buttons = num_buttons
#         self.radius = radius
#         self.draw_clock_face()

#     def draw_clock_face(self):
#         self.delete(tk.ALL)
#         center_x, center_y = self.winfo_width() // 2, self.winfo_height() // 2
#         angle = math.pi * 2 / self.num_buttons
#         for i in range(self.num_buttons):
#             x = center_x + self.radius * math.cos(i * angle - math.pi / 2)
#             y = center_y + self.radius * math.sin(i * angle - math.pi / 2)
#             self.create_oval(x - 10, y - 10, x + 10, y + 10, fill="black")
    
#     def set_num_buttons(self, num_buttons):
#         self.num_buttons = num_buttons
#         self.draw_clock_face()
    
#     def set_radius(self, radius):
#         self.radius = radius
#         self.draw_clock_face()

# class App(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.pack(fill=tk.BOTH, expand=True)
#         self.create_widgets()

#     def create_widgets(self):
#         self.clock_face = ClockFace(self, num_buttons=12, radius=100, bg="white")
#         self.clock_face.pack(fill=tk.BOTH, expand=True)

#         self.num_buttons_scale = tk.Scale(self, from_=1, to=24, orient=tk.HORIZONTAL, label="Number of Buttons",
#                                           command=self.on_num_buttons_scale)
#         self.num_buttons_scale.set(12)
#         self.num_buttons_scale.pack()

#         self.radius_scale = tk.Scale(self, from_=50, to=200, orient=tk.HORIZONTAL, label="Radius",
#                                      command=self.on_radius_scale)
#         self.radius_scale.set(100)
#         self.radius_scale.pack()

#     def on_num_buttons_scale(self, value):
#         self.clock_face.set_num_buttons(int(value))

#     def on_radius_scale(self, value):
#         self.clock_face.set_radius(int(value))

# if __name__ == '__main__':
#     root = tk.Tk()
#     root.geometry("400x400")
#     app = App(master=root)
#     app.mainloop()




################################################################################################################################################################################################




# import tkinter as tk
# import math

# class CircleButtonGUI:
#     def __init__(self, num_buttons=8, button_size=50, padding=20, text_size=12, circle_radius=150, torus_radius=50):
#         self.num_buttons = num_buttons
#         self.button_size = button_size
#         self.padding = padding
#         self.text_size = text_size
#         self.circle_radius = circle_radius
#         self.torus_radius = torus_radius
        
#         self.root = tk.Tk()
#         self.root.title("Circle Button GUI")
#         self.canvas = tk.Canvas(self.root, width=2*circle_radius+2*padding, height=2*circle_radius+2*padding)
#         self.canvas.pack()
        
#         self.buttons = []
#         for i in range(num_buttons):
#             angle = 2 * math.pi * i / num_buttons
#             x = circle_radius + torus_radius * math.cos(angle)
#             y = circle_radius + torus_radius * math.sin(angle)
#             button = tk.Button(self.canvas, text=str(i+1), width=button_size, height=button_size, font=("Arial", text_size), command=lambda i=i: self.button_click(i))
#             self.canvas.create_window(x, y, window=button)
#             self.buttons.append(button)
            
#     def run(self):
#         self.root.mainloop()
        
#     def button_click(self, i):
#         print(f"Button {i+1} clicked!")
        
# if __name__ == "__main__":
#     gui = CircleButtonGUI(num_buttons=12, button_size=5, padding=10, text_size=12, circle_radius=200, torus_radius=200)
#     gui.run()




































################################################################################################################################################################################################
################################################################ Display image on button ( buggy ) ########################################################################################################
# import tkinter as tk
# from PIL import Image, ImageTk

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Button App")
        
#         # Create the buttons
#         self.button1 = tk.Button(master, text="Button 1", command=self.print_hello_world, width=50, height=25, bg="grey")
#         self.button2 = tk.Button(master, text="Button 2", command=self.print_hello_world, width=50, height=25, bg="grey")
#         self.button3 = tk.Button(master, text="Button 3", command=self.print_hello_world, width=50, height=25, bg="grey")
#         self.button4 = tk.Button(master, width=50, height=25, bg="grey")
#         self.button5 = tk.Button(master, width=50, height=25, bg="grey")

#         # Load the images using PIL
#         self.image1 = ImageTk.PhotoImage(Image.open("image.jpg"))
#         # self.image2 = ImageTk.PhotoImage(Image.open("image.jpg"))
#         # self.image3 = ImageTk.PhotoImage(Image.open("image.jpg"))
#         # self.button1.config(image=self.image1)
        

#         # Bind the hover events to the buttons
#         self.button1.bind("<Enter>", lambda event, img=self.image1: self.on_hover(event, img))
#         self.button1.bind("<Leave>", self.on_leave)

#         self.button2.bind("<Enter>", lambda event, img=self.image1: self.on_hover(event, img))
#         self.button2.bind("<Leave>", self.on_leave)

#         self.button3.bind("<Enter>", lambda event, img=self.image1: self.on_hover(event, img))
#         self.button3.bind("<Leave>", self.on_leave)

#         self.button4.bind("<Enter>", lambda event, img=self.image1: self.on_hover(event, img))
#         self.button4.bind("<Leave>", self.on_leave)

#         self.button5.bind("<Enter>", lambda event, img=self.image1: self.on_hover(event, img))
#         self.button5.bind("<Leave>", self.on_leave)


#         # Place the buttons in the window
#         self.button1.grid(row=0, column=0)
#         self.button2.grid(row=0, column=1)
#         self.button3.grid(row=0, column=2)
#         self.button4.grid(row=1, column=0)
#         self.button5.grid(row=1, column=1)

#     def print_hello_world(self):
#         print("Hello, World!")

#     def on_hover(self, event, image):
#         event.widget.config(bg="white", image=image)

#     def on_leave(self, event):
#         event.widget.config(bg="grey", image="")

# root = tk.Tk()
# app = App(root)
# root.mainloop()
