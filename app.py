import tkinter as tk
from tkinter import ttk
from typing import Tuple, Callable
from ctypes import windll


# fix high DPI blurriness in Windows
windll.shcore.SetProcessDpiAwareness(1)

def reset_button_test():
    print("Reset button clicked!")


class Menu(ttk.Frame):
    def __init__(self, parent, reset_function: Callable):
        super().__init__(parent)

        self.create_widgets()
        self.create_layout()
        self.create_reset_button(reset_function)
        
        self.grid(row=0, column=0, columnspan=3, sticky='nsew')

    def create_widgets(self):
        self.label = ttk.Label(self, background='red')

    def create_layout(self):
        self.label.pack(expand=True, fill='both')
    
    def create_reset_button(self, reset_function):
        reset = ttk.Button(self, text='Button', command=reset_function)
        reset.place(relx=1, rely=1, anchor='se')
        reset.lift()


class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.create_widgets()
        self.create_layout()
        
        self.grid(row=0, column=3, columnspan=7, sticky='nsew')

    def create_widgets(self):
        self.label = ttk.Label(self, background='green')

    def create_layout(self):
        self.label.pack(expand=True, fill='both')


class Page(ttk.Frame):
    def __init__(self, parent, menu: Menu, main: Main, reset_function: Callable):
        super().__init__(parent)
        
        self.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1, uniform='a')
        self.rowconfigure(0, weight=1, uniform='a')
        menu(self, reset_function)
        main(self)

        self.place(x=0, y=0, relheight=1, relwidth=1)

class App(tk.Tk):
    def __init__(self, title: str, geometry: Tuple[int, int], minsize: Tuple[int, int]) -> None:
        # initialization
        super().__init__()
        self.title(title)
        self.geometry(f'{geometry[0]}x{geometry[1]}')
        self.minsize(minsize[0], minsize[1])
        self.state('zoomed')

        # widgets
        Page(self, Menu, Main, reset_button_test)

        # run the app
        self.mainloop()



App("In Search for a Gem", (1280, 720), (854, 480))