from flask import Flask, render_template, request, make_response, redirect
import hashlib
import sqlite3
app = Flask(__name__, template_folder="app/ui")
from app.views import index
from app.src import validateReg
from app.src import validateLogin
