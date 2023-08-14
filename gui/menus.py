"""
This file is part of the FJournal Project.
Copyright © 2020-2023, Daniele Penazzo. All Rights Reserved.
The use of this code is governed by the MIT license attached.
See the LICENSE file for the full license.

Created on: 2023-08-14

Author: Penaz
"""
import tkinter as tk

def create_menus(main_frame):
    """
    Prepares the function menus
    """
    menu = tk.Menu(main_frame)
    # File Menu
    filemenu = tk.Menu(menu, tearoff=0)
    filemenu.add_command(label="Quit", command=main_frame.master.quit)
    # Weight Menu
    weightmenu = tk.Menu(menu, tearoff=0)
    weightmenu.add_command(label="Add Weight Entry",
                            command=main_frame.open_weight_popup)
    # Journaling Menu
    journalmenu = tk.Menu(menu, tearoff=0)
    journalmenu.add_command(label="Manage Meals",
                            command=main_frame.open_meal_record_popup)
    # Charts Menu
    chartmenu = tk.Menu(menu, tearoff=0)
    chartmenu.add_command(label="Sorry Nothing")
    # Add menu cascades
    menu.add_cascade(label="File", menu=filemenu)
    menu.add_cascade(label="Weight", menu=weightmenu)
    menu.add_cascade(label="Journaling", menu=journalmenu)
    menu.add_cascade(label="Charts", menu=chartmenu)
    main_frame.master.configure(menu=menu)
