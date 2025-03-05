from flask import Flask, g, session
from flask_login import LoginManager
from flask_session import Session
from routes.login import LoginRoute
from routes.dashboard import DashboardRoute
from routes.users import UsersRoute
from routes.products import ProductsRoute
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
services_api = Services()

# Inicializa o banco de dados
@app.before_request
def before_request():
    if db.is_closed():
        db.connect()

    user_id = session.get('_user_id')
    if user_id:
        user = User.get(User.id == int(user_id))
        g.user_adm = user.adm



        

@app.teardown_request
def teardown_request(exception):
    """Desconecta o banco após cada requisição."""
    if not db.is_closed():
        db.close()

# Registra as rotas usando blueprints
app.register_blueprint(LoginRoute( services_api=services_api).blueprint, url_prefix="/login")
app.register_blueprint(DashboardRoute(services_api=services_api).blueprint, url_prefix="/dashboard")
app.register_blueprint(UsersRoute().blueprint, url_prefix="/users")
app.register_blueprint(ProductsRoute(services_api=services_api).blueprint, url_prefix="/products")

if __name__ == '__main__':
    app.run(debug=True)
