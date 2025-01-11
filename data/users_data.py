from dataclasses import dataclass
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import request, jsonify
from datetime import datetime

@dataclass
class UserServices:

    spreadsheet_id2: str = None
    credentials_file: str = "credenciais.json"
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
        user_adm = data.get('adm')

        if not user_email or not user_password or not user_shop:

            return jsonify({"error": "Todos os campos são obrigatórios."}), 400

        users = self.get_users()

        # Procura pelo usuário na lista de usuários
        for idx, user in enumerate(users, start=2):  # A primeira linha é o cabeçalho, então começa no índice 2

            if user_email == user['email'] and user_password == user['password']:

                if user_shop == user['shop']:

                    login_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    self.sheet.update_cell(idx, 6, login_time)  # Coluna 'F' é a 6ª coluna
                    infouser_login = user

                    return True, infouser_login
                else:
                    raise ValueError("Essa loja não consta em nosso sistema.")
    
        raise ValueError("E-mail ou senha incorretos.")



    def remove_user(self):
        return jsonify({"message": "Função de remoção ainda não implementada."}), 501

    def consult_users(self):

        users = self.get_users()
        usersinfo = []

        for _ , user in enumerate(users, start=2):

            usersinfo.append({
            'name': user['user'],
            'email': user['email'],
            'adm': user['adm']
            })
            
        return usersinfo





    def true_or_false(self,response):
        response.lower
        if response == "sim":
            return True
        else:
            return False
