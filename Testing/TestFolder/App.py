import Functions
import tkinter as tk 




class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Application")
        self.geometry("400x300")

        self.label = tk.Label(self, text="Hello, World!")
        self.label.pack(pady=10)

        self.button = tk.Button(self, text="Click me!", command=self.handle_click)
        self.button.pack()

    def handle_click(self):
        Functions.handle_button_click()
        self.label.configure(text="Button clicked!")
        Functions.process_data(data="helloProcessData")

if __name__ == "__main__":
    Functions.main()
    app = App()
    app.mainloop()
