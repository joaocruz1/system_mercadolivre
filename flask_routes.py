from flask import Flask, request, redirect, render_template, url_for, session, jsonify
from data.users_data import UserServices
from dataclasses import dataclass
from services import Services

@dataclass
class FlaskRoute:
    app: Flask
    user_login: UserServices
    user_info: str = None

    def __post_init__(self):
        self.register_routes()

    def register_routes(self):
        @self.app.route('/')
        def home():
            return render_template('login.html')

        @self.app.route('/userinfo')
        def userinfo():
            return render_template('userinfo.html', userinfo = self.user_info)

        @self.app.route('/dashboard')
        def dashboard():
            login_api = Services()
            session['userinfo_ml'] = login_api.infouser()
            self.user_info = session.get('userinfo_ml')
            
            return render_template('dashboard.html', userinfo = self.user_info)


        @self.app.route('/login', methods=['POST'])
        def login():
            try:
                email = request.form['email']
                password = request.form['password']
                shop = request.form['shop']

                # Armazena os dados em uma variável
                data = {"email": email, "password": password, "shop": shop}

                login_success = self.user_login.login(data)

                if login_success:
                    session['userinfo'] = data
                    return redirect(url_for('dashboard'))
                else:
                    return redirect(url_for('autherror'))

            except ValueError as e:
                # Tratamento para erros conhecidos
                print(f"Erro no login: {e}")
                return jsonify({"error": str(e)}), 400

            except Exception as e:
                # Tratamento para erros inesperados
                print(f"Erro inesperado no login: {e}")
                return jsonify({"error": "Erro no servidor"}), 500
            