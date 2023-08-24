import requests

# URL da rota para adicionar contatos (substitua pela URL correta)
url = 'https://docs.ikatec.cloud/api/contacts'

# Token de autenticação
token = 'seu_token_aqui'

# Cabeçalhos da requisição, incluindo o token de autenticação
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'  # Incluindo o token no cabeçalho
}

# Parâmetros do contato a serem enviados no corpo da requisição
contato = {
    # ... (seus parâmetros de contato aqui)
}

# Enviar a requisição POST para adicionar o novo contato
response = requests.post(url, json=contato, headers=headers)

# Verificar a resposta da requisição e lidar com os resultados
# ...
