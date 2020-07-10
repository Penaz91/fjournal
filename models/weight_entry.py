"""
This file is part of the FJournal Project.
Copyright © 2020, Daniele Penazzo. All Rights Reserved.
The use of this code is governed by the MIT license attached.
See the LICENSE file for the full license.

Created on: 2020-07-09

Author: Penaz
"""
from sqlalchemy import Column, Float, Date, Integer
from .common import Base


class WeightEntry(Base):
    __tablename__ = 'weight_entry'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    weight = Column(Float)

    def __repr__(self):
        return "<Entry(food=%s, meal=%s)>" % (self.food_id, self.meal_id)
