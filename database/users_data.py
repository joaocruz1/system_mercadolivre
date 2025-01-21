from dataclasses import dataclass
from flask import request, jsonify
from datetime import datetime
from database import User, Shop

@dataclass
class UserServices:

    def login(self, data):
        # Obter dados do dicionário
        user_email = data.get("email")
        user_password = data.get("password")
        user_shop = data.get("shop")

        print("AAAAAAAAAAAAAAAAAAAAAAAAAA")

        # Validação inicial
        if not user_email :
            return jsonify({"error": "Todos os campos são obrigatórios."}), 400

        try:
           users = User.select()

           for user in users:

            if user_email == user.email:
                print("Entrou")
           
            return True

        except User.DoesNotExist:
            raise ValueError("E-mail não encontrado.")
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": f"Erro no servidor: {str(e)}"}), 500

    def remove_user(self):
        return jsonify({"message": "Função de remoção ainda não implementada."}), 501

    def consult_users(self):

        users = self.get_users()
        usersinfo = []

        for _ , user in enumerate(users, start=2):

            usersinfo.append({
            'id': _,
            'name': user['user'],
            'email': user['email'],
            'adm': user['adm']
            })
            
        return usersinfo


    def consult_user(self,id):
        
        users = self.get_users()

        for id_user, user in enumerate(users, start=2):
            if(id == id_user):
                return {
                    'id' : id_user,
                    'name': user['user'],
                    'email': user['email'],
                    'adm': user['adm']
                }

    def edit_user(self,id, user_updates):

        users = self.get_users()

        for id_user, user in enumerate(users, start=2):
            
            if(id == id_user):
                self.sheet.update_cell(id_user, 2, user_updates['email'])
                self.sheet.update_cell(id_user, 1, user_updates['name'])
    
    def delete_user(self,id):
        users = self.get_users()

        for id_user,user in enumerate(users, start=2):

            if(id == id_user):
                self.sheet.delete_rows(id)



    def true_or_false(self,response):
        response.lower
        if response == "sim":
            return True
        else:
            return False
