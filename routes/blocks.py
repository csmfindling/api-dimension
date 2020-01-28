"""users routes"""
from flask import current_app as app, jsonify, request

# from domain.recommendation import AddRecommendation, DiscoverNewRecommendations
from models import Blocks, BaseObject
from collections import OrderedDict
import numpy
import json

@app.route('/test/', methods=['GET'])
def test():
    result = dict()
    result['test'] = 'test'
    return jsonify(result), 200


@app.route('/block/<block_id>', methods=['GET'])
def get_block(block_id):
    query                = Blocks.query.filter_by(id=block_id)
    block                = query.first_or_404()
    result               = dict()

    
    arr_left_symbol  = numpy.array(block.get_left_symbol()[1:-1].replace('  ', ' ').split(' '))
    arr_right_symbol = numpy.array(block.get_right_symbol()[1:-1].replace('  ', ' ').split(' '))

    arr_rewards_high = numpy.array(block.get_rewards_high()[1:-1].replace('  ', ' ').split(' '))
    arr_rewards_low  = numpy.array(block.get_rewards_low()[1:-1].replace('  ', ' ').split(' '))

    arr_correct_side   = numpy.array(block.get_correct_side()[1:-1].replace('  ', ' ').split(', '))

    result['left_symbol']  = { i : arr_left_symbol[i] for i in range(0, len(arr_left_symbol) ) }
    result['right_symbol'] = { i : arr_right_symbol[i] for i in range(0, len(arr_right_symbol) ) }
    result['rewards_high'] = { i : arr_rewards_high[i] for i in range(0, len(arr_rewards_high) ) }
    result['rewards_low']  = { i : arr_rewards_low[i] for i in range(0, len(arr_rewards_low) ) }
    result['correct_side'] = { i : arr_correct_side[i] for i in range(0, len(arr_correct_side) ) }

    result['correct_symbols'] = block.get_correct_symbols()
    result['correct_dimension'] = numpy.array(['shape', 'color', 'grate'])[int(block.get_correct_dimension()) - 1]
    result['correct_feature'] = block.get_correct_feature()

    return jsonify(result), 200
