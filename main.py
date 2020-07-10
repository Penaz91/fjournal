#!/usr/bin/env python
"""
This file is part of the FJournal Project.
Copyright © 2020, Daniele Penazzo. All Rights Reserved.
The use of this code is governed by the MIT license attached.
See the LICENSE file for the full license.

Created on: 2020-07-03

Author: Penaz
"""
import tkinter as tk
from datetime import date
from tkinter import ttk
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Meal, Food, Entry, Base
from gui import Calendar, WeightEntryPopup


class Application(ttk.Frame):
    def __init__(self, master=None):
        """
        Initializes the class
        """
        super().__init__(master)
        self.engine = create_engine("sqlite:///db.sqlite", echo=True)
        self.sessionmaker = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)
        self.master = master
        self.grid(row=0, column=0)
        self.create_menus()
        self.create_widgets()

    def create_menus(self):
        """
        Prepares the function menus
        """
        menu = tk.Menu(self)
        # File Menu
        filemenu = tk.Menu(menu, tearoff=0)
        filemenu.add_command(label="Quit", command=self.master.quit)
        # Weight Menu
        weightmenu = tk.Menu(menu, tearoff=0)
        weightmenu.add_command(label="Add Weight Entry",
                               command=self.open_weight_popup)
        # Add menu cascades
        menu.add_cascade(label="File", menu=filemenu)
        menu.add_cascade(label="Weight", menu=weightmenu)
        self.master.configure(menu=menu)

    def create_widgets(self):
        """
        Creates the widgets for the application
        """
        # Left sidebar
        self.sidebar = ttk.Frame(self)
        self.sidebar.grid(column=0, row=0, sticky="nsw")
        # Calendar Container
        self.calendarcontainer = ttk.Frame(self.sidebar)
        self.calendarcontainer.grid(row=0, column=0)
        # Calendar
        self.calendar = Calendar(self.calendarcontainer, self.echo)
        self.calendar.grid(row=0, column=0, sticky="nw")
        # Deatils of today
        self.day_details = ttk.Frame(self.sidebar)
        self.day_details.grid(row=1, column=0, sticky="sw")
        # Test button to show layout
        self.test_btnn = ttk.Button(self.day_details)
        self.test_btnn["text"] = "This is a test_Left"
        self.test_btnn.grid(row=0, column=0, sticky="w")
        # Right (content)
        self.content = ttk.Frame(self)
        self.content.grid(column=1, row=0)
        # Test button to show layout
        self.add_weight_btn = ttk.Button(self.content)
        self.add_weight_btn["text"] = "Add a new weight entry"
        self.add_weight_btn["command"] = self.open_weight_popup
        self.add_weight_btn.grid(column=1, row=0)
        self.test_btn = ttk.Button(self.content)
        self.test_btn["text"] = "This is a test"
        self.test_btn.grid(column=0, row=0)

    def open_weight_popup(self):
        """
        Opens the weight popup
        """
        child = tk.Toplevel()
        child.title("Insert new weight entry")
        WeightEntryPopup(child, self.date, self.sessionmaker())

    def echo(self, year, month, day):
        self.date = date(year=year, month=month, day=day)
        print(f"{year}/{month}/{day}")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("FJournal")
    app = Application(master=root)
    app.mainloop()
