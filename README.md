# dashsystextil
dashboard em flet consumindo api systêxtil


era legal ele ter um arquivo api.py import os
import requests
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
TOKEN_URL = os.getenv("TOKEN_URL")
API_URL = os.getenv("API_URL")

def get_faturamento():
    """Obtem token OAuth2 Client Credentials e chama API de faturamento"""
    # 1️⃣ Token
    token_response = requests.post(
        TOKEN_URL,
        data={