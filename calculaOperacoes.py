from datetime import date

#realiza o calculo da soma
def calculaSoma(num1, num2):
    soma = num1 + num2
    return {"soma": soma}

#captura a data atual
def getDia():
    today = date.today
    return {"data": today}

