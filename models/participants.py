"""User model"""
from sqlalchemy import Column, Integer, BigInteger, ForeignKey, DateTime, Float, VARCHAR
from datetime import datetime

from models.db import Model
from models.base_object import BaseObject
import numpy


class Participants(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    participant_id = Column(Integer, nullable=False)
    block_id       = Column(Integer, nullable=False)
    block_number   = Column(Integer, nullable=False)

    prolific_id     = Column(VARCHAR(length=200))
    chosen_symbols_training = Column(VARCHAR(length=200))
    chosen_positions_training = Column(VARCHAR(length=200))
    observed_rewards_training  = Column(VARCHAR(length=200))
    correct_symbols_training  = Column(VARCHAR(length=200))
    reaction_time_training    = Column(VARCHAR(length=200))

    chosen_symbols_testing = Column(VARCHAR(length=200))
    chosen_positions_testing = Column(VARCHAR(length=200))

    date_time  = Column(VARCHAR(length=200))

    def get_id(self):
        return str(self.id)

    def get_prolific_id(self):
        return str(self.prolific_id)

    def get_participant_id(self):
        return str(self.participant_id)

    def get_block_id(self):
        return str(self.block_id)

    def get_block_number(self):
        return str(self.block_number)

    def get_chosen_symbols_training(self):
        return str(self.chosen_symbols_training)

    def get_chosen_positions_training(self):
        return str(self.chosen_positions_training)

    def get_observed_rewards_training(self):
        return str(self.observed_rewards_training)

    def get_correct_symbols_training(self):
        return str(self.correct_symbols_training)

    def get_chosen_symbols_testing(self):
        return str(self.chosen_symbols_testing)

    def get_chosen_positions_testing(self):
        return str(self.chosen_positions_testing)

    def get_reaction_time_training(self):
        return str(self.reaction_time_training)

    def get_datetime(self):
        return str(self.date_time)


    def errors(self):
        errors = super(Participants, self).errors()
        return errors
