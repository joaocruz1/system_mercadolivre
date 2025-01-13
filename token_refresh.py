import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dataclasses import dataclass
import json  # Necessário para carregar a string JSON aninhada

@dataclass
class TokenRefresh:

    spreadsheet_id: str
    credentials_file: str = "credenciais.json"
    scope: list = None
    token: dict = None

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

        # Executar a lógica
        self.execute()

    def execute(self):
        # Ler dados
        self.rows = self.sheet.get_all_records()

        # Atualizar dados
        self.sheet.update_cell(2, 2, "Valor Atualizado!")

        # Extrair tokens
        self.token = self.extract_tokens()

    def extract_tokens(self):
        if not self.rows:
            print("Nenhum dado disponível para extrair tokens.")
            return None

        # Supõe que os dados estão na primeira linha
        first_row = self.rows[0]

        # Extrair informações
        conta = first_row.get("conta")
        refresh_token = first_row.get("refresh_novo")

        # Parsear a string JSON contida na chave 'bruto'
        bruto = first_row.get("bruto")

        try:
            bruto_data = json.loads(bruto)
            access_token = bruto_data.get("access_token")
        except json.JSONDecodeError:
            print("Erro ao decodificar o JSON em 'bruto'.")
            access_token = None
        
        return {
            "conta": conta,
            "refresh_token": refresh_token,
            "access_token": access_token
        }


