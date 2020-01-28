"""User model"""
from sqlalchemy import Column, Integer, BigInteger, ForeignKey, DateTime, Float, VARCHAR
from datetime import datetime

from models.db import Model
from models.base_object import BaseObject
import numpy


class ParticipantsSymbols(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    participant_id = Column(BigInteger, nullable=False)
    block_number   = Column(BigInteger, nullable=False)

    shapes_of_interest = Column(VARCHAR(length=20), nullable=False)
    colors_of_interest = Column(VARCHAR(length=20), nullable=False)
    grates_of_interest = Column(VARCHAR(length=20), nullable=False)


    def get_id(self):
        return str(self.id)

    def get_shapes_of_interest(self):
        return str(self.shapes_of_interest)

    def get_colors_of_interest(self):
        return str(self.colors_of_interest)

    def get_grates_of_interest(self):
        return str(self.grates_of_interest)

    def errors(self):
        errors = super(ParticipantsSymbols, self).errors()
        return errors
