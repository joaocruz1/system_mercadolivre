from dataclasses import dataclass
from data.api_data import APIData

# Dados dos usuários
users = {
    1: {
        'email': 'joaovcruz50@gmail.com',
        'senha': 'jvhc123',
        'loja': True,
        'adm': True
    },
    2: {
        'email': 'jvhcsuper123@gmail.com',
        'senha': '123456',
        'loja': True,
        'adm': False
    }
}

@dataclass
class UserLogin:
    user_email: str = None
    user_password: str = None

    def login(self):

        self.user_email = input("\nDigite seu e-mail: ").strip()
        self.user_password = input("\nDigite sua senha: ").strip()

        for user_id, user_data in users.items():

            if self.user_email == user_data['email'] and self.user_password == user_data['senha']:
                
                print("\nLogin realizado com sucesso!")
                print(f"Bem-vindo, usuário {user_id}!")

                self.api_data = APIData()
                self.api_data.datarows()

                return True
        
        print("\nE-mail ou senha incorretos. Tente novamente.")
        return False


