from flask import Flask, g
from flask_session import Session
from routes.login import LoginRoute
from routes.dashboard import DashboardRoute
from routes.users import UsersRoute
from data.users_data import UserServices
from services import Services
from database import db, User, Shop

# Inicializa o aplicativo Flask
app = Flask(__name__)
app.secret_key = 'system_ml$91873919'
app.config['SESSION_TYPE'] = 'filesystem'  # Configuração de sessão
Session(app)

# Inicializa serviços
user_services = UserServices()
services_api = Services()

db.connect()

# Listar todas as lojas
print("Lojas:")
for shop in Shop.select():
    print(f"ID: {shop.id}, Nome: {shop.name}")

# Listar todos os usuários
print("\nUsuários:")
for user in User.select():
    print(f"ID: {user.id}, Nome: {user.name}, Email: {user.email}, Senha: {user.password}, Loja: {user.shop.name}")

db.close()

# Inicializa o banco de dados
@app.before_request
def before_request():
    """Conecta ao banco antes de cada requisição."""
    if db.is_closed():
        db.connect()

@app.teardown_request
def teardown_request(exception):
    """Desconecta o banco após cada requisição."""
    if not db.is_closed():
        db.close()

# Registra as rotas usando blueprints
app.register_blueprint(LoginRoute(user_service=user_services).blueprint, url_prefix="/login")
app.register_blueprint(DashboardRoute(services_api=services_api).blueprint, url_prefix="/dashboard")
app.register_blueprint(UsersRoute(users_service=user_services).blueprint, url_prefix="/users")

if __name__ == '__main__':
    app.run(debug=True)
