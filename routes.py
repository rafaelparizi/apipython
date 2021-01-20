import os
from flask import Flask, request


app = Flask("Helius")

@app.route("/olamundo",methods=["GET"])
def olaMundo():
    return geraResponse(200,"Ola mundo")


#funcao para gerenciar responses
def geraResponse(status,mensagem, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem

    if(nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo

    return response

if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0',port=port)