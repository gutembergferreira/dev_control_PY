from flask import redirect, url_for, render_template
from app_dc import app, login_required
from helpers.helper_devices import *
from helpers.helper_users import *
from helpers.helper_simcards import *
from helpers.helper_accessories import *

@app.route('/')
@login_required
def home():
    return redirect(url_for('all_devices'))

# Rota inicial
@app.route('/alldevices')
@login_required
def all_devices():
    devices = get_all_devices()
    current_user = get_user_info()
    users = aba_usuarios.get_all_records()
    info_user = get_info_user()
    return render_template('newalldevices.html', devices=devices, current_user=current_user, users=users, info_user=info_user)

@app.route('/allsimcards')
@login_required
def all_sim_cards():
    simcards = get_all_sim_cards()
    current_user = get_user_info()
    users = aba_usuarios.get_all_records()
    info_user = get_info_user()
    return render_template('sim_cards.html', simcards=simcards, current_user=current_user, users=users, info_user=info_user)

@app.route('/allaccessories')
@login_required
def all_accessories():
    accessories = get_all_accessories()
    current_user = get_user_info()
    users = aba_usuarios.get_all_records()
    info_user = get_info_user()
    return render_template('accessories.html', accessories=accessories, current_user=current_user, users=users, info_user=info_user)

@app.route('/myresources')
@login_required
def myresources():
    current_user = get_user_info()
    devices = get_user_loaned_devices(current_user)
    accessories = get_user_loaned_accessories(current_user)
    simcards = get_user_loaned_simcards(current_user)
    users = aba_usuarios.get_all_records()
    users_sorted = sorted(users, key=lambda x: x['NAME'])
    users = users_sorted
    info_user = get_info_user()
    return render_template('my_resources.html', accessories=accessories,simcards=simcards, devices=devices,current_user=current_user, users=users, info_user=info_user)

@app.route('/history')
@login_required
def history():
    user = current_user.id
    info_user = get_info_user()
    all_transactions = get_user_transactions(user, "all")
    loan_transactions = get_user_transactions(user, "Loan")
    transfer_transactions = get_user_transactions(user, "Transfer")
    devolution_transactions = get_user_transactions(user, "Devolution")
    return render_template('history.html', info_user=info_user, transactions=all_transactions, loan_transactions = loan_transactions, transfer_transactions=transfer_transactions, devolution_transactions=devolution_transactions, user=user)



@app.route('/account')
@login_required
def account():
    info_user = get_info_user()
    return render_template('user.html', info_user=info_user)

