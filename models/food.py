"""
This file is part of the FJournal Project.
Copyright © 2020-2023, Daniele Penazzo. All Rights Reserved.
The use of this code is governed by the MIT license attached.
See the LICENSE file for the full license.

Created on: 2023-08-14

Author: Penaz
"""
from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped, mapped_column
from .common import Base


class Food(Base):
    """
    Defines a food to be saved
    """
    __tablename__ = 'food'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(150))
    reference_qty: Mapped[float] = mapped_column(Float)
    calories: Mapped[float] = mapped_column(Float)
    carb: Mapped[float] = mapped_column(Float)
    fat: Mapped[float] = mapped_column(Float)
    protein: Mapped[float] = mapped_column(Float)
    sugar: Mapped[float] = mapped_column(Float)
    fiber: Mapped[float] = mapped_column(Float)

    def __repr__(self):
        return f"<Food(name={self.name})>"
