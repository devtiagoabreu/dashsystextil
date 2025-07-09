import os
import requests
from dotenv import load_dotenv
import structlog
from typing import Optional

logger = structlog.get_logger(__name__)
load_dotenv()

class APIError(Exception):
    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code
        super().__init__(message)

def get_required_env(key: str) -> str:
    """Obtém uma variável de ambiente obrigatória ou levanta erro"""
    value = os.getenv(key)
    if value is None:
        raise APIError(f"Variável de ambiente {key} não configurada", 500)
    return value

def get_api_data(endpoint: str) -> dict:
    try:
        # Obter variáveis de ambiente com verificação
        token_url = get_required_env("TOKEN_URL")
        client_id = get_required_env("CLIENT_ID")
        client_secret = get_required_env("CLIENT_SECRET")
        api_base_url = get_required_env("API_BASE_URL")

        # Obter token
        token_response = requests.post(
            token_url,  # Agora garantido que é string
            data={"grant_type": "client_credentials"},
            auth=(client_id, client_secret)
        )
        token_response.raise_for_status()
        token = token_response.json().get("access_token")
        if not token:
            raise APIError("Token de acesso não recebido", 401)

        # Fazer requisição principal
        response = requests.get(
            f"{api_base_url}{endpoint}",
            headers={"Authorization": f"Bearer {token}"}
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        logger.error("Erro na API", error=str(e))
        raise APIError(f"Erro ao acessar a API: {str(e)}", 500)
    except APIError as e:
        raise
    except Exception as e:
        logger.error("Erro inesperado", error=str(e))
        raise APIError("Erro interno no processamento", 500)