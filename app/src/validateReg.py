
from app import app, request, make_response, sqlite3, redirect
import hashlib


@app.route("/api/private/validate/registration", methods=["POST"])
def validateReg():
    if request.method == "POST":
        try:
            uniqueTag = request.form["tag"]
            uname = request.form["uname"]
            pwd = request.form["pwd"]
            READY = False
            if int(uniqueTag) < 10_000 or int(uniqueTag) > 100_000:
                READY = False
            elif len(uname) < 5:
                READY = False
            elif len(pwd) < 6:
                READY = False
            else:
                READY = True


            if READY:
                encodePwd = hashlib.md5(pwd.encode("utf-8"))
                token = hashlib.md5((pwd+uname).encode("utf-8"))
                con = sqlite3.connect("app/db/users.db")
                curs = con.cursor()
                SQL = "INSERT INTO users ('tag', 'uname', 'pwd', 'token') VALUES (?, ? , ? , ?)"
                curs.execute(SQL, (uniqueTag, uname, encodePwd.hexdigest(), token.hexdigest()))
                con.commit()
                con.close()
                resp = make_response(redirect("/"))
                resp.set_cookie("token", token.hexdigest())
                # resp.set_cookie("user", uniqueTag)
                return resp, 200
            else:
                return "failed", 400

                           
        except Exception as e:
            return str(e), 400