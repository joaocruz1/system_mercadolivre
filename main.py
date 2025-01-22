from flask import Flask, url_for, session, g
from flask_login import LoginManager
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

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login.login'

@login_manager.user_loader
def load_user(user_id):
    try:
        return User.get(User.id == int(user_id))
    except User.DoesNotExist:
        return None

# Inicializa serviços
user_services = UserServices()
services_api = Services()
database_serviceUser= User()

# Inicializa o banco de dados
@app.before_request
def before_request():
    if db.is_closed():
        db.connect()

@app.teardown_request
def teardown_request(exception):
    """Desconecta o banco após cada requisição."""
    if not db.is_closed():
        db.close()

# Registra as rotas usando blueprints
app.register_blueprint(LoginRoute(user_service=user_services, database_serviceUser=database_serviceUser, services_api=services_api).blueprint, url_prefix="/login")
app.register_blueprint(DashboardRoute(services_api=services_api).blueprint, url_prefix="/dashboard")
app.register_blueprint(UsersRoute(users_service=user_services).blueprint, url_prefix="/users")

if __name__ == '__main__':
    app.run(debug=True)
