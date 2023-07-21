from flask import Flask
from flask_login import LoginManager, login_required
from services.google_sheets_services import *
from config import template_dir, static_dir

# Configurações Flask
app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)
app.config.from_object('config')
app.config['CUSTOM_METHODS'] = ['PUT']
app.secret_key = '@W#E$R%R'
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

if __name__ == '__main__':
    app.run()


from routes.router_htmls import *
from routes.router_accessories import *
from routes.router_devices import *
from routes.router_htmls_admins import *
from routes.router_login import *
from routes.router_simcards import *