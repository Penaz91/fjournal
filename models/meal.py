"""
This file is part of the FJournal Project.
Copyright © 2020, Daniele Penazzo. All Rights Reserved.
The use of this code is governed by the MIT license attached.
See the LICENSE file for the full license.

Created on: 2020-07-02

Author: Penaz
"""
from sqlalchemy import Column, Integer, String
from .common import Base


class Meal(Base):
    __tablename__ = 'meal'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<Meal(name=%s)>" % self.name
