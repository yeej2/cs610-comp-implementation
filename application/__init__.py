from flask import Flask, url_for, request, render_template
app = Flask(__name__)

from application import db_connect
from application import index
from application import students
from application import teachers
from application import login
