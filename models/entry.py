"""
This file is part of the FJournal Project.
Copyright © 2020-2023, Daniele Penazzo. All Rights Reserved.
The use of this code is governed by the MIT license attached.
See the LICENSE file for the full license.

Created on: 2023-08-14

Author: Penaz
"""
import datetime
from typing import List
from sqlalchemy import Column, Integer, Float, ForeignKey, Date
from sqlalchemy.orm import relationship, mapped_column, Mapped
from .common import Base


class Entry(Base):
    """
    A single meal entry
    """
    __tablename__ = 'entry'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    date: Mapped[datetime.date] = mapped_column(Date)
    food_id: Mapped[int] = mapped_column(ForeignKey('food.id'))
    meal_id: Mapped[int] = mapped_column(ForeignKey('meal.id'))
    qty: Mapped[float] = mapped_column(Float)
    calories: Mapped[float] = mapped_column(Float)
    carb: Mapped[float] = mapped_column(Float)
    fat: Mapped[float] = mapped_column(Float)
    protein: Mapped[float] = mapped_column(Float)
    sugar: Mapped[float] = mapped_column(Float)
    fiber: Mapped[float] = mapped_column(Float)

    food: Mapped[List["Food"]] = relationship("Food")
    meal: Mapped[List["Meal"]] = relationship("Meal")

    def __repr__(self):
        return f"<Entry(food={self.food_id}, meal={self.meal_id})>"
