from typing import Callable
from pages import Page, ImageMain, Menu
import tkinter as tk
from tkinter import ttk



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
        self.bind('<Configure>', lambda event: self.label.configure(wraplength=event.width - 20))

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
            select('GAB1')

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
        self.bind('<Configure>', lambda event: self.label.configure(wraplength=event.width - 20))

class PageGA(Page):
    def __init__(self, parent, reset: Callable, select: Callable):
        super().__init__(parent, reset, select)
    
    def create_page(self, reset_function, select):
        ImageMain(self, 'images/GA.png')
        MenuGA(self, reset_function, select)

# * GAA ============================================================================================

class MenuGAA(Menu):
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
        if self.radio_var.get() == 'visit':
            select('GAAA')
        else:
            select('GAAB1')

    def create_widgets(self, select):
        # define radio frame, radio variable, and submit button
        self.radio = ttk.Frame(self)
        self.radio_var = tk.StringVar()
        self.submit = ttk.Button(self.radio, text='Submit', command=lambda: self.on_submit(select))

        # disable button initially
        self.submit['state'] = 'disabled'

        # define radio buttons
        self.radio_left = ttk.Radiobutton(self.radio, text="Visit the village", variable=self.radio_var, value="visit", command=self.on_radio_click)
        self.radio_right = ttk.Radiobutton(self.radio, text="Pass the village", variable=self.radio_var, value="pass", command=self.on_radio_click)

        # define text
        self.label = ttk.Label(self, text='Billy drank enough water such that he was able to traverse the forest. Whilst doing so, he finds a village. Should he pass it or should he visit it?', font='Calibri 16')

    def create_layout(self):
        self.radio.columnconfigure((0, 1), weight=1, uniform='a')
        self.radio.rowconfigure((0, 1), weight=1, uniform='a')

        self.radio_left.grid(row=0, column=0)
        self.radio_right.grid(row=0, column=1)
        self.submit.grid(column=0, row=1, columnspan=2)

        self.label.grid(column=0, row=0)
        self.radio.grid(column=0, row=1)

        # Make label wrap text dynamically according to width of frame
        self.bind('<Configure>', lambda event: self.label.configure(wraplength=event.width - 20))

class PageGAA(Page):
    def __init__(self, parent, reset: Callable, select: Callable):
        super().__init__(parent, reset, select)
    
    def create_page(self, reset_function, select):
        ImageMain(self, 'images/GAA.png')
        MenuGAA(self, reset_function, select)


# * GAAA ==========================================================================================

class MenuGAAA(Menu):
    def __init__(self, parent, reset_function, select):
        super().__init__(parent, reset_function, select)

        # define grid
        self.columnconfigure(0, weight=1, uniform='a')
        self.rowconfigure((0, 1), weight=1, uniform='a')
    
    # if at least one item is stolen, enable button
    def on_check(self):
        if self.checked_gem.get() or self.checked_money.get() or self.checked_food.get():
            self.submit['state'] = 'enabled'
        else:
            self.submit['state'] = 'disabled'

    # select pages according to selection
    def on_submit(self, select):
        # TODO: May need updating!
        if self.checked_gem.get():
            select('win')
        else:
            select('lose')

    def create_widgets(self, select):
        # define check frame, checked variables, and submit button
        self.check_frame = ttk.Frame(self)
        self.checked_gem = tk.BooleanVar(value=False)
        self.checked_money = tk.BooleanVar(value=False)
        self.checked_food = tk.BooleanVar(value=False)
        self.submit = ttk.Button(self.check_frame, text='Submit', command=lambda: self.on_submit(select))

        # disable button initially
        self.submit['state'] = 'disabled'

        # define check buttons
        self.check_gem = ttk.Checkbutton(self.check_frame, text="Steal the gem", variable=self.checked_gem, command=self.on_check)
        self.check_money = ttk.Checkbutton(self.check_frame, text="Steal the money", variable=self.checked_money, command=self.on_check)
        self.check_food = ttk.Checkbutton(self.check_frame, text="Steal the food", variable=self.checked_food, command=self.on_check)
        
        # define text
        self.label = ttk.Label(self, text='Billy visits the village and finds a chest. What should he steal from it?', font='Calibri 16')

    def create_layout(self):
        # pack things inside check frame
        self.check_gem.pack()
        self.check_money.pack()
        self.check_food.pack()
        self.submit.pack()

        # put label and pack frame on menu
        self.label.grid(column=0, row=0)
        self.check_frame.grid(column=0, row=1)

        # Make label wrap text dynamically according to width of frame
        self.bind('<Configure>', lambda event: self.label.configure(wraplength=event.width - 20))

class PageGAAA(Page):
    def __init__(self, parent, reset: Callable, select: Callable):
        super().__init__(parent, reset, select)
    
    def create_page(self, reset_function, select):
        ImageMain(self, 'images/GAAA.png')
        MenuGAAA(self, reset_function, select)


# * GAAB1 ===========================================================================================

class MenuGAAB1(Menu):
    def __init__(self, parent, reset_function, select):
        super().__init__(parent, reset_function, select)

        # define grid
        self.columnconfigure(0, weight=1, uniform='a')
        self.rowconfigure((0, 1), weight=1, uniform='a')
    

    # select page
    def on_submit(self, select):
        select('GAAB2')

    def create_widgets(self, select):
        # define entry frame, text variable, and submit button
        self.text = tk.StringVar()
        self.entry_frame = ttk.Frame(self)
        self.submit = ttk.Button(self.entry_frame, text='Submit', command=lambda: self.on_submit(select))

        # define entry
        self.entry = ttk.Entry(self.entry_frame, textvariable=self.text)

        # define text
        self.label = ttk.Label(self, text='After passing the village, Billy is confronted by a villager. Say something!', font='Calibri 16')

    def create_layout(self):
        # put button and scale on scale frame
        self.entry.pack()
        self.submit.pack()

        # put label and scale frame on menu
        self.label.grid(column=0, row=0)
        self.entry_frame.grid(column=0, row=1)
        # Make label wrap text dynamically according to width of frame
        self.bind('<Configure>', lambda event: self.label.configure(wraplength=event.width - 20))

class PageGAAB1(Page):
    def __init__(self, parent, reset: Callable, select: Callable):
        super().__init__(parent, reset, select)
    
    def create_page(self, reset_function, select):
        ImageMain(self, 'images/GAAB1.png')
        MenuGAAB1(self, reset_function, select)


# * GAAB2 ========================================================================================

class MenuGAAB2(Menu):
    def __init__(self, parent, reset_function, select):
        super().__init__(parent, reset_function, select)

        # define grid
        self.columnconfigure(0, weight=1, uniform='a')
        self.rowconfigure((0, 1, 2), weight=1, uniform='a')

    # select pages according to selection
    def on_attack(self, select):
        # reduce health by 7.2%
        new_health = self.health.get() - 0.072

        if new_health < 0:
            new_health = 0
        
        # set health. if health is dead then next page
        self.health.set(new_health)
        if self.health.get() == 0 :
            select('GAAB3')

    def create_widgets(self, select):
        # health variable
        self.health = tk.DoubleVar(value=1)

        # define health bar
        self.health_frame = ttk.Frame(self)
        self.health_label = ttk.Label(self.health_frame, text='Villager health:')
        self.health_bar = ttk.Progressbar(self.health_frame, variable=self.health, length=400, maximum=1)
        self.attack = ttk.Button(self, text='Click here to attack!', command=lambda: self.on_attack(select))

        # define text
        self.label = ttk.Label(self, text='The villager does not care about what Billy said! He attacks you. Fight back!', font='Calibri 16')

    def create_layout(self):
        # put label and health bar on frame
        self.health_label.pack()
        self.health_bar.pack()

        # put all on menu
        self.label.grid(column=0, row=0)
        self.health_frame.grid(column=0, row=1)
        self.attack.grid(column=0, row=2, sticky='nsew')

        # Make label wrap text dynamically according to width of frame
        self.bind('<Configure>', lambda event: self.label.configure(wraplength=event.width - 20))

class PageGAAB2(Page):
    def __init__(self, parent, reset: Callable, select: Callable):
        super().__init__(parent, reset, select)
    
    def create_page(self, reset_function, select):
        ImageMain(self, 'images/GAAB2.png')
        MenuGAAB2(self, reset_function, select)


# * GAAB3 ==========================================================================================

class MenuGAAB3(Menu):
    def __init__(self, parent, reset_function, select):
        super().__init__(parent, reset_function, select)

        # define grid
        self.columnconfigure(0, weight=1, uniform='a')
        self.rowconfigure((0, 1), weight=1, uniform='a')
    
    # if at least one item is stolen, enable button
    def on_check(self):
        if self.checked_gem.get() or self.checked_money.get() or self.checked_food.get():
            self.submit['state'] = 'enabled'
        else:
            self.submit['state'] = 'disabled'

    # select pages according to selection
    def on_submit(self, select):
        # TODO: May need updating!
        if self.checked_gem.get():
            select('win')
        else:
            select('lose')

    def create_widgets(self, select):
        # define check frame, checked variables, and submit button
        self.check_frame = ttk.Frame(self)
        self.checked_gem = tk.BooleanVar(value=False)
        self.checked_money = tk.BooleanVar(value=False)
        self.checked_food = tk.BooleanVar(value=False)
        self.submit = ttk.Button(self.check_frame, text='Submit', command=lambda: self.on_submit(select))

        # disable button initially
        self.submit['state'] = 'disabled'

        # define check buttons
        self.check_gem = ttk.Checkbutton(self.check_frame, text="Steal the gem", variable=self.checked_gem, command=self.on_check)
        self.check_money = ttk.Checkbutton(self.check_frame, text="Steal the money", variable=self.checked_money, command=self.on_check)
        self.check_food = ttk.Checkbutton(self.check_frame, text="Steal the food", variable=self.checked_food, command=self.on_check)
        
        # define text
        self.label = ttk.Label(self, text='Billy successfully kills the villager. He loots his body; what should he steal?', font='Calibri 16')

    def create_layout(self):
        # pack things inside check frame
        self.check_gem.pack()
        self.check_money.pack()
        self.check_food.pack()
        self.submit.pack()

        # put label and pack frame on menu
        self.label.grid(column=0, row=0)
        self.check_frame.grid(column=0, row=1)

        # Make label wrap text dynamically according to width of frame
        self.bind('<Configure>', lambda event: self.label.configure(wraplength=event.width - 20))

class PageGAAB3(Page):
    def __init__(self, parent, reset: Callable, select: Callable):
        super().__init__(parent, reset, select)
    
    def create_page(self, reset_function, select):
        ImageMain(self, 'images/GAAB3.png')
        MenuGAAB3(self, reset_function, select)


# * GAB1 ========================================================================================

class MenuGAB1(Menu):
    def __init__(self, parent, reset_function, select):
        super().__init__(parent, reset_function, select)

        # define grid
        self.columnconfigure(0, weight=1, uniform='a')
        self.rowconfigure((0, 1, 2), weight=1, uniform='a')

    # select pages according to selection
    def on_attack(self, select):
        # reduce health by 7.2%
        new_health = self.health.get() - 0.072

        if new_health < 0:
            new_health = 0
        
        # set health. if health is dead then next page
        self.health.set(new_health)
        if self.health.get() == 0 :
            select('GAB2')

    def create_widgets(self, select):
        # health variable
        self.health = tk.DoubleVar(value=1)

        # define health bar
        self.health_frame = ttk.Frame(self)
        self.health_label = ttk.Label(self.health_frame, text='Pig health:')
        self.health_bar = ttk.Progressbar(self.health_frame, variable=self.health, length=400, maximum=1)
        self.attack = ttk.Button(self, text='Click here to attack!', command=lambda: self.on_attack(select))

        # define text
        self.label = ttk.Label(self, text='Billy did not drink enough water. He gets tired and must eat a pig to recuperate energy. Kill the pig!', font='Calibri 16')

    def create_layout(self):
        # put label and health bar on frame
        self.health_label.pack()
        self.health_bar.pack()

        # put all on menu
        self.label.grid(column=0, row=0)
        self.health_frame.grid(column=0, row=1)
        self.attack.grid(column=0, row=2, sticky='nsew')

        # Make label wrap text dynamically according to width of frame
        self.bind('<Configure>', lambda event: self.label.configure(wraplength=event.width - 20))

class PageGAB1(Page):
    def __init__(self, parent, reset: Callable, select: Callable):
        super().__init__(parent, reset, select)
    
    def create_page(self, reset_function, select):
        ImageMain(self, 'images/GAB1.png')
        MenuGAB1(self, reset_function, select)


# * GAB2 ===========================================================================================

class MenuGAB2(Menu):
    def __init__(self, parent, reset_function, select):
        super().__init__(parent, reset_function, select)

        # define grid
        self.columnconfigure(0, weight=1, uniform='a')
        self.rowconfigure((0, 1), weight=1, uniform='a')
    

    # select page
    def on_submit(self, select):
        select('GAB3')

    def create_widgets(self, select):
        # define entry frame, text variable, and submit button
        self.text = tk.StringVar()
        self.entry_frame = ttk.Frame(self)
        self.submit = ttk.Button(self.entry_frame, text='Submit', command=lambda: self.on_submit(select))

        # define entry
        self.entry = ttk.Entry(self.entry_frame, textvariable=self.text)

        # define text
        self.label = ttk.Label(self, text='The pig owner confronts Billy! What should he say to the pig owner?', font='Calibri 16')

    def create_layout(self):
        # put button and scale on scale frame
        self.entry.pack()
        self.submit.pack()

        # put label and scale frame on menu
        self.label.grid(column=0, row=0)
        self.entry_frame.grid(column=0, row=1)
        # Make label wrap text dynamically according to width of frame
        self.bind('<Configure>', lambda event: self.label.configure(wraplength=event.width - 20))

class PageGAB2(Page):
    def __init__(self, parent, reset: Callable, select: Callable):
        super().__init__(parent, reset, select)
    
    def create_page(self, reset_function, select):
        ImageMain(self, 'images/GAB2-3.png')
        MenuGAB2(self, reset_function, select)


# * GAB3 ========================================================================================

class MenuGAB3(Menu):
    def __init__(self, parent, reset_function, select):
        super().__init__(parent, reset_function, select)

        # define grid
        self.columnconfigure(0, weight=1, uniform='a')
        self.rowconfigure((0, 1, 2), weight=1, uniform='a')

    # select pages according to selection
    def on_attack(self, select):
        # reduce health by 7.2%
        new_health = self.health.get() - 0.072

        if new_health < 0:
            new_health = 0
        
        # set health. if health is dead then next page
        self.health.set(new_health)
        if self.health.get() == 0 :
            select('GAB4')

    def create_widgets(self, select):
        # health variable
        self.health = tk.DoubleVar(value=1)

        # define health bar
        self.health_frame = ttk.Frame(self)
        self.health_label = ttk.Label(self.health_frame, text='Pig owner health:')
        self.health_bar = ttk.Progressbar(self.health_frame, variable=self.health, length=400, maximum=1)
        self.attack = ttk.Button(self, text='Click here to attack!', command=lambda: self.on_attack(select))

        # define text
        self.label = ttk.Label(self, text="The pig owner doesn't care about what Billy said; he wants to kill him! Fight back!", font='Calibri 16')

    def create_layout(self):
        # put label and health bar on frame
        self.health_label.pack()
        self.health_bar.pack()

        # put all on menu
        self.label.grid(column=0, row=0)
        self.health_frame.grid(column=0, row=1)
        self.attack.grid(column=0, row=2, sticky='nsew')

        # Make label wrap text dynamically according to width of frame
        self.bind('<Configure>', lambda event: self.label.configure(wraplength=event.width - 20))

class PageGAB3(Page):
    def __init__(self, parent, reset: Callable, select: Callable):
        super().__init__(parent, reset, select)
    
    def create_page(self, reset_function, select):
        ImageMain(self, 'images/GAB2-3.png')
        MenuGAB3(self, reset_function, select)


# * GAB4 ==========================================================================================

class MenuGAB4(Menu):
    def __init__(self, parent, reset_function, select):
        super().__init__(parent, reset_function, select)

        # define grid
        self.columnconfigure(0, weight=1, uniform='a')
        self.rowconfigure((0, 1), weight=1, uniform='a')
    
    # if at least one item is stolen, enable button
    def on_check(self):
        if self.checked_gem.get() or self.checked_money.get() or self.checked_food.get():
            self.submit['state'] = 'enabled'
        else:
            self.submit['state'] = 'disabled'

    # select pages according to selection
    def on_submit(self, select):
        # TODO: May need updating!
        if self.checked_gem.get():
            select('win')
        else:
            select('lose')

    def create_widgets(self, select):
        # define check frame, checked variables, and submit button
        self.check_frame = ttk.Frame(self)
        self.checked_gem = tk.BooleanVar(value=False)
        self.checked_money = tk.BooleanVar(value=False)
        self.checked_food = tk.BooleanVar(value=False)
        self.submit = ttk.Button(self.check_frame, text='Submit', command=lambda: self.on_submit(select))

        # disable button initially
        self.submit['state'] = 'disabled'

        # define check buttons
        self.check_gem = ttk.Checkbutton(self.check_frame, text="Steal the gem", variable=self.checked_gem, command=self.on_check)
        self.check_money = ttk.Checkbutton(self.check_frame, text="Steal the money", variable=self.checked_money, command=self.on_check)
        self.check_food = ttk.Checkbutton(self.check_frame, text="Steal the food", variable=self.checked_food, command=self.on_check)
        
        # define text
        self.label = ttk.Label(self, text='Billy successfully kills the pig owner. He loots his body; what should he steal?', font='Calibri 16')

    def create_layout(self):
        # pack things inside check frame
        self.check_gem.pack()
        self.check_money.pack()
        self.check_food.pack()
        self.submit.pack()

        # put label and pack frame on menu
        self.label.grid(column=0, row=0)
        self.check_frame.grid(column=0, row=1)

        # Make label wrap text dynamically according to width of frame
        self.bind('<Configure>', lambda event: self.label.configure(wraplength=event.width - 20))

class PageGAB4(Page):
    def __init__(self, parent, reset: Callable, select: Callable):
        super().__init__(parent, reset, select)
    
    def create_page(self, reset_function, select):
        ImageMain(self, 'images/GAB4.png')
        MenuGAB4(self, reset_function, select)


# * GB ===========================================================================================

class MenuGB(Menu):
    def __init__(self, parent, reset_function, select):
        super().__init__(parent, reset_function, select)

        # define grid
        self.columnconfigure(0, weight=1, uniform='a')
        self.rowconfigure((0, 1), weight=1, uniform='a')
    

    # select page
    def on_submit(self, select):
        if len(self.text.get()) > 50:
            select('GBB1')
        else:
            select('GBA')

    def create_widgets(self, select):
        # define entry frame, text variable, and submit button
        self.text = tk.StringVar()
        self.entry_frame = ttk.Frame(self)
        self.submit = ttk.Button(self.entry_frame, text='Submit', command=lambda: self.on_submit(select))

        # define entry
        self.entry = ttk.Entry(self.entry_frame, textvariable=self.text)

        # define text
        self.label = ttk.Label(self, text='Billy finds a random dude! How should he present himself?', font='Calibri 16')

    def create_layout(self):
        # put button and scale on scale frame
        self.entry.pack()
        self.submit.pack()

        # put label and scale frame on menu
        self.label.grid(column=0, row=0)
        self.entry_frame.grid(column=0, row=1)
        # Make label wrap text dynamically according to width of frame
        self.bind('<Configure>', lambda event: self.label.configure(wraplength=event.width - 20))

class PageGB(Page):
    def __init__(self, parent, reset: Callable, select: Callable):
        super().__init__(parent, reset, select)
    
    def create_page(self, reset_function, select):
        ImageMain(self, 'images/GB.png')
        MenuGB(self, reset_function, select)


# * GBA ==========================================================================================

class MenuGBA(Menu):
    def __init__(self, parent, reset_function, select):
        super().__init__(parent, reset_function, select)

        # define grid
        self.columnconfigure(0, weight=1, uniform='a')
        self.rowconfigure((0, 1), weight=1, uniform='a')
    
    # if at least one item is stolen, enable button
    def on_check(self):
        if self.checked_gem.get() or self.checked_money.get() or self.checked_food.get():
            self.submit['state'] = 'enabled'
        else:
            self.submit['state'] = 'disabled'

    # select pages according to selection
    def on_submit(self, select):
        # TODO: May need updating!
        if self.checked_gem.get():
            select('GBAA')
        else:
            select('GBANoA')

    def create_widgets(self, select):
        # define check frame, checked variables, and submit button
        self.check_frame = ttk.Frame(self)
        self.checked_gem = tk.BooleanVar(value=False)
        self.checked_money = tk.BooleanVar(value=False)
        self.checked_food = tk.BooleanVar(value=False)
        self.submit = ttk.Button(self.check_frame, text='Submit', command=lambda: self.on_submit(select))

        # disable button initially
        self.submit['state'] = 'disabled'

        # define check buttons
        self.check_gem = ttk.Checkbutton(self.check_frame, text="Buy the gem", variable=self.checked_gem, command=self.on_check)
        self.check_money = ttk.Checkbutton(self.check_frame, text="Buy the money", variable=self.checked_money, command=self.on_check)
        self.check_food = ttk.Checkbutton(self.check_frame, text="Buy the food", variable=self.checked_food, command=self.on_check)
        
        # define text
        self.label = ttk.Label(self, text='The random dude seems to like how Billy presented himself. He offers Billy to buy some things from him. What should Billy buy?', font='Calibri 16')

    def create_layout(self):
        # pack things inside check frame
        self.check_gem.pack()
        self.check_money.pack()
        self.check_food.pack()
        self.submit.pack()

        # put label and pack frame on menu
        self.label.grid(column=0, row=0)
        self.check_frame.grid(column=0, row=1)

        # Make label wrap text dynamically according to width of frame
        self.bind('<Configure>', lambda event: self.label.configure(wraplength=event.width - 20))

class PageGBA(Page):
    def __init__(self, parent, reset: Callable, select: Callable):
        super().__init__(parent, reset, select)
    
    def create_page(self, reset_function, select):
        ImageMain(self, 'images/GBA.png')
        MenuGBA(self, reset_function, select)


# * GBAA ==========================================================================================

class MenuGBAA(Menu):
    def __init__(self, parent, reset_function, select):
        super().__init__(parent, reset_function, select)

        # define grid
        self.columnconfigure(0, weight=1, uniform='a')
        self.rowconfigure((0, 1), weight=1, uniform='a')


    # select pages according to selection
    def on_submit(self, select):
        select('GBB1')

    def create_widgets(self, select):
        # define button
        self.submit = ttk.Button(self, text='Proceed', command=lambda: self.on_submit(select))

        # define text
        self.label = ttk.Label(self, text="The random dude saw that Billy wanted to buy the gem; the gem is the most precious thing in the island and he realizes that Billy is aware of it. He is angry.", font='Calibri 16')

    def create_layout(self):
        self.label.grid(column=0, row=0)
        self.submit.grid(column=0, row=1)

        # Make label wrap text dynamically according to width of frame
        self.bind('<Configure>', lambda event: self.label.configure(wraplength=event.width - 20))

class PageGBAA(Page):
    def __init__(self, parent, reset: Callable, select: Callable):
        super().__init__(parent, reset, select)
    
    def create_page(self, reset_function, select):
        ImageMain(self, 'images/GBAA.png')
        MenuGBAA(self, reset_function, select)


# * GBANoA ==========================================================================================

class MenuGBANoA(Menu):
    def __init__(self, parent, reset_function, select):
        super().__init__(parent, reset_function, select)

        # define grid
        self.columnconfigure(0, weight=1, uniform='a')
        self.rowconfigure((0, 1), weight=1, uniform='a')


    # select pages according to selection
    def on_submit(self, select):
        select('GBB1')

    def create_widgets(self, select):
        # define button
        self.submit = ttk.Button(self, text='Proceed', command=lambda: self.on_submit(select))

        # define text
        self.label = ttk.Label(self, text="Billy did not bring enough money. He is angry.", font='Calibri 16')

    def create_layout(self):
        self.label.grid(column=0, row=0)
        self.submit.grid(column=0, row=1)

        # Make label wrap text dynamically according to width of frame
        self.bind('<Configure>', lambda event: self.label.configure(wraplength=event.width - 20))

class PageGBANoA(Page):
    def __init__(self, parent, reset: Callable, select: Callable):
        super().__init__(parent, reset, select)
    
    def create_page(self, reset_function, select):
        ImageMain(self, 'images/GBANoA.png')
        MenuGBANoA(self, reset_function, select)


# * GBB1 ========================================================================================

class MenuGBB1(Menu):
    def __init__(self, parent, reset_function, select):
        super().__init__(parent, reset_function, select)

        # define grid
        self.columnconfigure(0, weight=1, uniform='a')
        self.rowconfigure((0, 1, 2), weight=1, uniform='a')

    # select pages according to selection
    def on_attack(self, select):
        # reduce health by 7.2%
        new_health = self.health.get() - 0.072

        if new_health < 0:
            new_health = 0
        
        # set health. if health is dead then next page
        self.health.set(new_health)
        if self.health.get() == 0 :
            select('GBB2')

    def create_widgets(self, select):
        # health variable
        self.health = tk.DoubleVar(value=1)

        # define health bar
        self.health_frame = ttk.Frame(self)
        self.health_label = ttk.Label(self.health_frame, text="Random dude's health:")
        self.health_bar = ttk.Progressbar(self.health_frame, variable=self.health, length=400, maximum=1)
        self.attack = ttk.Button(self, text='Click here to attack!', command=lambda: self.on_attack(select))

        # define text
        self.label = ttk.Label(self, text="The random dude dislikes Billy and wants to kill him! Fight back!", font='Calibri 16')

    def create_layout(self):
        # put label and health bar on frame
        self.health_label.pack()
        self.health_bar.pack()

        # put all on menu
        self.label.grid(column=0, row=0)
        self.health_frame.grid(column=0, row=1)
        self.attack.grid(column=0, row=2, sticky='nsew')

        # Make label wrap text dynamically according to width of frame
        self.bind('<Configure>', lambda event: self.label.configure(wraplength=event.width - 20))

class PageGBB1(Page):
    def __init__(self, parent, reset: Callable, select: Callable):
        super().__init__(parent, reset, select)
    
    def create_page(self, reset_function, select):
        ImageMain(self, 'images/GBB1.png')
        MenuGBB1(self, reset_function, select)


# * GBB2 ===========================================================================================

class MenuGBB2(Menu):
    def __init__(self, parent, reset_function, select):
        super().__init__(parent, reset_function, select)

        # define grid
        self.columnconfigure(0, weight=1, uniform='a')
        self.rowconfigure((0, 1), weight=1, uniform='a')
    

    # select pages according to selection
    def on_submit(self, select):
        if self.scale_value.get() > 0.80:
            select('GBB2A')
        elif self.scale_value.get() > 0.5:
            select('GBB2B')
        else:
            select('GBB2C')

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
        self.label = ttk.Label(self, text='Billy almost kills the random dude. He just needs one more hit; how hard should Billy strike him?', font='Calibri 16')

    def create_layout(self):
        # put button and scale on scale frame
        self.scale.pack()
        self.submit.pack()

        # put label and scale frame on menu
        self.label.grid(column=0, row=0)
        self.scale_frame.grid(column=0, row=1)
        # Make label wrap text dynamically according to width of frame
        self.bind('<Configure>', lambda event: self.label.configure(wraplength=event.width - 20))

class PageGBB2(Page):
    def __init__(self, parent, reset: Callable, select: Callable):
        super().__init__(parent, reset, select)
    
    def create_page(self, reset_function, select):
        ImageMain(self, 'images/GBB2.png')
        MenuGBB2(self, reset_function, select)


# ? Winning/losing screens

# * GBB2A ==========================================================================================

class MenuGBB2A(Menu):
    def __init__(self, parent, reset_function, select):
        super().__init__(parent, reset_function, select)

        # define grid
        self.columnconfigure(0, weight=1, uniform='a')
        self.rowconfigure((0, 1), weight=1, uniform='a')

    def create_widgets(self, select):
        # define text
        self.label = ttk.Label(self, text="Billy hit the random dude too hard that he fell into the sea and the gem is forever lost!", font='Calibri 16')

    def create_layout(self):
        self.label.grid(column=0, row=0)

        # Make label wrap text dynamically according to width of frame
        self.bind('<Configure>', lambda event: self.label.configure(wraplength=event.width - 20))

class PageGBB2A(Page):
    def __init__(self, parent, reset: Callable, select: Callable):
        super().__init__(parent, reset, select)
    
    def create_page(self, reset_function, select):
        ImageMain(self, 'images/lose.png')
        MenuGBB2A(self, reset_function, select)


# * GBB2B ==========================================================================================

class MenuGBB2B(Menu):
    def __init__(self, parent, reset_function, select):
        super().__init__(parent, reset_function, select)

        # define grid
        self.columnconfigure(0, weight=1, uniform='a')
        self.rowconfigure((0, 1), weight=1, uniform='a')


    def create_widgets(self, select):
        # define text
        self.label = ttk.Label(self, text="Billy killed the guy and got his gem!", font='Calibri 16')

    def create_layout(self):
        self.label.grid(column=0, row=0)

        # Make label wrap text dynamically according to width of frame
        self.bind('<Configure>', lambda event: self.label.configure(wraplength=event.width - 20))

class PageGBB2B(Page):
    def __init__(self, parent, reset: Callable, select: Callable):
        super().__init__(parent, reset, select)
    
    def create_page(self, reset_function, select):
        ImageMain(self, 'images/win.png')
        MenuGBB2B(self, reset_function, select)

# * GBB2C ==========================================================================================

class MenuGBB2C(Menu):
    def __init__(self, parent, reset_function, select):
        super().__init__(parent, reset_function, select)

        # define grid
        self.columnconfigure(0, weight=1, uniform='a')
        self.rowconfigure((0, 1), weight=1, uniform='a')

    def create_widgets(self, select):

        # define text
        self.label = ttk.Label(self, text="Billy's strike wasn't strong enough; the guy kills Billy!", font='Calibri 16')

    def create_layout(self):
        self.label.grid(column=0, row=0)

        # Make label wrap text dynamically according to width of frame
        self.bind('<Configure>', lambda event: self.label.configure(wraplength=event.width - 20))

class PageGBB2C(Page):
    def __init__(self, parent, reset: Callable, select: Callable):
        super().__init__(parent, reset, select)
    
    def create_page(self, reset_function, select):
        ImageMain(self, 'images/lose.png')
        MenuGBB2C(self, reset_function, select)


# * win ==========================================================================================

class MenuWin(Menu):
    def __init__(self, parent, reset_function, select):
        super().__init__(parent, reset_function, select)

        # define grid
        self.columnconfigure(0, weight=1, uniform='a')
        self.rowconfigure((0, 1), weight=1, uniform='a')

    def create_widgets(self, select):

        # define text
        self.label = ttk.Label(self, text="Billy finds the gem and wins!", font='Calibri 16')

    def create_layout(self):
        self.label.grid(column=0, row=0)

        # Make label wrap text dynamically according to width of frame
        self.bind('<Configure>', lambda event: self.label.configure(wraplength=event.width - 20))

class PageWin(Page):
    def __init__(self, parent, reset: Callable, select: Callable):
        super().__init__(parent, reset, select)
    
    def create_page(self, reset_function, select):
        ImageMain(self, 'images/win.png')
        MenuWin(self, reset_function, select)


# * lose ==========================================================================================

class MenuLose(Menu):
    def __init__(self, parent, reset_function, select):
        super().__init__(parent, reset_function, select)

        # define grid
        self.columnconfigure(0, weight=1, uniform='a')
        self.rowconfigure((0, 1), weight=1, uniform='a')

    def create_widgets(self, select):

        # define text
        self.label = ttk.Label(self, text="Billy fails to find the gem and never makes it out!", font='Calibri 16')

    def create_layout(self):
        self.label.grid(column=0, row=0)

        # Make label wrap text dynamically according to width of frame
        self.bind('<Configure>', lambda event: self.label.configure(wraplength=event.width - 20))

class PageLose(Page):
    def __init__(self, parent, reset: Callable, select: Callable):
        super().__init__(parent, reset, select)
    
    def create_page(self, reset_function, select):
        ImageMain(self, 'images/lose.png')
        MenuLose(self, reset_function, select)