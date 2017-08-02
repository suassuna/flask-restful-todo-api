from flask_restful import Resource, reqparse
from flask import jsonify
from datetime import datetime
from models.todo import TodoModel

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

    def get(self, todo_id):
        todo = TodoModel.find_by_id(todo_id)

        if todo:
            return todo.json()
        return { 'message': 'Todo not found'}, 404

    def put(self, todo_id):
        todo = TodoModel.find_by_id(todo_id)

        if todo:
            data = self.parser.parse_args()

            todo.description = data['description']
            todo.done = data['done']
            todo.createdAt = data['createdAt']

            todo.save_to_db()

            return todo.json()

        return { 'message': 'Todo not found'}, 404

    def delete(self, todo_id):
        todo = TodoModel.find_by_id(todo_id)

        if todo:
            todo.delete_from_db()
        return { 'message': 'Todo deleted'}


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
            default=datetime.utcnow())

    def get(self):
        return [todo.json() for todo in TodoModel.query.all()]

    def post(self):
        data = self.parser.parse_args()
        todo = TodoModel(**data)

        try:
            todo.save_to_db()
        except Exception as exception:
            print(exception)
            return { 'message' : 'An error occured inserting the item.'}, 500

        return todo.json(), 201
