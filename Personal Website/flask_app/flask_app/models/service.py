from flask_app.models.user import User
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL


db = 'andrewwebsite_db'

class Service:
    def __init__( self , data ):
        self.id = data['id']
        self.location = data['location']
        self.description = data['description']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.creator = None