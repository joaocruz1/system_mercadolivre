from flask import Flask, request, redirect, render_template, url_for, session, jsonify
from data.api_data import APIData 
from data.users_data import UserLogin
from data.dataid import spreadsheet_id2

app = Flask(__name__)

user_login = UserLogin(spreadsheet_id2=spreadsheet_id2)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    try:
        email = request.form['email']
        password = request.form['password']
        shop = request.form['shop']

        # Armazena os dados em uma variável
        data = {"email": email, "password": password, "shop": shop}

        # Realiza o login com os dados
        return user_login.login(data)
    except Exception as e:
        print(f"Erro no login: {e}")
        return jsonify({"error": "Erro no servidor"}), 500



if __name__  == '__main__':
    app.run(debug=True)
    
    
    
    


