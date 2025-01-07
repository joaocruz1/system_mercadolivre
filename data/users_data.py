from dataclasses import dataclass
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import request, jsonify
from data.api_data import APIData


@dataclass
class UserLogin:

    spreadsheet_id2: str = None
    credentials_file: str = "credenciais.json"
    shop: str = None
    scope: list = None

    def __post_init__(self):
        # Definir escopo de permissões
        if self.scope is None:
            self.scope = [
                "https://spreadsheets.google.com/feeds",
                "https://www.googleapis.com/auth/drive"
            ]

        # Carregar credenciais do arquivo JSON
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.credentials_file, self.scope)

        # Autenticar e acessar o Google Sheets
        self.client = gspread.authorize(credentials)

        # Abrir a planilha pelo ID
        self.sheet = self.client.open_by_key(self.spreadsheet_id2).sheet1

    def get_users(self):
        # Retorna todos os registros da planilha como uma lista de dicionários
        return self.sheet.get_all_records()

    def login(self, data):
        # Obter dados do dicionário
        user_email = data.get("email")
        user_password = data.get("password")
        user_shop = data.get("shop")

        if not user_email or not user_password or not user_shop:
            return jsonify({"error": "Todos os campos são obrigatórios."}), 400

        users = self.get_users()

        for user in users:
            if user_email == user['email'] and user_password == user['password']:
                if user_shop == user['shop']:
                    self.shop = user_shop
                    login_api = APIData()
                    login_api.datarows()
                    return True
                else:
                    raise ValueError("Essa loja não consta em nosso sistema.")
    
            raise ValueError("E-mail ou senha incorretos.")


    def add_user(self):
        # Obter dados da requisição HTTP
        new_nickname = request.json.get("nickname")
        new_email = request.json.get("email")
        new_password = request.json.get("password")
        new_adm = request.json.get("adm")

        # Verificar se todos os campos foram preenchidos
        if not new_nickname or not new_email or not new_password or new_adm is None:
            return jsonify({"error": "Todos os campos devem ser preenchidos."}), 400

        # Adicionar os dados como uma nova linha na planilha
        try:
            self.sheet.append_row([new_nickname, new_email, new_password, self.shop, str(new_adm).lower()])
            return jsonify({"message": "Novo usuário adicionado com sucesso!"}), 201
        except Exception as e:
            return jsonify({"error": f"Erro ao adicionar usuário: {str(e)}"}), 500

    def remove_user(self):
        return jsonify({"message": "Função de remoção ainda não implementada."}), 501
