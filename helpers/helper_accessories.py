from app_dc import all_dev_accessories
from datetime import datetime

def get_accessorie_by_id(accessorie_id):
    records = all_dev_accessories.get_all_records()
    accessorie = [record for record in records if record['ID'] == accessorie_id]
    return accessorie

def update_accessorie(accessorie):
    row = find_accessorie_row(accessorie['ID'])
    if row:
        timestamp = datetime.now().strftime('%d-%m-%Y')
        all_dev_accessories.update_cell(row, 2, accessorie['Empréstimo'])
        all_dev_accessories.update_cell(row, 7, timestamp)
        
def find_accessorie_row(accessorie_id):
    accessories = all_dev_accessories.get_all_records()

    for i, accessorie in enumerate(accessories, start=2):
        if accessorie['ID'] == accessorie_id:
            return i

    return None

def get_all_accessories():
    records = all_dev_accessories.get_all_records()
    accessories = [record for record in records]
    return accessories

def get_accessorie(accessorie_id):
    row = find_accessorie_row(accessorie_id)
    if row:
        accessories = all_dev_accessories.get_all_records()
        accessorie_info = accessories[row - 2]
        return {
            'ID': accessorie_info['ID'],
            'Empréstimo': accessorie_info['Empréstimo']
        }
    return None