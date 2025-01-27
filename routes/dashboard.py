from flask import Blueprint, render_template, session, redirect, url_for, g
from flask_login import login_required
from dataclasses import dataclass
from services import Services

@dataclass
class DashboardRoute:
    blueprint_name: str = "dashboard"
    import_name: str = __name__
    services_api: Services = None

    def __post_init__(self):
        self.blueprint = Blueprint(self.blueprint_name, self.import_name)
        self.register_routes()

    def register_routes(self):
        @self.blueprint.route('/')
        @login_required
        def dashboard():
            g.user_adm = session.get('userinfo', {}).get('user_adm')
            if g.user_adm:
                session['userinfo_ml'] = self.services_api.infouser()
                userinfo = session.get('userinfo')
                userinfo_ml = session.get('userinfo_ml')
                quantity_products = self.services_api.search_products()
                quantity_sales = self.services_api.import_sales()
                return render_template(
                    'dashboard.html', 
                    userinfo_ml=userinfo_ml, 
                    quantity_products=quantity_products, 
                    quantity_sales=quantity_sales,
                    userinfo=userinfo
                )
        
        @self.blueprint.route('/check-session')
        @login_required
        def check_session():
            if session:
                return {key: session[key] for key in session}, 200  # Retorna as informações da sessão como JSON
            else:
                return "No session data available", 200
        
        @self.blueprint.route('/clear-session')
        @login_required
        def clear_session():
            session.clear()  # Limpa todos os dados armazenados na sessão
            return redirect(url_for('login.login'))  # Redireciona para a página inicial (ou outra página desejada)
