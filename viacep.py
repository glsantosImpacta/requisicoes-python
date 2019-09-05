from requests import api

def busca_cep(cep):

    url = f"http://viacep.com.br/ws/{cep}/json"
    endereco = api.get(url).json()

    return endereco

cep = input("Insira um CEP: ")
endereco = busca_cep(cep)

print("---Consulta de CEP---")
print(f"CEP informado: {cep}")
print(f"Estado: {endereco['uf']}")
print(f"Cidade: {endereco['localidade']}")
print(f"Logradouro: {endereco['logradouro']}")