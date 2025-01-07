from flask import Flask, request, redirect, render_template, url_for, session, jsonify
from data.api_data import APIData 
from data.users_data import UserLogin
from data.dataid import spreadsheet_id2
from flask_routes import FlaskRoute  # Importe a classe criada

app = Flask(__name__)
app.secret_key = 'system_ml$91873919'

# Inicializa o UserLogin
user_login = UserLogin(spreadsheet_id2=spreadsheet_id2)

# Registra as rotas usando a classe FlaskRoute
FlaskRoute(app=app, user_login=user_login)

if __name__ == '__main__':
    app.run(debug=True)
    
    
    


