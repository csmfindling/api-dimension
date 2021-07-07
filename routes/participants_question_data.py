"""users routes"""
from flask import current_app as app, jsonify, request

from models import ParticipantsQuestionData, BaseObject, db
from collections import OrderedDict
import numpy
import json
import glob
from datetime import datetime
import numpy as np 
from sqlalchemy.sql.expression import func


@app.route("/participants_question_data/create/<participant_id>/<block_id>/<prolific_id>", methods=["POST","GET"])
def create_question_participant(participant_id,block_id,prolific_id):
     content     = request.json        
     participant = ParticipantsQuestionData()

     participant.participant_id          = int(participant_id)
     participant.prolific_id             = str(prolific_id)
     participant.study_id                = str(content['study_id'])
     participant.block_number            = int(content['block_number'])
     participant.block_name              = str(content['block_name'])  
     participant.question_ids            = str(content['question_ids'])
     participant.answers                 = str(content['answers'])
     participant.date_time_survey_start  = str(content['date_time_survey_start'])
     participant.date_time_survey_end    = str(content['date_time_survey_end'])
     participant.date_time               = str(content['date_time'])
     participant.completed               = content['survey_completed'] 

     BaseObject.check_and_save(participant)

     result = dict({"success": "yes"})    

     return jsonify(result)

# To ge the data from this table 
@app.route('/participants_question_data/<participant_id>/<block_id>', methods=['GET'])

def get_participant_question_data(participant_id,block_id):

    query = ParticipantsQuestionData.query.filter(ParticipantsQuestionData.participant_id==participant_id, ParticipantsQuestionData.block_number==block_id)
    if query != None:
        print('Exists')
        
    block  = query.first_or_404()

    # format the query into a dictionnary first:
     
    result                   = {}

    arr_participant_id       = block.get_participant_id()[0].replace('  ',' ').split(' ')
    result['participant_id'] = arr_participant_id[0]

    arr_block                = block.get_block_number()[0].replace('  ',' ').split(' ')
    result['block_number']   = arr_block[0]

    arr_block_name           = block.get_block_name().replace('  ',' ').split(' ')
    result['block_name']     = arr_block_name

    arr_questions_ids        = np.array(block.get_question_ids()[1:-1].split(' '))
    result['question_ids']   = np.str(arr_questions_ids)
    
    arr_answers              = block.get_answers()[1:-1].replace('  ',' ').split(' ')
    result['answers']        = arr_answers

    arr_completed            = block.get_survey_completed()[0].replace('  ',' ')
    result['completed']      = arr_completed
    
    arr_date_time_survey_start       = block.get_date_time_survey_start()
    result['date_time_survey_start'] = arr_date_time_survey_start

    arr_date_time_survey_end         = block.get_date_time_survey_end()
    result['date_time_survey_end']   = arr_date_time_survey_end


    arr_date_time         = block.get_date_time()
    result['date_time']   = arr_date_time
    

    app.logger.info(result)
    return jsonify(result), 200 



