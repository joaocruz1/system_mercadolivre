from dataclasses import dataclass
from flask import Blueprint, render_template, session, redirect, url_for, request, flash

@dataclass
class HomeRoute:
    blueprint_name : str = 'home'
    import_name: str = __name__

    def __post_init__(self):
        self.blueprint = Blueprint(self.blueprint_name, self.import_name)
        self.register_routes()

    def register_routes(self):
        @self.blueprint.route('/')
        def home():
            return render_template('home.html')