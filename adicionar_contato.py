import requests

# URL base da API (substitua pela URL correta)
base_url = 'https://agnuspromotora.digisac.co/api/v1'

# Endpoint para adicionar contatos
endpoint = '/contacts'

# Token de autenticação (substitua pelo token correto)
auth_token = 'Bearer e67524a09f3fc9917902eeaf331562a9ba46a8d5'

# Token de autenticação
token = 'seu_token_aqui'

# Cabeçalhos da requisição, incluindo o token de autenticação
headers = {
    'Authorization': auth_token,
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'  # Incluindo o token no cabeçalho
}

# Parâmetros do contato a serem enviados no corpo da requisição
contato = {

    # ... (seus parâmetros de contato aqui)
    "unsubscribed": False,
    "note": "novo contato",
    "serviceId": "12345678-abcdefghi-1234-abcdefghijkl",
    "personId": "12345678-abcdefghi-1234-abcdefghijkl",
    "defaultDepartmentId": "12345678-abcdefghi-1234-abcdefghijkl",
    "defaultUserId": "12345678-abcdefghi-1234-abcdefghijkl",
    "name": "Natã",
    "internalName": "GabrielM",
    "alternativeName": "GabrielM",
    "number": "5547991027132"

}

# URL completa para adicionar o novo contato
url = base_url + endpoint

# Enviar a requisição POST para adicionar o novo contato
response = requests.post(url, json=contato, headers=headers)


# Verificar a resposta da requisição e lidar com os resultados
# ...
# Verificar a resposta da requisição

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
