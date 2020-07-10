"""
This file is part of the FJournal Project.
Copyright © 2020, Daniele Penazzo. All Rights Reserved.
The use of this code is governed by the MIT license attached.
See the LICENSE file for the full license.

Created on: 2020-07-02

Author: Penaz
"""
from sqlalchemy import Column, Integer, String, Float
from .common import Base


class Food(Base):
    __tablename__ = 'food'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    reference_qty = Column(Float)
    calories = Column(Float)
    carb = Column(Float)
    fat = Column(Float)
    protein = Column(Float)
    sugar = Column(Float)
    fiber = Column(Float)

    def __repr__(self):
        return "<Food(name=%s)>" % self.name
