from marshmallow import Schema, fields

from src.setup_db import db


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
