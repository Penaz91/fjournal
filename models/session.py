"""
This file is part of the FJournal Project.
Copyright © 2020-2023, Daniele Penazzo. All Rights Reserved.
The use of this code is governed by the MIT license attached.
See the LICENSE file for the full license.

Created on: 2023-08-14

Author: Penaz
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .common import Base

ENGINE = create_engine("sqlite:///db.sqlite", echo=True)

SESSIONMAKER = sessionmaker(ENGINE)

Base.metadata.create_all(ENGINE)
