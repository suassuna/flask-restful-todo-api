from db import db

class TodoModel(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80), nullable=False)
    done = db.Column(db.Boolean, nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False)

    def __init__(self, description, done, createdAt):
        self.description = description
        self.done = done
        self.createdAt = createdAt

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
