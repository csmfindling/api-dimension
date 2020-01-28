"""User model"""
from sqlalchemy import Column, Integer, BigInteger, ForeignKey, DateTime, Float, VARCHAR
from datetime import datetime

from models.db import Model
from models.base_object import BaseObject
import numpy


class ParticipantsBlocks(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    participant_id = Column(BigInteger, nullable=False)

    blocks_ids = Column(VARCHAR(length=100), nullable=False)

    correct_dimension = Column(VARCHAR(length=100), nullable=False)

    unidimensional_block = Column(VARCHAR(length=100), nullable=False)


    def get_id(self):
        return str(self.id)

    def get_blocks_ids(self):
        return str(self.blocks_ids)

    def get_unidimensional_blocks(self):
        return str(self.unidimensional_block)

    def errors(self):
        errors = super(ParticipantsBlocks, self).errors()
        return errors
