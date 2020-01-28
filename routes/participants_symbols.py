"""users routes"""
from flask import current_app as app, jsonify, request

# from domain.recommendation import AddRecommendation, DiscoverNewRecommendations
from models import ParticipantsSymbols, BaseObject, Symbols
from collections import OrderedDict
import numpy
import json
import glob

@app.route('/api/v1.0/test', methods=['GET'])
def test():
    return jsonify({'item': 'ok'}), 201

@app.route('/participants_symbols/get_symbols/<participant_id>/<block_number>', methods=['GET'])
def get_participant_symbols(participant_id, block_number):
    query                = ParticipantsSymbols.query.filter_by(participant_id=participant_id, block_number=block_number)
    participants_symbols = query.first_or_404()
    nb_possibleShapes    = 4
    nb_dimensions        = 3
    shapes_of_interest = numpy.sort(numpy.array(participants_symbols.get_shapes_of_interest()[1:-1].split(' '), dtype=numpy.int))
    colors_of_interest = numpy.sort(numpy.array(participants_symbols.get_colors_of_interest()[1:-1].split(' '), dtype=numpy.int))
    grates_of_interest = numpy.sort(numpy.array(participants_symbols.get_grates_of_interest()[1:-1].split(' '), dtype=numpy.int))

    allsymbols_indexes_raw = Symbols.query.all()
    allsymbols_indexes     = numpy.zeros([len(allsymbols_indexes_raw), nb_dimensions], dtype=numpy.int)
    for idx in range(len(allsymbols_indexes_raw)):
        allsymbols_indexes[idx] = int(allsymbols_indexes_raw[idx].get_shape_id()) - 1, int(allsymbols_indexes_raw[idx].get_color_id()) - 1, int(allsymbols_indexes_raw[idx].get_grate_id()) - 1
    
    # regular expression to get first symbols     
    regex_path_of_symbols = '../front/src/images/symbols/symbol_shape_[{0},{1}]_grate_[{2},{3}]_color_[{4},{5}].png'. \
                                                                format(shapes_of_interest[0], shapes_of_interest[1],  \
                                                                        grates_of_interest[0], grates_of_interest[1], \
                                                                        colors_of_interest[0], colors_of_interest[1])    

    paths_of_symbols  = glob.glob(regex_path_of_symbols)
    
    # app.logger.info(paths_of_symbols)
    # app.logger.info(allsymbols_indexes)
    
    all_of_interest   = numpy.concatenate((shapes_of_interest[:,numpy.newaxis], \
                                            colors_of_interest[:,numpy.newaxis], \
                                            grates_of_interest[:,numpy.newaxis]), axis=1)

    # app.logger.info(all_of_interest)

    pool_of_symbols           = {}
    for path in paths_of_symbols:
        indexes_of_features = numpy.array(list(map(lambda x: x[0], numpy.array(path.split('_'))[numpy.array([-5, -1, -3])])), dtype=numpy.int) # shape color grate
        # app.logger.info(indexes_of_features)
        temp_indexes        = numpy.zeros(nb_dimensions)
        for idx_dim in range(nb_dimensions):            
            temp_indexes[idx_dim] = numpy.where(indexes_of_features[idx_dim] == all_of_interest[:,idx_dim])[0][0]
        intelligent_index = numpy.where(numpy.sum(numpy.abs(allsymbols_indexes - temp_indexes[numpy.newaxis]), axis=1) == 0)[0][0] + 1
        # app.logger.info(str(intelligent_index))
        pool_of_symbols[str(intelligent_index)] = path.split('src/')[-1]

    # return result
    result                    = dict()
    result['pool_of_symbols'] = pool_of_symbols

    return jsonify(result), 200 # json.dumps(result)    
