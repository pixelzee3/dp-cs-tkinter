import tkinter as tk
from tkinter import ttk
from typing import Tuple, Dict
from ctypes import windll
from pages import Page
from custom_pages import PageG, PageGA, PageGAA, PageGAAA, PageGAAB1, PageGAAB2, PageGAAB3, PageGAB1, PageGAB2, PageGAB3, PageGAB4, PageGB, PageGBA, PageGBAA, PageGBANoA, PageGBB1, PageGBB2, PageGBB2A, PageGBB2B, PageGBB2C, PageLose, PageWin

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
            'GAAB3': PageGAAB3,
            'GAB1': PageGAB1,
            'GAB2': PageGAB2,
            'GAB3': PageGAB3,
            'GAB4': PageGAB4,
            'GB': PageGB,
            'GBA': PageGBA,
            'GBAA': PageGBAA,
            'GBANoA': PageGBANoA,
            'GBB1': PageGBB1,
            'GBB2': PageGBB2,
            'GBB2A': PageGBB2A,
            'GBB2B': PageGBB2B,
            'GBB2C': PageGBB2C,
            'win': PageWin,
            'lose': PageLose,
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