from app_dc import all_sim_cads
from datetime import datetime

def get_simcard_by_id(simcard_id):
    records = all_sim_cads.get_all_records()
    simcard = [record for record in records if record['ID'] == simcard_id]
    return simcard

def update_simcard(simcard):
    row = find_simcard_row(simcard['ID'])
    if row:
        timestamp = datetime.now().strftime('%d-%m-%Y')
        all_sim_cads.update_cell(row, 2, simcard['Empréstimo'])
        all_sim_cads.update_cell(row, 16, timestamp)

def find_simcard_row(simcard_id):
    simcards = all_sim_cads.get_all_records()

    for i, simcard in enumerate(simcards, start=2):
        if simcard['ID'] == simcard_id:
            return i

    return None

def get_all_sim_cards():
    records = all_sim_cads.get_all_records()
    sim_cards = [record for record in records]
    return sim_cards

def get_simcard(simcard_id):
    row = find_simcard_row(simcard_id)
    if row:
        simcards = all_sim_cads.get_all_records()
        simcard_info = simcards[row - 2]
        return {
            'ID': simcard_info['ID'],
            'Empréstimo': simcard_info['Empréstimo']
        }
    return None