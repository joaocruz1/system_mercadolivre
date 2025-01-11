from flask import Flask, request, redirect, render_template, url_for, session, jsonify
from data.users_data import UserServices
from data.dataid import spreadsheet_id2
from flask_routes import FlaskRoute  # Importe a classe criada
from services import Services

app = Flask(__name__)
app.secret_key = 'system_ml$91873919'

# Inicializa o UserLogin
user_login = UserServices(spreadsheet_id2=spreadsheet_id2)
services_api = Services()

# Registra as rotas usando a classe FlaskRoute
FlaskRoute(app=app, user_login=user_login, services_api=services_api)

if __name__ == '__main__':
    app.run(debug=True)
    
    
    


