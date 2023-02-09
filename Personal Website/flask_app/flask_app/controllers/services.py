from flask import redirect, render_template, request, session

from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.service import Service
from flask_app.models.user import User