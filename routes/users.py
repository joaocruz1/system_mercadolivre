from flask import Blueprint, flash, render_template, request, redirect, url_for, session, jsonify
from dataclasses import dataclass
from data.users_data import UserServices

@dataclass 
class UsersRoute:
    blueprint_name: str = "users"
    import_name: str = __name__
    users_service: UserServices = None

    def __post_init__(self):
        self.blueprint = Blueprint(self.blueprint_name, self.import_name)
        self.register_routes()
    
    def register_routes(self):
        @self.blueprint.route('/')
        def users():
            usersinfo = self.users_service.consult_users()
            return render_template('users.html', usersinfo=usersinfo, userinfo_ml=session.get('userinfo_ml'))

        @self.blueprint.route('/userinfo')
        def userinfo():
            return render_template('userinfo.html', userinfo_ml=session.get('userinfo_ml'),userinfo=session.get('userinfo') )


        @self.blueprint.route('/<int:user_id>/delete')
        def userdelete(user_id):

            self.users_service.delete_user(user_id)

            return redirect(url_for('users.users'))


        @self.blueprint.route('/<int:user_id>/edit')
        def useredit(user_id):
            user_infos = self.users_service.consult_user(user_id)

            return render_template('useredit.html', userinfo_ml=session.get('userinfo_ml'), user_infos=user_infos)


        @self.blueprint.route('/<int:user_id>/edit/update', methods=['POST'])
        def userupdate(user_id):
            name = request.form['name']
            email = request.form['email']
            update = {"name": name, "email": email}

            self.users_service.edit_user(user_id, update)

            # Mensagem flash de sucesso
            flash("Usuário atualizado com sucesso!", "success")

            return redirect(url_for('users.useredit', user_id=user_id))

        