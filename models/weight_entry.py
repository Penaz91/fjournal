"""
This file is part of the FJournal Project.
Copyright © 2020-2023, Daniele Penazzo. All Rights Reserved.
The use of this code is governed by the MIT license attached.
See the LICENSE file for the full license.

Created on: 2023-08-14

Author: Penaz
"""
import datetime
from sqlalchemy import Float, Date, Integer
from sqlalchemy.orm import Mapped, mapped_column
from .common import Base


class WeightEntry(Base):
    """
    A single entry for a person's weight
    """
    __tablename__ = 'weight_entry'

    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[datetime.date] = mapped_column(Date)
    weight: Mapped[float] = mapped_column(Float)

    def __repr__(self):
        return f"<Entry(date={self.date}, weight={self.weight})>"
