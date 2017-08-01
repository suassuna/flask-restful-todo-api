from flask import Flask
from flask_restful import Api
from resources.todos import Todo, TodoList

app = Flask(__name__)
api = Api(app)

api.add_resource(Todo, '/api/todos/<int:id>')
api.add_resource(TodoList, '/api/todos')

app.run(port=5000, debug=True)
