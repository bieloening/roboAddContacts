import requests

# URL da rota para adicionar contatos (substitua pela URL correta)
url = 'https://docs.ikatec.cloud/api/contacts'

# Cabeçalhos da requisição
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

# Parâmetros do contato a serem enviados no corpo da requisição
contato = {
    "unsubscribed": False,
    "note": "novo contato",
    "serviceId": "12345678-abcdefghi-1234-abcdefghijkl",
    "personId": "12345678-abcdefghi-1234-abcdefghijkl",
    "defaultDepartmentId": "12345678-abcdefghi-1234-abcdefghijkl",
    "defaultUserId": "12345678-abcdefghi-1234-abcdefghijkl",
    "name": "Natã",
    "internalName": "Natã",
    "alternativeName": "Natã",
    "number": "5514999999999"
}

# Enviar a requisição POST para adicionar o novo contato
response = requests.post(url, json=contato, headers=headers)

# Verificar a resposta da requisição
if response.status_code == 200:
    print("Contato adicionado com sucesso!")
    print("Resposta:")
    print(response.json())
else:
    print("Erro ao adicionar contato. Código de status:", response.status_code)
    print("Resposta:", response.text)

if response.status_code == 200:
    try:
        print("Contato adicionado com sucesso!")
        print("Resposta:")
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Resposta inválida. Não foi possível decodificar como JSON.")
else:
    print("Erro ao adicionar contato. Código de status:", response.status_code)
    print("Resposta:", response.text)
