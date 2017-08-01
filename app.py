from flask import Flask
from flask_restful import Api
from resources.todos import Todo, TodoList
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

api.add_resource(Todo, '/api/todos/<int:id>')
api.add_resource(TodoList, '/api/todos')

db.init_app(app)
app.run(port=5000, debug=True)
