import os
import requests
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
TOKEN_URL = os.getenv("TOKEN_URL")
API_BASE_URL = os.getenv("API_BASE_URL")

# Gera token OAuth2 com client_credentials
def get_token():
    response = requests.post(
        TOKEN_URL,
        data={"grant_type": "client_credentials"},
        auth=(CLIENT_ID, CLIENT_SECRET)
    )
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print("Erro ao obter token:", response.text)
        return None

# Chamada GET genérica por endpoint
def get_api_data(endpoint: str):
    token = get_token()
    if not token:
        return {}
    
    url = f"{API_BASE_URL}{endpoint}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao chamar endpoint '{endpoint}':", response.text)
        return {}
