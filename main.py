from flask import Flask
from flask_session import Session
from routes.login import LoginRoute
from routes.dashboard import DashboardRoute
from routes.users import UsersRoute
from data.users_data import UserServices
from data.dataid import spreadsheet_id2
from services import Services

# Inicializa o aplicativo Flask
app = Flask(__name__)
app.secret_key = 'system_ml$91873919'
app.config['SESSION_TYPE'] = 'filesystem'  # Configuração de sessão
Session(app)

# Inicializa serviços
user_services = UserServices(spreadsheet_id2=spreadsheet_id2)
services_api = Services()

# Registra as rotas usando blueprints
app.register_blueprint(LoginRoute(user_service=user_services).blueprint, url_prefix="/login")
app.register_blueprint(DashboardRoute(services_api=services_api).blueprint, url_prefix="/dashboard")
app.register_blueprint(UsersRoute(users_service=user_services).blueprint, url_prefix="/users")

if __name__ == '__main__':
    app.run(debug=True)

    
    
    


