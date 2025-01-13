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
        @self.blueprint.route('/login')
        def home():
            return render_template('login.html')

        @self.blueprint.route('/login', methods=['POST'])
        def login():
            try:
                email = request.form['email']
                password = request.form['password']
                shop = request.form['shop']
                data = {"email": email, "password": password, "shop": shop}
                login_success, user_info = self.user_service.login(data)

                if login_success:
                    session['userinfo'] = user_info
                    return redirect(url_for('dashboard.dashboard'))
                else:
                    return redirect(url_for('autherror'))
            except ValueError as e:
                return jsonify({"error": str(e)}), 400
            except Exception as e:
                 return jsonify({"error": f"Erro no servidor: {str(e)}"}), 500

