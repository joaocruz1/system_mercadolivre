from flask import Flask, request, redirect, render_template, url_for, session, jsonify
from data.users_data import UserServices
from dataclasses import dataclass
from services import Services

@dataclass
class FlaskRoute:
    app: Flask
    user_login: UserServices
    services_api: Services
    user_infoml: str = None
    user_info: str = None
    date_login: str = None

    def __post_init__(self):
        # Registra as rotas
        self.register_routes()

    def register_routes(self):
        # Função que será chamada antes de cada requisição (before request)
        @self.app.before_request
        def check_login():
            # Verifica se a chave 'userinfo' existe na sessão
            if 'userinfo' not in session:
                # Se não estiver logado e a requisição não for para login ou erro, redireciona
                if request.endpoint not in ['login', 'autherror']:
                    return redirect(url_for('login'))
                
        @self.app.route('/')
        def index():
            return redirect(url_for('login'))

        # Rota inicial de login
        @self.app.route('/login')
        def home():
            return render_template('login.html')

        # Rota de login (POST)
        @self.app.route('/login', methods=['POST'])
        def login():
            try:
                # Pega os dados do formulário de login
                email = request.form['email']
                password = request.form['password']
                shop = request.form['shop']

                # Armazena os dados em uma variável
                data = {"email": email, "password": password, "shop": shop}

                # Verifica se o login foi bem-sucedido
                login_success, self.date_login = self.user_login.login(data)

                if login_success:
                    session['userinfo'] = data  # Armazena os dados do usuário na sessão
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

        # Dashboard do usuário
        @self.app.route('/dashboard')
        def dashboard():

            # Obtém as informações do usuário (simulando uma consulta externa)
            self.user_info = session.get('userinfo_ml')
            session['userinfo_ml'] = self.services_api.infouser()
            
            quantity_products = self.services_api.search_products()
            quantity_sales = self.services_api.import_sales()

            return render_template('dashboard.html', userinfo=self.user_info, quantity_products=quantity_products, quantity_sales=quantity_sales)
        
        


        # Rota de informações do usuário
        @self.app.route('/userinfo')
        def userinfo():

            # Acessa as informações do usuário já logado (presumido)
            session['userinfoml']= self.services_api.infouser()
            self.user_infoml = session.get('userinfoml')
            self.user_info = session.get('userinfo')

            return render_template('userinfo.html', userinfo=self.user_infoml, datelogin=self.date_login, usershop=self.user_info)

