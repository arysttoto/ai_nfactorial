import joblib
from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from datetime import datetime
import sqlite3
from ruffier_calculations import result_comments
from diseases_dictionary import dict_diseases
from dict_symptoms import dict_symptoms
from workfile import func_disease_read, func_hospital_find, func_essay_summarize, func_classify_disease, image_generator
from creating_tables import func_add_essay, func_fetch_my_essays

app = Flask(__name__)
app.secret_key = 'nfactorialaicup2023'

# configure the session object
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["TIMEOUT"] = 50000
Session(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
