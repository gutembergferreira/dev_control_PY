from datetime import datetime
from app_dc import auditoria
def register_loan(accessorie_id=None,device_id=None, simcard_id=None, user=None, action=None):
    if device_id:
        timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        auditoria.append_row([timestamp, device_id, user, action])
    if accessorie_id:
        timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        auditoria.append_row([timestamp, accessorie_id, user, action])
    if simcard_id:
        timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        auditoria.append_row([timestamp, simcard_id, user, action])

def register_devolution(accessorie_id=None, device_id=None, simcard_id=None, user=None, action=None, storeid=None):
    if device_id:
        timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        auditoria.append_row([timestamp, device_id, user, action, '' , storeid])
    if accessorie_id:
        timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        auditoria.append_row([timestamp, accessorie_id, user, action, '' , storeid])
    if simcard_id:
        timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        auditoria.append_row([timestamp, simcard_id, user, action, '' , storeid])

def register_transfer(accessorie_id=None, device_id=None, simcard_id=None, user=None, new_user=None, comments=None):
    if device_id:
        timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        auditoria.append_row([timestamp, device_id, user, 'Transfer to '+ new_user, comments])
        auditoria.append_row([timestamp, device_id, new_user, 'Transferred from '+ user,comments])
    if accessorie_id:
        timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        auditoria.append_row([timestamp, accessorie_id, user, 'Transfer to '+ new_user, comments])
        auditoria.append_row([timestamp, accessorie_id, new_user, 'Transferred from '+ user,comments])        
    if simcard_id:
        timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        auditoria.append_row([timestamp, simcard_id, user, 'Transfer to '+ new_user, comments])
        auditoria.append_row([timestamp, simcard_id, new_user, 'Transferred from '+ user,comments])   