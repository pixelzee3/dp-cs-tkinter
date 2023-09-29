import tkinter as tk
from tkinter import ttk
from typing import Tuple, Dict
from ctypes import windll
from pages import Page
from custom_pages import PageG, PageGA, PageGAA, PageGAAA, PageGAAB1, PageGAAB2, TestPage1, TestPage2

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
        self.page_config = {
            'G': PageG,
            'GA': PageGA,
            'GAA': PageGAA,
            'GAAA': PageGAAA,
            'GAAB1': PageGAAB1,
            'GAAB2': PageGAAB2,
            'GAB': TestPage2,
            'GB': TestPage2,
        }

        # initialize
        self.reset()

        # run the app
        self.mainloop()

    def reset(self):
        # reinitialize pages, or perform reinitialization of pages upon reset so that pages have fresh state
        self.pages: Dict[str, Page] = {name: cls(self, self.reset, self.select) for name, cls in self.page_config.items()}

        # put genesis page on screen
        self.pages['G'].lift()


    def select(self, message: str):
        self.pages[message].lift()



App("In Search for a Gem", (1280, 720), (854, 480))