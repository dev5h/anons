from app import app, render_template

@app.route("/")
def index():
    return "Flask app is now running "