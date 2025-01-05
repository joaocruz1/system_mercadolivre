from flask import Flask, request, redirect, render_template, url_for, session, jsonify
from token_refresh import TokenRefresh
from data.dataid import spreadsheet_id


if __name__  == '__main__':
    token_refresh = TokenRefresh(spreadsheet_id)
    token = token_refresh.token

    print("Dados retornados:", token)
    
    


