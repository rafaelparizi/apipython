from flask import Flask, request


app = Flask("Youtube")

@app.route("/olamundo",methods=["GET"])
def olaMundo():
    return {"ola" : "mundo"}


app.run()