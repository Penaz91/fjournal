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
from tkinter import ttk
from models.session import SESSIONMAKER
from models import Meal
from gui import (
    WeightEntryPopup, ManageMealPopup, MealPanel, Sidebar
)
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
        self.selected_date = None
        create_menus(self)
        self.create_widgets()

    def create_widgets(self):
        """
        Creates the widgets for the application
        """
        # Left sidebar
        self.sidebar = Sidebar(self)
        self.sidebar.grid(column=0, row=0, sticky="nsw")
        # Deatils of today
        self.day_details = ttk.Frame(self.sidebar)
        self.day_details.grid(row=1, column=0, sticky="sw")
        # Test button to show layout
        self.test_btnn = ttk.Button(self.day_details)
        self.test_btnn["text"] = "This is a test_Left"
        self.test_btnn.grid(row=0, column=0, sticky="w")
        # Meal Panel
        self.meal_panel = MealPanel(self)
        self.meal_panel.grid(column=1, row=0)
        self.meal_panel.show_today()
        # Test button to show layout
        self.add_weight_btn = ttk.Button(self)
        self.add_weight_btn["text"] = "Add a new weight entry"
        self.add_weight_btn["command"] = self.open_weight_popup
        self.add_weight_btn.grid(column=2, row=0)

    def open_weight_popup(self):
        """
        Opens the weight popup
        """
        child = tk.Toplevel()
        child.title("Insert new weight entry")
        WeightEntryPopup(child, self.selected_date)

    def open_meal_record_popup(self):
        """
        Opens the "Register Meal" Popup
        """
        child = tk.Toplevel()
        child.title("Manage Meals")
        ManageMealPopup(child)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("FJournal")
    app = Application(master=root)
    app.mainloop()
