from datetime import date
from core import getCosine
from core import getIndice
#realiza o calculo da soma
def calculaSoma(num1, num2):
    soma = num1 + num2
    return {"soma": soma}

#captura a data atual
def getDia():
    today = date.today()
    return {"data": today}

#TF-IDF
def tfIdf(title):
    tecnicas_recomendadas = []
    #pega a lista de tecnicas e a matrix do cosseno das tecnicas.
    indices = getIndice()
    cosine_sim = getCosine()
    # retorna o indice da tecnica cujo o nome é igual ao passado por parametro.
    idx = indices.[indices == title].index[0]

    # criando a Series com a similaridade
    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)

    # retornando as 5 tecnicas mais similares com a passada por parametro
    top_5_indexes = list(score_series.iloc[1:6].index)
    
    # put in the list
    for i in top_5_indexes:
        tecnicas_recomendadas.append(list(df.index)[i])

    return tecnicas_recomendadas
