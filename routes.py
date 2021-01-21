import os
from flask import Flask, request
from calculaOperacoes import calculaSoma
from calculaOperacoes import getDia

app = Flask("Helius")

@app.route("/olamundo",methods=["GET"])
def olaMundo():
    return geraResponse(200, "Ola mundo")

@app.route("/getdata",methods=["GET"])
def pegaData():
    dia = getDia()
    return geraResponse(200,"dia ok","dia",dia)

#calculo de soma
@app.route("/calcula/soma",methods=["POST"])
def soma():
    body = request.get_json()
    print(body)

    #analisa se os campos foram preenchidos
    if("num1" not in body):
        return geraResponse(400,"O parâmetro num1 é obrigatório")
    if ("num2" not in body):
        return geraResponse(400, "O parâmetro num1 é obrigatório")

    #chama função soma
    soma = calculaSoma(body["num1"],body["num2"])
    return geraResponse(200,"Soma realizada com sucesso","soma",soma)


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