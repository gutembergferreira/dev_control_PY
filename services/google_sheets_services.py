import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import credential

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_dict(credential, scope)
client = gspread.authorize(credentials)

spreadsheet = client.open('Devices&Accessories - Upgrades Validation - Eldorado Manaus')
aba_usuarios = spreadsheet.worksheet("ELD_USERS")
auditoria = spreadsheet.worksheet("LOG TRANSACTIONS")
new_dispositivos = spreadsheet.worksheet("DEVICES_ELD")
all_sim_cads = spreadsheet.worksheet("ELD_SIMCARDS")
all_dev_accessories = spreadsheet.worksheet("ELD_ACCESSORIES")