from werkzeug.security import check_password_hash
from flask_login import current_user
from app_dc import aba_usuarios, new_dispositivos, all_sim_cads, all_dev_accessories, spreadsheet
from helpers.helper_devices import get_device
from helpers.helper_accessories import get_accessorie
from helpers.helper_simcards import get_simcard

def validate_login(username,password):
    users = aba_usuarios.get_all_values()
    for user in users:
        if user[1] == username and check_password_hash(user[4], password) :
            return True
    return False

def get_info_user():
    users = aba_usuarios.get_all_values()
    for user in users:
        if user[1] == current_user.id:
            return user
        
def get_user_info():
    if current_user.is_authenticated:
        return current_user.id
    
def is_user_allowed(device_id=None,accessorie_id=None, simcard_id=None):
    if device_id:
        current_user = get_user_info()
        device = get_device(device_id)
        if device['Empréstimo'] == current_user:
            return True
        return False
    if accessorie_id:
        current_user = get_user_info()
        accessorie = get_accessorie(accessorie_id)
        if accessorie['Empréstimo'] == current_user:
            return True
        return False       
    if simcard_id:
        current_user = get_user_info()
        simcard = get_simcard(simcard_id)
        if simcard['Empréstimo'] == current_user:
            return True
        return False     
    
def get_core_id(text):
    partes = text.split("-")
    resultado = partes[1].strip()
    return resultado

def get_info_new_user(new_user):
    users = aba_usuarios.get_all_values()
    for user in users:
        if user[1] == new_user:
            return user
        
def get_user_loaned_devices(user):
    records = new_dispositivos.get_all_records()
    devices = [record for record in records if record['Empréstimo'] == user]
    return devices

def get_user_loaned_accessories(user):
    records = all_dev_accessories.get_all_records()
    accessories = [record for record in records if record['Empréstimo'] == user]
    return accessories

def get_user_loaned_simcards(user):
    records = all_sim_cads.get_all_records()
    simcards = [record for record in records if record['Empréstimo'] == user]
    return simcards

def get_user_transactions(user=None, transaction=""):
    auditoria = spreadsheet.worksheet("LOG TRANSACTIONS")
    records = auditoria.get_all_records()
    if (user == "" and transaction == ""):
        user_transactions = [record for record in records]
        return user_transactions
    if (transaction == "all"):
        user_transactions = [record for record in records if record['USER'] == user]
        return user_transactions

    if (transaction == "Loan" and user is not None):
        user_transactions = [record for record in records if (record['USER'] == user and record['ACTION'] == transaction )]
        return user_transactions

    if (transaction == 'Loan' and user is None):
        all_loans_transactions = [record for record in records if (record['ACTION'] == transaction )]
        return all_loans_transactions

    if (transaction == "Devolution" and user is not None):
        user_transactions = [record for record in records if (record['USER'] == user and record['ACTION'] == transaction )]
        return user_transactions

    if (transaction == 'Devolution' and user is None):
        all_devolutions_transactions = [record for record in records if (record['ACTION'] == transaction )]
        return all_devolutions_transactions

    if (transaction == "Transfer" and user is not None):
        user_transactions = [record for record in records if (record['USER'] == user and record['ACTION'].startswith(transaction) )]
        return user_transactions

    if (transaction == 'Transfer' and user is None):
        all_transfers_transactions = [record for record in records if (record['ACTION'].startswith(transaction) )]
        return all_transfers_transactions