from typing import Callable
from pages import Page, ImageMain, Menu
import tkinter as tk
from tkinter import ttk


class TestMenu1(Menu):
    def __init__(self, parent, reset, select):
        super().__init__(parent, reset, select)
    
    def create_widgets(self, select):
        self.page_2_button = ttk.Button(self, text='Go to page 2', command=lambda: select('test2'))
    
    def create_layout(self):
        self.page_2_button.pack()


class TestPage1(Page):
    def __init__(self, parent, reset: Callable, select):
        super().__init__(parent, reset, select)
    
    def create_page(self, reset, select):
        ImageMain(self, 'images/model 3.jpg')
        TestMenu1(self, reset, select)


class TestMenu2(Menu):
    def __init__(self, parent, reset_function, select):
        super().__init__(parent, reset_function, select)
    
    def create_widgets(self, select):
        self.red_bg = ttk.Label(self, background='red')
    
    def create_layout(self):
        self.red_bg.pack(expand=True, fill='both')


class TestPage2(Page):
    def __init__(self, parent, reset: Callable, select: Callable):
        super().__init__(parent, reset, select)
    
    def create_page(self, reset_function, select):
        ImageMain(self, 'images/model 3.jpg')
        TestMenu2(self, reset_function, select)