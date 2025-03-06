from flask import Blueprint, render_template, session, redirect, url_for, request, flash
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
            
            return render_template('products/productnew.html', category_attributes=category_attributes, category_id = category)

        @self.blueprint.route('<category_id>/newuptade', methods=['POST'])
        @login_required
        def newproductupdate(category_id):
            
            name = request.form['productName']
            description = request.form['productDescription']
            price = request.form['productPrice']
            
            condition = request.form['productCondition']
            avaiilable_quantity = request.form['productQuantity'] 
            attributes = self.services_api.import_category_attributes(category_id)
            attributes_request = []

            for attribute in attributes:
                if request.form[attribute['id']] != "":
                    attributes_request.append({
                        'id': attribute['id'],
                        'value_name': request.form[attribute['id']]
                    })

            self.services_api.publi_product(name,category_id,price,avaiilable_quantity,condition,description,attributes_request)

            return redirect(url_for('products.products'))


        @self.blueprint.route('<product_id>/edit')
        @login_required
        def productedit(product_id):

            product_info = self.services_api.import_info_product(product_id)
            product_description = self.services_api.import_description_product(product_id)
            
            return render_template('products/productedit.html', product = product_info, product_description = product_description)
        
        @self.blueprint.route('<product_id>/<img_id>/delete')
        @login_required
        def imagedelete(product_id,img_id):
            message = self.services_api.delete_image_product(product_id,img_id)
            flash(message['message'], message['status'])
            
            return redirect(url_for('products.productedit',product_id = product_id))


        @self.blueprint.route('<product_id>/edit/uptade', methods=['POST'])
        @login_required
        def productupdate(product_id):
            product_img = request.files.get('newImageUpload', None)
            
            product_title = request.form['productName']
            product_description = request.form['productDescription']
            product_price = request.form['productPrice']
            product_condition = request.form['productCondition']
            product_status = request.form.get('productStatus', None)
            product_quantity = request.form['productQuantity']

            if product_img is not None and product_img.filename == '':
                product_img = None  

            message = self.services_api.edit_infos_product(
                product_id, product_img, product_title, product_description, product_price, product_condition, product_status, product_quantity
            )

            flash(message["message"], message["status"])
            return redirect(url_for('products.productedit', product_id=product_id))