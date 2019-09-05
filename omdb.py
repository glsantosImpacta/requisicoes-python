from requests import api

key = "7b66358d"
url = f"http://www.omdbapi.com/?s=star wars&apikey={key}"

retorno = api.get(url).json()

filmes = retorno["Search"]
nome_filmes = []

for filme in filmes:
    print(filme["Title"])

#print(retorno["Search"][1]["Title"])