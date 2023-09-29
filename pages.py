from abc import ABC,abstractmethod
import tkinter as tk
from tkinter import ttk
from typing import Callable
from PIL import Image, ImageTk


class Menu(ttk.Frame, ABC):
    def __init__(self, parent, reset: Callable, select: Callable):
        super().__init__(parent)

        self.create_widgets(select)
        self.create_layout()
        self.create_reset_button(reset)
        
        self.grid(row=0, column=0, columnspan=3, sticky='nsew')

    def create_reset_button(self, reset):
        reset = ttk.Button(self, text='Reset', command=reset)
        reset.place(relx=1, rely=1, anchor='se')
        reset.lift()
    
    @abstractmethod
    def create_widgets(self, select):
        # * Place widgets here
        # self.label = ttk.Label(self, background='red')
        pass

    @abstractmethod
    def create_layout(self):
        # * Place widgets here
        # self.label.pack(expand=True, fill='both')
        pass



class ImageMain(ttk.Frame):
    def __init__(self, parent, path: str):
        super().__init__(parent)
        
        # import image
        self.image_original = Image.open(path)
        self.image_ratio = self.image_original.size[0] / self.image_original.size[1]
        self.image_tk = ImageTk.PhotoImage(self.image_original)

        self.create_canvas()

        self.grid(row=0, column=3, columnspan=7, sticky='nsew')

    def create_canvas(self):
        # create canvas
        self.canvas = tk.Canvas(self, background='black', bd=0, highlightthickness=0, relief='ridge')
        self.canvas.pack(expand=True, fill='both')
        # put image on canvas + when canvas is resized, run configure image
        self.canvas.bind('<Configure>', self.fill_image)
        self.canvas.create_image(0, 0, image=self.image_tk, anchor='nw')

    def fill_image(self, event):
        # current canvas ratio
        canvas_ratio = event.width / event.height
        # canvas is wider than the image
        if canvas_ratio > self.image_ratio:
            width = int(event.width)
            height = int(width / self.image_ratio)
        # canvas is narrower than the image
        else:
            height = int(event.height)
            width = int(height * self.image_ratio)

        # create resized image and put on canvas        
        resized_image = self.image_original.resize((width, height))
        self.resized_tk = ImageTk.PhotoImage(resized_image)
        self.canvas.create_image(int(event.width / 2), int(event.height / 2), anchor = 'center', image=self.resized_tk)

class Page(ttk.Frame, ABC):
    def __init__(self, parent, reset: Callable, select: Callable):
        super().__init__(parent)
        
        # create grid for page
        self.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1, uniform='a')
        self.rowconfigure(0, weight=1, uniform='b')
        
        # put page elements
        self.create_page(reset, select)

        # place page on screen
        self.place(x=0, y=0, relheight=1, relwidth=1)
    
    # show page on screen
    def lift(self):
        self.tkraise()

    @abstractmethod
    def create_page(self, reset, select):
        # ? How to implement?
        
        # * Create an instance of an implementation of the ImageMain class like so
        # ImageMain('path/to/image')

        # * Create an instance of an implementation of the Menu class like so
        # Menu(self, reset, select)
        pass