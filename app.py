import tkinter as tk
from tkinter import ttk
from typing import Tuple, Dict
from ctypes import windll
from pages import Page
from custom_pages import PageG, TestPage1, TestPage2

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
        self.pages: Dict[str, Page] = {
            'G': PageG(self, self.reset, self.select),
            'GA': TestPage1(self, self.reset, self.select),
            'GB': TestPage2(self, self.reset, self.select),
        }

        self.reset()

        # run the app
        self.mainloop()

    def reset(self):
        # put genesis page on screen
        self.pages['G'].lift()

    def select(self, message: str):
        self.pages[message].lift()



App("In Search for a Gem", (1280, 720), (854, 480))