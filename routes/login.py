from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from flask_login import login_user
from dataclasses import dataclass
from data.users_data import UserServices
from services import Services
from database import User

@dataclass
class LoginRoute:
    blueprint_name: str = "login"
    import_name: str = __name__
    user_service: UserServices = None
    services_api: Services = None
    database_serviceUser: User = None
    
    def __post_init__(self):
        self.blueprint = Blueprint(self.blueprint_name, self.import_name)
        self.register_routes()

    def register_routes(self):
        @self.blueprint.route('/')
        def home():
            return render_template('login.html')

        @self.blueprint.route('/', methods=['POST'])
        def login():
            try:
                # Obter dados do formulário
                email = request.form['email']
                password = request.form['password']
                shop = request.form['shop']

                # Dados do login
                data = {"email": email, "password": password, "shop": shop}

                for user in self.database_serviceUser.select():

                    if data['shop'] == user.shop.name:
                        if data['email'] == user.email and data['password'] == user.password:
                            user1 = {user.name,user.email,user.adm,user.shop.name}
                            login_user(user1)
                            session['userinfo_ml'] = self.services_api.infouser()
                            session['userinfo'] = {'user_name': user.name,
                                                   'user_email': user.email,
                                                   'user_adm': user.adm,
                                                   'user_shop':user.shop.name}

                            return redirect(url_for('dashboard.dashboard')) 
                        else:
                            return jsonify({"email ou senha incorretos"})
                    else:
                        return jsonify("Loja não consta em nosso sistema")

            except ValueError as e:
                print(f"Erro de validação: {e}")  # Depuração
                return jsonify({"error": str(e)}), 400

            except Exception as e:
                print(f"Erro inesperado: {e}")  # Depuração
                return jsonify({"error": f"Erro no servidor: {str(e)}"}), 500



