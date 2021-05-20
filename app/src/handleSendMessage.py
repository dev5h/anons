from sqlite3.dbapi2 import connect
from app import app, request, make_response, hashlib, sqlite3
def findUserByToken(token):
    con = sqlite3.connect("../db/users.db")
    curs = con.cursor()
    curs.execute(f"SELECT * FROM users WHERE token='{token}'")
    row = curs.fetchone()
    con.close()
    return row[1], row[2]

def findTokenByUsername(uname):
    con = sqlite3.connect("../db/users.db")
    curs = con.cursor()
    curs.execute(f"SELECT * FROM users WHERE token='{token}'")
    row = curs.fetchone()
    con.close()
    return row[1], row[2]

def userExist(token):
    con = sqlite3.connect("../db/users.db")
    curs = con.cursor()
    curs.execute(f"SELECT * FROM users WHERE token='{token}'")
    row = curs.fetchone()
    con.close()
    if len(row) > 0:
        return True
    else:
        return False




@app.route("/api/private/text/send/", methods=["POST"])
def handleSendMessage():
    try:
        sender = request.form["sender"]
    except Exception as e:
        pass





