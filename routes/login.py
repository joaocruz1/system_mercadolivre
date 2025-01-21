from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from dataclasses import dataclass
from data.users_data import UserServices
from database import User

@dataclass
class LoginRoute:
    blueprint_name: str = "login"
    import_name: str = __name__
    user_service: UserServices = None
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
                shop = request.form['password']

                print(f"Tentativa de login: {email}, {shop}")  # Depuração

                # Dados do login
                data = {"email": email, "password": password, "shop": shop}

                for user in self.database_serviceUser.select():

                    if data['email'] == user.email:
                        return redirect(url_for('dashboard.dashboard'))

            except ValueError as e:
                print(f"Erro de validação: {e}")  # Depuração
                return jsonify({"error": str(e)}), 400

            except Exception as e:
                print(f"Erro inesperado: {e}")  # Depuração
                return jsonify({"error": f"Erro no servidor: {str(e)}"}), 500



