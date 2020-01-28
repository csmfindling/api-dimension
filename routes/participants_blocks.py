"""users routes"""
from flask import current_app as app, jsonify, request

from models import ParticipantsBlocks, BaseObject
from collections import OrderedDict
import numpy

import json

@app.route('/participants_blocks/<participant_id>', methods=['GET'])
def get_participant_blocks(participant_id):
    query                   = ParticipantsBlocks.query.filter_by(id=participant_id)
    participants_blocks     = query.first_or_404()    
    result                  = {}

    arr_participants_blocks = numpy.array(participants_blocks.get_blocks_ids().replace('[  ', '[').replace('[ ', '[')[1:-1].replace('   ', ' ').replace('  ', ' ').replace('\n', '').split(' '))
    result['blocks_ids']    = { i : arr_participants_blocks[i] for i in range(0, len(arr_participants_blocks) ) }

    arr_unidimensional_blocks       = numpy.array(participants_blocks.get_unidimensional_blocks().replace('[  ', '[').replace('[ ', '[')[1:-1].replace('   ', ' ').replace('  ', ' ').replace('\n', '').split(' '))
    result['unidimensional_blocks'] = { i : arr_unidimensional_blocks[i] for i in range(0, len(arr_unidimensional_blocks) ) }

    return jsonify(result), 200 # json.dumps(result)
