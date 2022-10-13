from flask import Flask
app=Flask(__name__)

@app.route("/")
def home_view():
    return "<h1>i am th boss who are the main boss that u can made</h1>"
