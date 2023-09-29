from typing import Callable
from pages import Page, ImageMain, Menu
import tkinter as tk
from tkinter import ttk


# * Test Page 1 ============================================================================================

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


# * Test Page 2 ============================================================================================


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


# * G ============================================================================================

class MenuG(Menu):
    def __init__(self, parent, reset_function, select):
        super().__init__(parent, reset_function, select)

        # define grid
        self.columnconfigure(0, weight=1, uniform='a')
        self.rowconfigure((0, 1), weight=1, uniform='a')
    
    # if radio button is clicked, enable button
    def on_radio_click(self):
        if self.radio_var.get():
            self.submit['state'] = 'enabled'
        else:
            self.submit['state'] = 'disabled'

    # select pages according to selection
    def on_submit(self, select):
        if self.radio_var.get() == 'left':
            select('GA')
        else:
            select('GB')

    def create_widgets(self, select):
        # define radio frame, radio variable, and submit button
        self.radio = ttk.Frame(self)
        self.radio_var = tk.StringVar()
        self.submit = ttk.Button(self.radio, text='Submit', command=lambda: self.on_submit(select))

        # disable button initially
        self.submit['state'] = 'disabled'

        # define radio buttons
        self.radio_left = ttk.Radiobutton(self.radio, text="Left", variable=self.radio_var, value="left", command=self.on_radio_click)
        self.radio_right = ttk.Radiobutton(self.radio, text="Right", variable=self.radio_var, value="right", command=self.on_radio_click)

        # define text
        self.label = ttk.Label(self, text='Billy had just woke up after his plane crashed in this mysterious island. Now, he must find a hidden gem in this island to teleport his way back home. Which way should he go?', font='Calibri 16')

    def create_layout(self):
        self.radio.columnconfigure((0, 1), weight=1, uniform='a')
        self.radio.rowconfigure((0, 1), weight=1, uniform='a')

        self.radio_left.grid(row=0, column=0)
        self.radio_right.grid(row=0, column=1)
        self.submit.grid(column=0, row=1, columnspan=2)

        self.label.grid(column=0, row=0)
        self.radio.grid(column=0, row=1)

        # Make label wrap text dynamically according to width of frame
        self.bind('<Configure>', lambda event: self.label.configure(wraplength=event.width))

class PageG(Page):
    def __init__(self, parent, reset: Callable, select: Callable):
        super().__init__(parent, reset, select)
    
    def create_page(self, reset_function, select):
        ImageMain(self, 'images/G.png')
        MenuG(self, reset_function, select)

# * GA ===========================================================================================

class MenuGA(Menu):
    def __init__(self, parent, reset_function, select):
        super().__init__(parent, reset_function, select)

        # define grid
        self.columnconfigure(0, weight=1, uniform='a')
        self.rowconfigure((0, 1), weight=1, uniform='a')
    

    # select pages according to selection
    def on_submit(self, select):
        if self.scale_value.get() > 0.5:
            select('GAA')
        else:
            select('GAB')

    def create_widgets(self, select):
        # define scale frame, scale variable, and submit button
        self.scale_value = tk.DoubleVar(value=0)
        self.scale_frame = ttk.Frame(self)
        self.submit = ttk.Button(self.scale_frame, text='Submit', command=lambda: self.on_submit(select))

        self.scale = ttk.Scale(
            self.scale_frame, 
            length=300,
            variable=self.scale_value,
        )

        # define text
        self.label = ttk.Label(self, text='He finds a well. How much from it should he drink?', font='Calibri 16')

    def create_layout(self):
        # put button and scale on scale frame
        self.scale.pack()
        self.submit.pack()

        # put label and scale frame on menu
        self.label.grid(column=0, row=0)
        self.scale_frame.grid(column=0, row=1)
        # Make label wrap text dynamically according to width of frame
        self.bind('<Configure>', lambda event: self.label.configure(wraplength=event.width))

class PageGA(Page):
    def __init__(self, parent, reset: Callable, select: Callable):
        super().__init__(parent, reset, select)
    
    def create_page(self, reset_function, select):
        ImageMain(self, 'images/GA.png')
        MenuGA(self, reset_function, select)