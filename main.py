import time
import joblib
from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from datetime import datetime
import sqlite3
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from csv import writer
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

# @app.route('/healthcare')
# def healthcare():
#     db = sqlite3.connect('blog.db')
#     sql = db.cursor()
#     sql.execute(f"""SELECT * FROM hospitals WHERE continent = 'africa'""")
#     hospitals_africa = sql.fetchall()
#     sql.execute(f"""SELECT * FROM hospitals WHERE continent = 'europe'""")
#     hospitals_europe = sql.fetchall()
#     sql.execute(f"""SELECT * FROM hospitals WHERE continent = 'asia'""")
#     hospitals_asia = sql.fetchall()
#     sql.close()
#     return render_template('healthcare.html', hospitals_africa=hospitals_africa, hospitals_asia=hospitals_asia, hospitals_europe=hospitals_europe)

@app.route('/find-my-disease', methods=["POST", "GET"])
def find_my_disease():
    if request.method == 'POST':
        # take the list
        try:
            list_symptoms = request.form.getlist('symptom')
            list_symptoms_for_ai = [0] * 132
            for i in list_symptoms:
                list_symptoms_for_ai[dict_symptoms[i]] = 1
            loaded_model = joblib.load('decision_tree_model.joblib')
            y_pred = loaded_model.predict([list_symptoms_for_ai])
            session['symptom_based_prognosis'] = dict_diseases[list(list(y_pred)[0]).index(1)]
            return redirect('/my-prognosis')
        except Exception as ex:
            return f'Error: {ex}'
    else:
        return render_template('find-my-disease.html')

@app.route('/my-prognosis')
def my_prognosis():
    if session.get('symptom_based_prognosis'):
        return render_template('my_prognosis.html')
    else:
        return redirect('/find-my-disease')

@app.route('/find-my-hospital', methods=["POST", "GET"])
def find_my_hospital():
    if request.method == 'POST':
        hospitals_info = func_hospital_find(request.form.get('disease'), request.form.get('city'), request.form.get('country'))
        return render_template('find-hospital.html', hospitals=hospitals_info)
    else:
        return render_template('find-hospital.html')

@app.route('/read-about-diseases', methods=["POST", "GET"])
def read_about_diseases():
    if request.method == "POST":
        try:
            session['username'] = request.form.get('username')
            topic = request.form.get('disease-input')
            get_essay_ai = func_disease_read(topic)
            get_essay_summary = func_essay_summarize(get_essay_ai)
            disease_type = func_classify_disease(topic)
            image_url = image_generator(topic)
            func_add_essay(username=session['username'], topic=topic, essay=get_essay_ai, summary=get_essay_summary, disease_type=disease_type, image_url=image_url)
            return render_template('read_about_diseases.html', essay=get_essay_ai, topic=topic, disease_type=disease_type)
        except Exception as ex:
            return ex
    else:
        return render_template('read_about_diseases.html')

@app.route('/our-tests')
def our_tests():
    db = sqlite3.connect('blog.db')
    sql = db.cursor()
    sql.execute("""SELECT * FROM all_tests""")
    tests = sql.fetchall()
    return render_template('all_tests.html', tests=tests)

@app.route('/our-tests/2', methods=["POST", "GET"])
def ruffier_test():
    if request.method == "POST":
        session['name'] = request.form['Name']
        session['age'] = int(request.form['Age'])
        p1 = int(request.form['p1'])
        p2 = int(request.form['p2'])
        p3 = int(request.form['p3'])
        session['ruffier_test'] = result_comments((p1+p2+p3-200)/100, session['age'])
        return redirect('/our-tests/results')
    else:
        return render_template('ruffier-test.html')

@app.route('/our-tests/results')
def results():
    return render_template('results.html')

######## EXAMPLE OF A TEST BASED ON AI #########
# @app.route('/our-tests/1', methods=["POST", "GET"])
# def quick_test():
#     if request.method == 'POST':
#         answer1 = request.form['1']
#         answer2 = request.form['2']
#         answer3 = request.form['3']
#         answer4 = request.form['4']
#         answer5 = request.form['5']
#         answer6 = request.form['6']
#         answer7 = request.form['7']
#         answer8 = request.form['8']
#         answer9 = request.form['9']
#         ######################################################################################
#         result = model.predict(x_test)
#         List = [int(answer1), int(answer2), int(answer3), int(answer4), int(answer5), int(answer6), int(answer7), int(answer8),int(answer9), int(result[0])]
#         if result == 1:
#             recommendations = 'Low risk, congratulations!'
#         elif result == 2:
#             recommendations = 'Average risk, you should make check ups often!'
#         else:
#             recommendations = 'High risk, you should go to a hospital urgently!'
#         ######################################################################################
#         # add the object to the csv file
#         with open('data.csv', 'a') as file:
#             writer_object = writer(file)
#
#             # Pass the list as an argument into
#             # the writerow()
#             writer_object.writerow(List)
#
#             # Close the file object
#             file.close()
#
#         return render_template('results.html', result=result, recommendations=recommendations)
#     else:
#         return render_template('quick-test.html')
@app.route('/my-articles')
def my_articles():
    if session.get('name'):
        data = func_fetch_my_essays(session['username'])
        return render_template('my-articles.html', data=data)
    else:
        return redirect('/my-prognosis')

# @app.route('/articles')
# def solutions():


# for future use, continuing to read the article
# @app.route('/articles/<int:id>')
# def view(id):
#     db = sqlite3.connect('blog.db')
#     sql = db.cursor()
#     sql.execute(f"""SELECT * FROM articles WHERE id = {id}""")
#     article = sql.fetchone()
#     db.commit()
#     return render_template('view.html', article=article)


@app.route('/create-article', methods=["POST", "GET"])
def create_solution():
    if request.method == "POST":
        username = request.form['username']
        title = request.form['title']
        content = request.form['content']
        date_time = datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")

        try:
            db = sqlite3.connect('blog.db')
            sql = db.cursor()
            sql.execute("""CREATE TABLE IF NOT EXISTS articles (
                                                        id INTEGER primary key,
                                                        username TEXT,
                                                        title TEXT,
                                                        content TEXT,
                                                        date_time TEXT
                                                    )""")
            db.commit()
            sql.execute(
                """INSERT INTO articles (username, title, content, date_time) VALUES (?, ?, ?, ?)""",
                (username, title, content, date_time))
            db.commit()
        except Exception as ex:
            print(ex)
        return redirect('/')
    else:
        return render_template('create-solution.html')

@app.route('/admin-panel')
def admin_panel():
    db = sqlite3.connect('blog.db')
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS articles (
                                    id INTEGER primary key,
                                    title TEXT,
                                    text TEXT,
                                    date_time TEXT
                                )""")
    db.commit()
    sql.execute("""SELECT * FROM articles ORDER BY id DESC""")
    articles = sql.fetchall()
    db.commit()
    return render_template('admin-panel.html', articles=articles)

@app.route('/admin-panel/<int:id>/delete')
def article_delete(id):
    db = sqlite3.connect('blog.db')
    sql = db.cursor()
    sql.execute(f"""DELETE FROM articles WHERE id = {id}""")
    db.commit()
    return redirect('/admin-panel')

if __name__ == '__main__':
    app.run(debug=True)