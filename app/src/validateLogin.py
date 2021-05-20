
from app import app, request, make_response, sqlite3, redirect
import hashlib


@app.route("/api/private/validate/login", methods=["POST"])
def validateLogin():
    if request.method == "POST":
        try:
            uname = request.form["uname"]
            pwd = request.form["pwd"]    
            token = hashlib.md5((pwd+uname).encode("utf-8"))
            con = sqlite3.connect("app/db/users.db")
            curs = con.cursor()
            curs.execute(f"SELECT * FROM users WHERE token = '{token.hexdigest()}'")
            row = curs.fetchall()
            con.close()
            if len(row) == 1:
                resp = make_response(redirect("/"))
                resp.set_cookie("token", token.hexdigest())
                
                return resp , 200
            else:
                return make_response(redirect("/login?err=true")), 400
            # return str(row)
         
        except Exception as e:
            return str(e), 400