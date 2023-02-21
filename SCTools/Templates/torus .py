# import tkinter as tk
# import math

# def create_buttons(num_buttons, radius, name):
#     """Create 'num_buttons' buttons arranged around a torus with 'radius'."""
#     buttons = []
#     for i in range(num_buttons):
#         angle = 2 * i * math.pi / num_buttons
#         x = radius * math.cos(angle) + radius
#         y = radius * math.sin(angle) + radius
#         button = tk.Button(root, text=name, command=lambda name=f"Button {i+1}": print(name))
#         button.place(x=x, y=y)
#         buttons.append(button)
#     return buttons

# if __name__ == "__main__":
#     x = 8   # number of buttons
#     r = 100 # radius of torus
#     name = "Button"   # set button name here

#     root = tk.Tk()
#     root.geometry(f"{2*r+50}x{2*r+50}")   # set window size

#     buttons = create_buttons(x, r, name)

#     root.mainloop()


import tkinter as tk
import math

def add_pizza_slice(root, x, num_slices):
    # calculate the angle between each button
    slice_angle = 360 / num_slices
    
    # calculate the radius of the pizza slice (based on the width of the root window)
    radius = root.winfo_width() / 2
    
    # loop through the number of slices and create a button for each one
    for i in range(num_slices):
        # calculate the angle for this button
        angle = slice_angle * i
        
        # calculate the coordinates for the button's center (relative to the root window)
        x = math.cos(math.radians(angle)) * radius + root.winfo_width() / 2
        y = math.sin(math.radians(angle)) * radius + root.winfo_height() / 2
        
        # create the button
        button = tk.Button(root, text=f"Slice {i+1}", command=lambda: print(f"You clicked slice {i+1}!"))
        button.place(x=x-25, y=y-25, width=50, height=50)
root = tk.Tk()
root.geometry("400x400")

add_pizza_slice(root, 8, 4)

root.mainloop()
