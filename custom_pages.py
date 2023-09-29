from typing import Callable
from pages import Page, ImageMain, Menu
import tkinter as tk
from tkinter import ttk


class TestMenu(Menu):
    def __init__(self, parent, reset_function):
        super().__init__(parent, reset_function)
    
    def create_widgets(self):
        self.green_bg = ttk.Label(self, background='green')
    
    def create_layout(self):
        self.green_bg.pack(expand=True, fill='both')


class TestPage(Page):
    def __init__(self, parent, reset_function: Callable):
        super().__init__(parent, reset_function)
    
    def create_image(self):
        ImageMain(self, 'images/model 3.jpg')

    def create_menu(self, reset_function):
        TestMenu(self, reset_function)