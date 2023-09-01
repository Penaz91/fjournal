"""
This file is part of the FJournal Project.
Copyright © 2023, Daniele Penazzo. All Rights Reserved.
The use of this code is governed by the MIT license attached.
See the LICENSE file for the full license.

Created on: 2023-09-01

Author: Penaz
"""
from tkinter import ttk
from datetime import date
from gui import Calendar


class Sidebar(ttk.Frame):
    """
    The main sidebar, containing a calendar
    """
    def __init__(self, parent=None):
        """
        Constructor
        """
        super().__init__(parent)
        self.parent = parent
        self.container = ttk.Frame(self)
        self.container.grid(row=0, column=0)
        self.calendar = Calendar(self.container, self.echo)
        self.calendar.grid(row=0, column=0, sticky="nw")

    def echo(self, year, month, day):
        self.selected_date = date(year=year, month=month, day=day)
        print(f"{year}/{month}/{day}")
