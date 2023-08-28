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
from models.session import SESSIONMAKER
from models import Meal, Food, Entry, Base
from gui import Calendar, WeightEntryPopup, ManageMealPopup
from gui.menus import create_menus


class Application(ttk.Frame):
    """
    The main application window
    """
    def __init__(self, master=None):
        """
        Initializes the class
        """
        super().__init__(master)
        self.sessionmaker = SESSIONMAKER
        self.master = master
        self.contentwidgets = []
        self.grid(row=0, column=0)
        create_menus(self)
        self.create_widgets()

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
        self.showToday()
        # Test button to show layout
        self.add_weight_btn = ttk.Button(self.content)
        self.add_weight_btn["text"] = "Add a new weight entry"
        self.add_weight_btn["command"] = self.open_weight_popup
        self.add_weight_btn.grid(column=1, row=0)

    def showToday(self):
        """
        Prepares and shows the "Today" section
        """
        session = self.sessionmaker()
        meals = session.query(Meal).all()
        self.nomealslbl = None
        self.refreshbtn = None
        if meals:
            for index, meal in enumerate(meals):
                self.contentwidgets.append(
                    ttk.Label(self.content, text=meal.name))
                self.contentwidgets[index].grid(row=index, column=0)
        else:
            self.nomealslbl = ttk.Label(self.content,
                                        text="No meals available")
            self.nomealslbl.grid(row=0, column=0)
            self.refreshbtn = ttk.Button(self.content,
                                         text="Refresh",
                                         command=self.showToday)
            self.refreshbtn.grid(row=1, column=0)

    def open_weight_popup(self):
        """
        Opens the weight popup
        """
        child = tk.Toplevel()
        child.title("Insert new weight entry")
        WeightEntryPopup(child, self.date)

    def open_meal_record_popup(self):
        """
        Opens the "Register Meal" Popup
        """
        child = tk.Toplevel()
        child.title("Manage Meals")
        ManageMealPopup(child)

    def echo(self, year, month, day):
        self.date = date(year=year, month=month, day=day)
        print(f"{year}/{month}/{day}")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("FJournal")
    app = Application(master=root)
    app.mainloop()
