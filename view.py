from tkinter import *
import controller

class GUI:
    def __init__(self, window):
        '''
        Show's the main menu and holds all base values needed to run
        smoothly.
        :param window:
        '''
        # Base variables
        self.window = window
        self.frame_menu = None # This is here to allow you to click checkout first without any errors occuring
        self.sandwich_total = 0
        self.cookie_total = 0
        self.water_total = 0

        # Main Menu
        self.frame_main = Frame(self.window)
        self.label_main = Label(self.frame_main, text='Welcome to Michael\'s restaurant', font=60)
        self.frame_main.pack(pady=5, side='top')
        self.label_main.pack(pady=5, side='top')

        self.frame_question = Frame(self.window)
        self.label_question = Label(self.frame_question, text='Press shop if you would you like to order?', font=30)
        self.frame_question.pack(pady=5, side='top')
        self.label_question.pack(pady=5, side='top')

        self.frame_shop = Frame(self.window)
        self.order_button = Button(self.frame_shop, text="SHOP", font=80, command=self.clicked)
        self.checkout_button = Button(self.frame_shop, text="Checkout", font=80, command=self.checkout)
        self.frame_shop.pack(padx=30, pady=10, side='bottom')
        self.order_button.pack(padx=30, pady=10, side='left')
        self.checkout_button.pack(padx=30, pady=10, side='left')



    def clicked(self):
        '''
        Function to send into the menu of food items. Then to enter which item wanted and the quantity
        for each item in menu
        :param self:
        :return: None
        '''
        self.label_question.destroy()
        self.frame_menu = Frame(self.window)
        self.label_menu = Label(self.frame_menu, text='MENU', font=60)
        self.label_explanation = Label(self.frame_menu, text='Select what you would like to order!', font=60)
        self.frame_menu.pack(padx=10, side='top')
        self.label_menu.pack(padx=10, side='top')
        self.label_explanation.pack(padx=10, side='top')

        # Sandwich Menu Item
        self.frame_sandwich = Frame(self.window)
        self.label_sandwich = Label(self.frame_sandwich, text='Sandwich - $4.00ea', font=45)
        self.label_amount = Label(self.frame_sandwich, text='Enter Amount:', font=25)
        self.entry_sandwich = Entry(self.frame_sandwich, width=10)
        self.button_sandwich = Button(self.frame_sandwich, text="Order", font=80, command=self.order_sandwich)
        self.label_sandwich.pack(padx=10, side='left')
        self.label_amount.pack(padx=20, side='left')
        self.entry_sandwich.pack(padx=18, side='left')
        self.button_sandwich.pack(padx=40, side='left')
        self.frame_sandwich.pack(anchor='w', pady=20)

        # Cookie Menu Item
        self.frame_cookie = Frame(self.window)
        self.label_cookie = Label(self.frame_cookie, text='Cookie - $1.50ea', font=45)
        self.entry_cookie = Entry(self.frame_cookie, width=10)
        self.label_amount = Label(self.frame_cookie, text='Enter Amount:', font=25)
        self.button_cookie = Button(self.frame_cookie, text="Order", font=80, command=self.order_cookie)
        self.label_cookie.pack(padx=10, side='left')
        self.label_amount.pack(padx=42, side='left')
        self.entry_cookie.pack( side='left')
        self.button_cookie.pack(padx=50, side='left')
        self.frame_cookie.pack(anchor='w', pady=20)

        # Water Menu Item
        self.frame_water= Frame(self.window)
        self.label_water = Label(self.frame_water, text='Water - $1.00ea', font=45)
        self.label_amount = Label(self.frame_water, text='Enter Amount:', font=25)
        self.entry_water = Entry(self.frame_water, width=10)
        self.button_water = Button(self.frame_water, text="Order", font=80, command=self.order_water)
        self.label_water.pack(padx=10, side='left')
        self.label_amount.pack(padx=44, side='left')
        self.entry_water.pack(side='left')
        self.button_water.pack(padx=50, side='left')
        self.frame_water.pack(anchor='w', pady=20)

    def checkout(self):
        '''
        A function to close out the menu and show total amount spent and
        the quantity gathered.
        :param self:
        :return: None
        '''
        if self.frame_menu != None:
            self.frame_menu.destroy()
            self.frame_sandwich.destroy()
            self.frame_cookie.destroy()
            self.frame_water.destroy()
        self.frame_checkout = Frame(self.window)
        self.label_checkout = Label(self.frame_checkout, text='Total ordered', font=60)
        self.label_checkout.pack(padx=10, side='top')
        self.frame_checkout.pack(anchor='n', pady=10)

        self.frame_items = Frame(self.window)
        if self.sandwich_total > 0:
            self.label_sandwich_amount = Label(self.frame_items, text=f'Sandwich total is ${self.sandwich_total:.2f}', font=60)
            self.label_sandwich_amount.pack(padx=10, side='top')
        if self.cookie_total > 0:
            self.label_cookie_amount = Label(self.frame_items, text=f'Cookie total is ${self.cookie_total:.2f}', font=60)
            self.label_cookie_amount.pack(padx=10, side='top')
        if self.water_total > 0:
            self.label_water_amount = Label(self.frame_items, text=f'Water total is ${self.water_total:.2f}', font=60)
            self.label_water_amount.pack(padx=10, side='top')
        self.frame_items.pack(anchor='n', pady=10)

    def order_sandwich(self):
        '''
        This function runs when the user presses the order button for the sandwich option. It will grab the
        entry that had been put in and send it to another function to calculate it and send it back for it
        to be printed in the checkout screen.
        :return: None
        '''
        amount = self.entry_sandwich.get()
        self.sandwich_total = controller.get_sandwich(amount)

    def order_cookie(self):
        '''
        This function runs when the user presses the order button for the cookie option. It will grab the
        entry that had been put in and send it to another function to calculate it and send it back for it
        to be printed in the checkout screen.
        :return: None
        '''
        amount = self.entry_cookie.get()
        self.cookie_total = controller.get_cookie(amount)

    def order_water(self):
        '''
        This function runs when the user presses the order button for the water option. It will grab the
        entry that had been put in and send it to another function to calculate it and send it back for it
        to be printed in the checkout screen.
        :return: None
        '''
        amount = self.entry_water.get()
        self.water_total = controller.get_water(amount)

