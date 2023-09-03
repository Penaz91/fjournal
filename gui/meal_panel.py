from tkinter import ttk
from models.session import SESSIONMAKER
from models import Meal


class MealPanel(ttk.Frame):
    """
    Defines the meal panel, showing the meals of the selected day
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.nomealslbl = None
        self.refreshbtn = None
        self.widgets = []

    def show_today(self):
        """
        Prepares and shows the "Today" section
        """
        session = SESSIONMAKER()
        meals = session.query(Meal).all()
        if self.nomealslbl is not None:
            self.nomealslbl.destroy()
            self.nomealslbl = None
        if self.refreshbtn is not None:
            self.refreshbtn.destroy()
            self.refreshbtn = None
        if meals:
            for index, meal in enumerate(meals):
                self.widgets.append(
                    ttk.Label(self, text=meal.name))
                self.widgets[index].grid(row=index, column=0)
        else:
            self.nomealslbl = ttk.Label(
                self,
                text="No meals available"
            )
            self.nomealslbl.grid(row=0, column=0)
            self.refreshbtn = ttk.Button(
                self,
                text="Refresh",
                command=self.show_today
            )
            self.refreshbtn.grid(row=1, column=0)
        self.tkraise()
