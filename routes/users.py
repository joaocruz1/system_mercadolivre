from flask import Blueprint, flash, render_template, request, redirect, url_for, session, jsonify, g
from flask_login import login_required
from dataclasses import dataclass
from data.users_data import UserServices
from database import User, Shop

@dataclass 
class UsersRoute:
    blueprint_name: str = "users"
    import_name: str = __name__
    users_service: UserServices = None

    def __post_init__(self):
        self.blueprint = Blueprint(self.blueprint_name, self.import_name)
        self.register_routes()

    
    def register_routes(self):
        @self.blueprint.before_request
        def check_admin():
            if not getattr(g, "user_adm", False):
                return redirect(url_for("dashboard.dashboard"))
            
        @self.blueprint.route('/')
        @login_required
        def users():
            users_database = User.select()
            for user in users_database:
                print(user.shop)
            return render_template('users.html', usersinfo=users_database, userinfo_ml=session.get('userinfo_ml'))
        

        @self.blueprint.route('/userinfo')
        @login_required
        def userinfo():
            return render_template('userinfo.html', userinfo_ml=session.get('userinfo_ml'),userinfo=session.get('userinfo') )


        @self.blueprint.route('/<int:user_id>/delete')
        @login_required
        def userdelete(user_id):

            user_to_delete = User.get(User.id == user_id)
            user_to_delete.delete_instance()

            return redirect(url_for('users.users'))


        @self.blueprint.route('/<int:user_id>/edit')
        @login_required
        def useredit(user_id):
            user_infos = User.get(User.id == user_id)

            return render_template('useredit.html', userinfo_ml=session.get('userinfo_ml'), user_infos=user_infos)


        @self.blueprint.route('/<int:user_id>/edit/update', methods=['POST'])
        @login_required
        def user_editupdate(user_id):
            User.update(name=request.form['name'],email=request.form['email']).where(User.id == user_id).execute()
            # Mensagem flash de sucesso
            flash("Usuário atualizado com sucesso!", "success")

            return redirect(url_for('users.useredit', user_id=user_id))
        
        @self.blueprint.route('/useradd')
        @login_required
        def useradd():
            return render_template('useradd.html', userinfo_ml=session.get('userinfo_ml'))
        
        @self.blueprint.route('/useradd/update', methods =['POST'])
        @login_required
        def user_addupdate():
            
            adm = request.form.get('adm')
            if adm == None:
                adm = False
            
            user_shop = session.get('userinfo', {}).get('shop_id')
            User.create(
                shop= Shop.get(Shop.id == user_shop),
                name=request.form['name'],
                email=request.form['email'],
                password=request.form['password'],
                adm=adm
            )

            return redirect(url_for('users.users'))

        