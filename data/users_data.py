from dataclasses import dataclass
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from data.api_data import APIData

@dataclass
class UserLogin:
   
    spreadsheet_id2: str = None
    credentials_file: str = "credenciais.json"
    shop: str = None
    users: list = None
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

        data = self.sheet.get_all_records()  # Retorna todos os registros da planilha como uma lista de dicionários

        return data
    
    def login(self):
        
        self.user_email = input("Digite seu e-mail: ").strip()
        self.user_password = input("Digite sua senha: ").strip()
        self.user_shop = input("Digite o nome da loja: ").strip()

        users = self.get_users()  # Pega os dados da planilha

        # Verificar se o e-mail e a senha correspondem a algum usuário
        for user in users:
            if self.user_email == user['email'] and self.user_password == user['password']:
                if self.user_shop == user['shop']:
                    print("\nLogin realizado com sucesso!")
                    self.shop = self.user_shop
                    self.loginapi = APIData()
                    self.loginapi.datarows()
                    
                    return True
                else:
                    print("Essa Loja não consta em nosso sistema")
            else:
                print("\nE-mail ou senha incorretos. Tente novamente.")
                return False
            

    def adduser(self):
       
        print("\n--- Adicionar Novo Usuário ---")

        # Solicitar os dados do novo usuário
        self.new_nicknameuser = input("Digite o nome desse usuário").strip()
        self.new_email = input("Digite o e-mail do novo usuário: ").strip()
        self.new_password = input("Digite a senha do novo usuário: ").strip()
        self.new_adm = input("true ou false ").strip()



        # Verificar se todos os campos foram preenchidos
        if not self.new_nicknameuser or not self.new_email or not self.new_password or not self.new_adm:
            print("Erro: Todos os campos devem ser preenchidos.")
            return

        # Adicionar os dados como uma nova linha na planilha
        try:
            self.sheet.append_row([self.new_nicknameuser, self.new_email, self.new_password, self.shop, self.new_adm])
            print("Novo usuário adicionado com sucesso!")

        except Exception as e:
            print(f"Erro ao adicionar usuário: {e}")

        def removeuser(self):
            pass

       


