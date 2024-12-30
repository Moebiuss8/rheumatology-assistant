from flask import Blueprint, request, jsonify
from utils.bayes import calculate_posttest_probability
from utils.pretest_calculator import get_pretest_probability

probabilities_bp = Blueprint('probabilities', __name__)

@probabilities_bp.route('/pretest', methods=['POST'])
def calculate_pretest():
    data = request.get_json()
    
    try:
        condition = data['condition']
        risk_factors = data.get('risk_factors', [])
        
        probability = get_pretest_probability(condition, risk_factors)
        return jsonify({'probability': probability})
        
    except KeyError as e:
        return jsonify({'error': f'Missing required field: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@probabilities_bp.route('/posttest', methods=['POST'])
def calculate_posttest():
    data = request.get_json()
    
    try:
        pretest_prob = data['pretest_probability']
        sensitivity = data['sensitivity']
        specificity = data['specificity']
        test_result = data['test_result']
        
        probability = calculate_posttest_probability(
            pretest_prob,
            sensitivity,
            specificity,
            test_result
        )
        
        return jsonify({'probability': probability})
        
    except KeyError as e:
        return jsonify({'error': f'Missing required field: {str(e)}'}), 400
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500