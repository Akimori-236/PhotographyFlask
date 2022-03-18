from select import select
from flask import Flask, request, jsonify, g, render_template
from flask_cors import CORS
from model.User import User
from Validation.Validator import *

app = Flask(__name__)
CORS(app)

@app.route('/')
@app.route("/index")
def sanityCheck():
    return render_template("index.html")

# ERRORS
@app.errorhandler(500)
def error500(e):
    print(e)
    return render_template("500.html"), 500

@app.errorhandler(404)
def error404(e):
    print(e)
    return render_template("404.html"), 404


# GET all users
@app.route('/users')
@validateJWTToken
@requireAdmin
def getAllUsers():
    print("g context role:" + g.role)
    print("g context userid:" + str(g.userid))
    try:
        jsonUsers = User.getAllUsers()
        output = {"Users": jsonUsers}
        return render_template("users.html", users = output["Users"]), 200     # OK
    except Exception as err:
        print(err)
        return {}, 500      # internal server error

# GET Log in page
@app.route('/login')
def Login():
    try:
        return render_template("login.html"), 200     # OK
    except Exception as err:
        print(err)
        return {}, 500      # internal server error

# get scenery page
@app.route('/photos/scenery')
def GetScenery():
    try:
        return render_template("scenery.html"), 200     # OK
    except Exception as err:
        print(err)
        return {}, 500      # internal server error

if __name__ == "__main__":
    app.run(debug=True)