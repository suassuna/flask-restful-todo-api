from flask_restful import Resource, reqparse
from flask import jsonify
from datetime import datetime

class Todo(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('description',
            required=True,
            help='This field cannot be left blank.')
        self.parser.add_argument('done',
            required=True,
            type=bool,
            help='This field cannot be left blank.')
        self.parser.add_argument('createdAt',
            required=True,
            type=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S.%fZ'),
            help='This field cannot be left blank.')

    def get(self, id):
        return { 'todo': id }

    def put(self, id):
        data = self.parser.parse_args()

        return jsonify({
            'message': 'updated',
            'description': data['description'],
            'done': data['done'],
            'createdAt': data['createdAt']
        })

    def delete(self, id):
        return { 'deleted': id }


class TodoList(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('description',
            required=True,
            help='This field cannot be left blank.')
        self.parser.add_argument('done',
            type=bool,
            default=False)
        self.parser.add_argument('createdAt',
            type=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S.%fZ'),
            default=datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ'))

    def get(self):
        return {'message': 'Got it!'}

    def post(self):
        data = self.parser.parse_args()

        return jsonify({
            'message': 'added',
            'description': data['description'],
            'done': data['done'],
            'createdAt': data['createdAt']
        })
