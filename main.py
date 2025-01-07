from flask import Flask, request, redirect, render_template, url_for, session, jsonify
from data.api_data import APIData 
from data.users_data import UserLogin
from data.dataid import spreadsheet_id2

app = Flask(__name__)

user_login = UserLogin(spreadsheet_id2=spreadsheet_id2)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        shop = request.form['shop']

        # Mock request data as JSON to pass to login function
        request.json = {"email": email, "password": password, "shop": shop}
        return user_login.login()
    return render_template('login.html')


if __name__  == '__main__':
    app.run()
    
    
    
    


