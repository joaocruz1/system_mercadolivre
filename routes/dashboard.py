from flask import Blueprint, render_template, session, redirect, url_for
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
        @self.blueprint.route('/dashboard')
        def dashboard():
            userinfo_ml = session.get('userinfo_ml')
            session['userinfo_ml'] = self.services_api.infouser()
            quantity_products = self.services_api.search_products()
            quantity_sales = self.services_api.import_sales()
            return render_template(
                'dashboard.html', 
                userinfo=userinfo_ml, 
                quantity_products=quantity_products, 
                quantity_sales=quantity_sales
            )
