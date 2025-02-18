from flask import Blueprint, render_template, session, redirect, url_for, request
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
   
            return render_template('products/products.html',products_infos=products_infos)
        
        @self.blueprint.route('/newcategory')
        @login_required
        def newcategoryproduct():
            categories = self.services_api.import_categories()

            return render_template('products/productcategorynew.html', categories=categories)
        
        @self.blueprint.route('/new', methods=['POST'])
        @login_required
        def newproduct():

            if request.form['productSubcategory'] != "":
                category = request.form['productSubcategory']
            else:
                category = request.form['productCategory']
            
            category_attributes = self.services_api.import_category_attributes(category)
            
            return render_template('products/productnew.html', category_attributes=category_attributes)


        @self.blueprint.route('<product_id>/edit')
        @login_required
        def productedit(product_id):

            product_info = self.services_api.import_info_product(product_id)
            product_description = self.services_api.import_description_product(product_id)
            
            return render_template('products/productedit.html', product = product_info, product_description = product_description)
        
        @self.blueprint.route('<product_id>/<img_id>/delete')
        @login_required
        def imagedelete(product_id,img_id):
            self.services_api.delete_image_product(product_id,img_id)
            
            return redirect(url_for('products.productedit',product_id = product_id))


        @self.blueprint.route('<product_id>/edit/uptade', methods=['POST'])
        @login_required
        def productupdate(product_id):
        
            product_img = request.files.get('products/newImageUpload', None)

            product_title = request.form['productName']
            product_description = request.form['productDescription']
            product_price = request.form['productPrice']
            product_condition = request.form['productCondition']
            product_status = request.form.get('productStatus', None)
            product_quantity = request.form['productQuantity']

            if product_img is None:
                self.services_api.edit_infos_product(product_id, None, None, None, None, None, None, None)
            else:
                self.services_api.edit_infos_product(product_id, product_img, None, None, None, None, None, None)
            
            if not product_title and not product_description and not product_price and not product_condition and not product_status and not product_quantity:
                self.services_api.edit_infos_product(product_id, None, None, None, None, None, None, None)

            if product_title != "":
                self.services_api.edit_infos_product(product_id, None, product_title, None, None, None, None, None)
            
            if product_description != "":
                self.services_api.edit_infos_product(product_id, None, None, product_description, None, None, None, None)
            
            if product_price != "":
                self.services_api.edit_infos_product(product_id, None, None, None, product_price, None, None, None)

            if product_condition != "":
                self.services_api.edit_infos_product(product_id, None, None, None, None, product_condition, None, None) 

            if product_status != "":
                self.services_api.edit_infos_product(product_id, None, None, None, None, None, product_status, None)

            if product_quantity != "":
                self.services_api.edit_infos_product(product_id, None, None, None, None, None, None, product_quantity) 
            
              

            return redirect(url_for('products.productedit', product_id=product_id))