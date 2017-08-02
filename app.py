from flask import Flask
from flask_restful import Api
from resources.todos import Todo, TodoList
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response

api.add_resource(Todo, '/api/todos/<int:todo_id>')
api.add_resource(TodoList, '/api/todos')

db.init_app(app)
app.run(port=3003, debug=True)
