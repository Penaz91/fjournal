"""
This file is part of the FJournal Project.
Copyright © 2020-2023, Daniele Penazzo. All Rights Reserved.
The use of this code is governed by the MIT license attached.
See the LICENSE file for the full license.

Created on: 2023-08-14

Author: Penaz
"""
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from .common import Base


class Meal(Base):
    """
    A meal instance where you can save many entries
    """
    __tablename__ = 'meal'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)

    def __repr__(self):
        return f"<Meal(name={self.name})>"
