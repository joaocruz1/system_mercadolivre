from flask import Blueprint, render_template, session, redirect, url_for
from flask_login import login_required
from services import Services
from dataclasses import dataclass

@dataclass
class ProductsRoute:

    blueprint_name : str = 'products'
    import_name: str = __name__
    services_api : Services = None

    def __post_init__(self):

        self.blueprint = Blueprint(self.blueprint_name, self.import_name)
        self.register_routes()
    
    def register_routes(self):
        @self.blueprint.route('/')
        @login_required
        def products():
            products_infos = self.services_api.import_info_products_list(self.services_api.import_id_products())
   
            return render_template('products.html',products_infos=products_infos)
        
        @self.blueprint.route('<product_id>/edit')
        @login_required
        def productedit(product_id):

            product_info = self.services_api.import_info_product(product_id)
            print(product_info)
            return render_template('productedit.html', product = product_info)