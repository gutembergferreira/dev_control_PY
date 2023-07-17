from flask import Flask
from flask_login import LoginManager, login_required
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import credential, template_dir, static_dir

# Configurações Flask
app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)
app.config.from_object('config')
app.config['CUSTOM_METHODS'] = ['PUT']
app.secret_key = '@W#E$R%R'
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

# Configurações do Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_dict(credential, scope)
client = gspread.authorize(credentials)

global spreadsheet
spreadsheet = client.open('Devices&Accessories - Upgrades Validation - Eldorado Manaus')

global aba_usuarios
aba_usuarios = spreadsheet.worksheet("ELD_USERS")

global auditoria
auditoria = spreadsheet.worksheet("LOG TRANSACTIONS")

global new_dispositivos
new_dispositivos = spreadsheet.worksheet("DEVICES_ELD")

global all_sim_cads
all_sim_cads = spreadsheet.worksheet("ELD_SIMCARDS")

global all_dev_accessories
all_dev_accessories = spreadsheet.worksheet("ELD_ACCESSORIES")


from routes.router_htmls import * 
from routes.router_accessories import *
from routes.router_devices import *
from routes.router_htmls_admins import *
from routes.router_login import *
from routes.router_simcards import * 