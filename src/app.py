from flask import *
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/account", methods=["POST", "GET"])
def account():
    usr = "<User Not Defined>"
    if (request.method == "POST"):
        usr = request.form["name"]
        if not usr:
            usr = "<User Not Defined>"
    return render_template("account.html",username=usr)

if __name__ == "__main__":
    app.run()