"""users routes"""
from flask import current_app as app, jsonify, request

# from domain.recommendation import AddRecommendation, DiscoverNewRecommendations
from models import BaseObject, Participants, db
from collections import OrderedDict
import numpy
import json
import glob
from sqlalchemy.sql.expression import func

@app.route("/participants/create/<participant_id>/<block_id>/<prolific_id>", methods=["POST", "GET"])
def create_participant(participant_id, block_id, prolific_id):
    content     = request.json        
    participant = Participants()

    participant.participant_id = int(participant_id)
    participant.block_id       = int(block_id)
    participant.block_number   = int(content['block_number'])

    participant.prolific_id = str(prolific_id)
    participant.chosen_symbols_training   = str(content['chosen_symbols'])
    participant.chosen_positions_training = str(content['chosen_positions'])
    participant.observed_rewards_training = str(content['observed_rewards'])
    participant.correct_symbols_training  = str(content['correct_symbols'])
    participant.reaction_time_training    = str(content['reaction_times'])
    participant.chosen_symbols_testing    = ''
    participant.chosen_positions_testing  = ''
    participant.date_time = str(content['date_time'])

    BaseObject.check_and_save(participant)

    result = dict({"success": "yes"})    

    return jsonify(result)

@app.route("/participants/last_participant_id/", methods=["GET"])
def get_last_participant_id():
    query  = db.db.session.query(func.max(Participants.participant_id)).first_or_404()
    if query[0] is not None:
        result = dict({"new_participant_id": str(int(query[0]) + 1)})
    else:
        result = dict({"new_participant_id": str(1)})
    return jsonify(result)

@app.route("/participants/get_observed_rewards_training/<prolific_id>", methods=["GET"])
def get_observed_rewards_training(prolific_id):
    query                   = Participants.query.filter_by(prolific_id=prolific_id)    
    participants_score      = query.all()
    result                  = {}
    rewards_over_blocks     = numpy.concatenate([numpy.array(participants_score[i].get_observed_rewards_training()[1:-1].split(',')[-2:]) for i in range(len(participants_score))])
    result['score']         = str(rewards_over_blocks)
    return jsonify(result)


@app.route('/participants/score/<prolific_id>', methods=['GET'])
def get_participant_score(prolific_id):
    query                   = Participants.query.filter_by(prolific_id=prolific_id)    
    participants_score      = query.all()
    result                  = {}

    rewards_over_blocks     = numpy.concatenate([numpy.array(participants_score[i].get_observed_rewards_training()[1:-1].split(',')[-2:], dtype=numpy.float) for i in range(len(participants_score))])
    result['score']         = str(numpy.round((rewards_over_blocks.mean() - 40)/20. * 100))[:-2]

    return jsonify(result), 200 # json.dumps(result)

