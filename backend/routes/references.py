from flask import Blueprint, jsonify
import json
import os

references_bp = Blueprint('references', __name__)

def load_references():
    with open(os.path.join('data', 'references.json'), 'r') as f:
        return json.load(f)

@references_bp.route('/', methods=['GET'])
def get_all_references():
    try:
        references = load_references()
        return jsonify(references)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@references_bp.route('/<condition>', methods=['GET'])
def get_condition_references(condition):
    try:
        references = load_references()
        condition_refs = references.get(condition, [])
        
        if not condition_refs:
            return jsonify({'error': 'Condition not found'}), 404
            
        return jsonify(condition_refs)
    except Exception as e:
        return jsonify({'error': str(e)}), 500