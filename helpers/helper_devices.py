from app_dc import new_dispositivos, spreadsheet
from datetime import datetime

def get_device_by_id(device_id):
    records = new_dispositivos.get_all_records()
    devices = [record for record in records if record['ID'] == device_id]
    return devices

def update_device(device):
    row = find_device_row(device['ID'])
    if row:
        timestamp = datetime.now().strftime('%d-%m-%Y')
        new_dispositivos.update_cell(row, 2, device['Empréstimo'])
        new_dispositivos.update_cell(row, 29, timestamp)

def find_device_row(device_id):
    devices = new_dispositivos.get_all_records()

    for i, device in enumerate(devices, start=2):
        if device['ID'] == device_id:
            return i

    return None

def get_available_devices():
    sheet = spreadsheet.sheet1
    records = sheet.get_all_records()
    devices = [record for record in records]
    return devices

def get_all_devices():
    records = new_dispositivos.get_all_records()
    devices = [record for record in records]
    return devices

def is_device_available(device_id):
    devices = get_available_devices()

    for device in devices:
        if device['ID'] == int(device_id):
            return device['Status'] == 'Disponivel'

    return False

def search_devices(keyword):
    devices = get_available_devices()
    results = []
    for device in devices:
        if keyword.lower() in device['Responsável'].lower() or keyword in str(device['ID']) :
            results.append(device)
    return results

def get_device(device_id):
    row = find_device_row(device_id)
    if row:
        devices = new_dispositivos.get_all_records()
        device_info = devices[row - 2]
        return {
            'ID': device_info['ID'],
            'Empréstimo': device_info['Empréstimo']
        }
    return None