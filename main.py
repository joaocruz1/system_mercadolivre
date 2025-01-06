from flask import Flask, request, redirect, render_template, url_for, session, jsonify
from data.api_data import APIData 
from data.users_data import UserLogin
from data.dataid import spreadsheet_id2



    

if __name__  == '__main__':
    login_system = UserLogin(spreadsheet_id2=spreadsheet_id2)
    login_system.login()
    login_system.adduser()
    
    
    
    


