# Dashboard Financeiro Systêxtil

![Badge Versão](https://img.shields.io/badge/versão-1.0.0-blue) 
![Python](https://img.shields.io/badge/python-3.7%2B-green)
![Licença](https://img.shields.io/badge/licença-MIT-orange)

**Desenvolvedor:** Tiago de Abreu  
**Data de Lançamento:** 09/07/2025

## 📌 Visão Geral

Dashboard financeiro integrado com a API da Systêxtil para visualização em tempo real de:
- Faturamento mensal
- Contas a receber
- Contas a pagar

## ✨ Funcionalidades Principais

✅ Visualização consolidada de dados financeiros  
✅ Atualização manual ou automática (15 minutos)  
✅ Tratamento robusto de erros e falhas  
✅ Interface intuitiva e responsiva  
✅ Segurança com autenticação OAuth2  

## 🛠️ Tecnologias Utilizadas

- **Frontend:** Flet (Python)
- **Backend:** Python 3.7+
- **Autenticação:** OAuth2 Client Credentials
- **Logging:** Structlog
- **Configuração:** Python-dotenv

## 📦 Estrutura do Projeto

```
dashsystextil/
├── src/
│   ├── main.py            # Ponto de entrada
│   ├── ui.py              # Componentes UI
│   ├── api.py             # Integração com API
├── assets/                # Recursos visuais
├── .env                   # Configurações
├── requirements.txt       # Dependências
└── README.md              # Documentação
```

## ⚙️ Configuração

1. Clone o repositório:
```bash
git clone https://github.com/devtiagoabreu/dashsystextil.git
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure o arquivo `.env`:
```ini
CLIENT_ID=seu_client_id
CLIENT_SECRET=seu_client_secret
TOKEN_URL=http://api.systextil.com/oauth/token
API_BASE_URL=http://api.systextil.com/v1/
DEBUG=True
```

## 🚀 Execução

```bash
python src/main.py
```

O aplicativo será aberto automaticamente no seu navegador padrão.

## 📊 Telas

| Faturamento | Contas a Receber |
|-------------|------------------|
| ![Faturamento](assets/screenshots/faturamento.png) | ![A Receber](assets/screenshots/receber.png) |

## ⚠️ Tratamento de Erros

O sistema identifica e trata automaticamente:
- Falhas de conexão
- Erros de autenticação
- Dados inválidos
- Problemas na API

## 📝 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🤝 Contribuição

Contribuições são bem-vindas! Siga os passos:
1. Faça um fork do projeto
2. Crie sua branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## ✉️ Contato

**Tiago de Abreu**  
📧 tiago@email.com  
🔗 [LinkedIn](https://linkedin.com/in/devtiagoabreu)  
🐙 [GitHub](https://github.com/devtiagoabreu)

---

**Atualizado em:** Julho 2025  
**Versão:** 1.0.0