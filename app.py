import tkinter as tk
from tkinter import ttk
from typing import Tuple
from ctypes import windll
from custom_pages import TestPage1, TestPage2

# fix high DPI blurriness in Windows
windll.shcore.SetProcessDpiAwareness(1)


class App(tk.Tk):
    def __init__(self, title: str, geometry: Tuple[int, int], minsize: Tuple[int, int]) -> None:
        # initialization
        super().__init__()
        self.title(title)
        self.geometry(f'{geometry[0]}x{geometry[1]}')
        self.minsize(minsize[0], minsize[1])
        self.state('zoomed')

        # widgets
        self.page1 = TestPage1(self, self.reset_button_test)
        self.page2 = TestPage2(self, self.reset_button_test)
        
        # run the app
        self.mainloop()

    def reset_button_test(self):
        self.page1.lift()



App("In Search for a Gem", (1280, 720), (854, 480))