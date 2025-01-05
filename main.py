from flask import Flask, request, redirect, render_template, url_for, session, jsonify

from data.api_data import APIData


if __name__  == '__main__':
    api_data = APIData()
    api_data.datarows()
    
    


