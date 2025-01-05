import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dataclasses import dataclass

@dataclass
class TokenRefresh:
    
    spreadsheet_id: str
    credentials_file: str = "credenciais.json"
    scope: list = None

    def __post_init__(self):
        # Definir escopo de permissões
        if self.scope is None:
            self.scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

        # Carregar credenciais
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.credentials_file, self.scope)

        # Autenticar e acessar o Google Sheets
        self.client = gspread.authorize(credentials)

        # Abrir a planilha pelo ID
        self.sheet = self.client.open_by_key(self.spreadsheet_id).sheet1
        
        self.execute()

    def execute(self):
        # Ler dados
        rows = self.sheet.get_all_records()
        print("Dados:", rows)

        # Atualizar dados
        self.sheet.update_cell(2, 2, "Novo valor!")
        print("Atualizado com sucesso!")