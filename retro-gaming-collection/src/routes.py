from flask import Blueprint, request, jsonify
from models import Game

routes = Blueprint('routes', __name__)

@games.route('/games', methods=['GET'])
def get_games():
    games = Game.get_all()
    return jsonify(games), 200

@games.route('/games', methods=['POST'])
def create_game():
    data = request.json
    new_game = Game.create(data['title'], data['genre'], data['release_year'])
    return jsonify(new_game), 201

@games.route('/games/<int:game_id>', methods=['PUT'])
def update_game(game_id):
    data = request.json
    updated_game = Game.update(game_id, data['title'], data['genre'], data['release_year'])
    return jsonify(updated_game), 200

@games.route('/games/<int:game_id>', methods=['DELETE'])
def delete_game(game_id):
    Game.delete(game_id)
    return jsonify({'message': 'Game deleted successfully'}), 204