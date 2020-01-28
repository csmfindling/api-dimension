"""User model"""
from sqlalchemy import Column, Integer, BigInteger, ForeignKey, DateTime, Float, VARCHAR
from datetime import datetime

from models.db import Model
from models.base_object import BaseObject
import numpy


class Symbols(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    shape_id = Column(BigInteger, nullable=False)

    color_id = Column(BigInteger, nullable=False)

    grate_id = Column(BigInteger, nullable=False)


    def get_id(self):
        return str(self.id)

    def get_shape_id(self):
        return str(self.shape_id)

    def get_color_id(self):
        return str(self.color_id)

    def get_grate_id(self):
        return str(self.grate_id)


    def errors(self):
        errors = super(Symbols, self).errors()
        return errors
