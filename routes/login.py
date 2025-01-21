from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from dataclasses import dataclass
from data.users_data import UserServices

@dataclass
class LoginRoute:
    blueprint_name: str = "login"
    import_name: str = __name__
    user_service: UserServices = None

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
                email = request.form.get('email')
                password = request.form.get('password')
                shop = request.form.get('shop')

                print(f"Tentativa de login: {email}, {shop}")  # Depuração

                # Dados do login
                data = {"email": email, "password": password, "shop": shop}

                # Validar login
                login_success, user_info = self.user_service.login(data)

                if login_success:
                    session['userinfo'] = user_info
                    print(f"Login bem-sucedido: {user_info}")  # Depuração
                    return redirect(url_for('dashboard.dashboard'))
                else:
                    return jsonify({"error": "Login falhou."}), 400

            except ValueError as e:
                print(f"Erro de validação: {e}")  # Depuração
                return jsonify({"error": str(e)}), 400

            except Exception as e:
                print(f"Erro inesperado: {e}")  # Depuração
                return jsonify({"error": f"Erro no servidor: {str(e)}"}), 500


