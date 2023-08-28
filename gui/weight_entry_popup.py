"""
This file is part of the FJournal Project.
Copyright © 2019-2020, Daniele Penazzo. All Rights Reserved.
The use of this code is governed by the MIT license attached.
See the LICENSE file for the full license.

Created on: 2020-07-09

Author: Penaz
"""
from datetime import datetime
from tkinter import ttk
import tkinter as tk
from models import WeightEntry
from models.session import SESSIONMAKER
from gui import Calendar


class WeightEntryPopup(ttk.Frame):
    """
    Defines a popup for entering weight
    """

    def __init__(self, master=None, date=None):
        """
        Constructor of the class
        """
        super().__init__(master)
        self.master = master
        self.date = tk.StringVar()
        self.weight = tk.DoubleVar()
        self.date.set(date.strftime("%Y-%m-%d"))
        self.grid(row=0, column=0)
        self.session = SESSIONMAKER()
        self.create_widgets()

    def create_widgets(self):
        """
        Creates the widgets for the popup
        """
        self.dateinputlbl = ttk.Label(self, text="Entry Date:")
        self.dateinputlbl.grid(row=0, column=0)
        self.dateinput = ttk.Entry(self, textvariable=self.date)
        self.dateinput.grid(row=0, column=1)
        self.dateinputbtn = ttk.Button(self, text="...")
        self.dateinputbtn["command"] = self.calendarPopup
        self.dateinputbtn.grid(row=0, column=2)
        self.weightinputlbl = ttk.Label(self, text="Weight:")
        self.weightinputlbl.grid(row=1, column=0)
        self.weightinput = ttk.Entry(self, textvariable=self.weight)
        self.weightinput.grid(row=1, column=1)
        self.confirmbtn = ttk.Button(self, command=self.confirm_entry)
        self.confirmbtn["text"] = "Confirm"
        self.confirmbtn["command"] = self.confirm_entry
        self.confirmbtn.grid(row=2, column=0, columnspan=2)

    def calendarPopup(self):
        """
        Pops out a calendar date selector
        """
        child = tk.Toplevel()
        child.title("Date Picker")
        Calendar(child, self.selectDate)

    def selectDate(self, year, month, day):
        """
        Selects a date from the calendar popup
        """
        self.date.set("{}-{}-{}".format(year, month, day))

    def confirm_entry(self):
        """
        Creates the DB Entry
        """
        we = WeightEntry(
            date=datetime.strptime(self.date.get(), "%Y-%m-%d"),
            weight=self.weight.get()
        )
        self.session.add(we)
        self.session.commit()
        self.master.destroy()
