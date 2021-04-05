from app import db
from datetime import datetime


class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(160), unique=False, nullable=False, default='NONE')
    is_active = db.Column(db.Boolean(), default=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<ToDo %r>' % self.task

