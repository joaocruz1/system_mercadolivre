from flask import Flask, request, redirect, render_template, url_for, session, jsonify
from data.users_data import UserLogin
from dataclasses import dataclass

@dataclass
class FlaskRoute:
    app: Flask
    user_login: UserLogin

    def __post_init__(self):
        self.register_routes()

    def register_routes(self):
        @self.app.route('/')
        def home():
            return render_template('login.html')

        @self.app.route('/dashboard')
        def dashboard():
            return self.login_validation('dashboard.html')


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
                    session['user'] = data
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
            

    def login_validation(self,page):

        if 'user' in session:
            return render_template(page)
        else:
            return render_template('login.html')