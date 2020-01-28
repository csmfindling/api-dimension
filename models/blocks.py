"""User model"""
from sqlalchemy import Column, Integer, BigInteger, ForeignKey, DateTime, Float, VARCHAR
from datetime import datetime

from models.db import Model
from models.base_object import BaseObject
import numpy


class Blocks(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    left_symbol  = Column(VARCHAR(length=100), nullable=False)
    right_symbol = Column(VARCHAR(length=100), nullable=False)
        
    rewards_high   = Column(VARCHAR(length=100), nullable=False)
    rewards_low    = Column(VARCHAR(length=100), nullable=False)
    correct_side   = Column(VARCHAR(length=500), nullable=False)    

    correct_symbols   = Column(VARCHAR(length=20), nullable=False)
    correct_dimension = Column(Integer, nullable=False)
    correct_feature   = Column(Integer, nullable=False)

    def get_id(self):
        return str(self.id)

    def get_left_symbol(self):
        return str(self.left_symbol)

    def get_right_symbol(self):
        return str(self.right_symbol)

    def get_rewards_high(self):
        return str(self.rewards_high)

    def get_rewards_low(self):
        return str(self.rewards_low)

    def get_correct_side(self):
        return str(self.correct_side)

    def get_correct_symbols(self):
        return str(self.correct_symbols)

    def get_correct_dimension(self):
        return str(self.correct_dimension)

    def get_correct_feature(self):
        return str(self.correct_feature)

    def errors(self):
        errors = super(Blocks, self).errors()
        return errors
