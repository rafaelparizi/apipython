import os
from flask import Flask, request


app = Flask("Helius")

@app.route("/olamundo",methods=["GET"])
def olaMundo():
    return {"ola" : "mundo"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0',port=port)