"""
This file is part of the FJournal Project.
Copyright © 2020, Daniele Penazzo. All Rights Reserved.
The use of this code is governed by the MIT license attached.
See the LICENSE file for the full license.

Created on: 2020-07-02

Author: Penaz
"""
from sqlalchemy import Column, Integer, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from .common import Base


class Entry(Base):
    __tablename__ = 'entry'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    food_id = Column(Integer, ForeignKey('food.id'))
    meal_id = Column(Integer, ForeignKey('meal.id'))
    qty = Column(Float)
    calories = Column(Float)
    carb = Column(Float)
    fat = Column(Float)
    protein = Column(Float)
    sugar = Column(Float)
    fiber = Column(Float)

    food = relationship("Food")
    meal = relationship("Meal")

    def __repr__(self):
        return "<Entry(food=%s, meal=%s)>" % (self.food_id, self.meal_id)
