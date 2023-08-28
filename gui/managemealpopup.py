"""
This file is part of the FJournal Project.
Copyright © 2019-2020, Daniele Penazzo. All Rights Reserved.
The use of this code is governed by the MIT license attached.
See the LICENSE file for the full license.

Created on: 2020-07-10

Author: Penaz
"""
from tkinter import ttk
import tkinter as tk
from models import Meal
from models.session import SESSIONMAKER
from gui import AddMealPopup


class ManageMealPopup(ttk.Frame):
    """
    Defines a popup for entering meals
    """

    def __init__(self, master=None):
        """
        Constructor of the class
        """
        super().__init__(master)
        self.master = master
        self.session = SESSIONMAKER()
        self.meals = self.session.query(Meal).all()
        self.grid(row=0, column=0)
        self.create_widgets()

    def create_widgets(self):
        """
        Creates the widgets for the popup
        """
        self.widgets = []
        for index, meal in enumerate(self.meals):
            self.widgets.append(ttk.Label(self, text=meal.name))
            self.widgets[index].grid(row=index, column=0)
        self.addbtn = ttk.Button(self,
                                 text="Add New Meal",
                                 command=self.add_meal)
        self.addbtn.grid(row=len(self.widgets)+1, column=0)

    def add_meal(self):
        """
        Opens the Add Meal popup
        """
        child = tk.Toplevel()
        child.title("Add new Meal")
        AddMealPopup(child, self.session)
