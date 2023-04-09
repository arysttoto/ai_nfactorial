import sqlite3


def func_add_essay(username, topic, essay, summary, disease_type, image_url):
    db = sqlite3.connect('blog.db')
    sql = db.cursor()
    try:
        sql.execute("""INSERT INTO disease_essays (username, topic, essay, summary, disease_type, image_url) VALUES (?, ?, ?, ?, ?, ?)""",
                    (username, topic, essay, summary,  disease_type, image_url))
        db.commit()
        sql.close()
        db.close()
    except Exception as ex:
        print(ex)

def func_fetch_my_essays(username):
    db = sqlite3.connect('blog.db')
    sql = db.cursor()
    sql.execute(f"""SELECT * FROM disease_essays WHERE username = '{username}' ORDER BY disease_type""")
    data = sql.fetchall()
    sql.close()
    db.commit()
    db.close()
    return data

# def func_get_essays(session_id):
#     db = sqlite3.connect('blog.db')
#     sql = db.cursor()
#     sql.execute(f"""SELECT topic, essay FROM diseases WHERE session_id == {session_id}""")
#     data = sql.fetchall()
#     sql.close()
#     db.close()
#     return data
# import sqlite3
# db = sqlite3.connect('blog.db')
# sql = db.cursor()
# sql.execute("""CREATE TABLE disease_types(
#             disease_type TEXT,
#             essay TEXT)""")
# db.commit()
