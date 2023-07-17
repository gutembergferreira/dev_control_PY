from flask import redirect, url_for, flash, request, render_template
from helpers.helper_register import register_loan, register_devolution, register_transfer
from app_dc import app, login_required
from helpers.helper_devices import *
from helpers.helper_users import *
from helpers.helper_simcards import *
from helpers.helper_accessories import *
from helpers.helper_sendMessage import sendMessageWebhook


# Rota para empréstimo de dispositivo
@app.route('/loan/<device_id>')
@login_required
def loan_device(device_id):
    user = get_user_info()
    user_info = get_info_user()
    device = get_device(device_id)
    if (device['Empréstimo'] == ''):
        device['Empréstimo'] = user
        update_device(device)
        register_loan(None, device_id,None, user, 'Loan')
        sendMessageWebhook(user_info[7], None, "Loan", device_id, None, None)
        flash('Device Loan '+ device_id +' succssesfully done.', 'success')
        return redirect(url_for('all_devices'))
    else:
        flash('It is not possible to carry out the loan! Device already allocated, request transfer', 'error')
        return redirect(url_for('all_devices'))

@app.route('/return/<device_id>')
@login_required
def return_device(device_id):
    if is_user_allowed(device_id, None,None):
        user = get_user_info()
        user_info = get_info_user()
        device = get_device(device_id)
        storeid = request.args['armario']
        device['Empréstimo'] = ''
        update_device(device)
        register_devolution(None,device_id, None, user, 'Devolution', storeid)
        flash('Device return '+ device_id +' successfully completed.', 'success')
        sendMessageWebhook(user_info[7], None, "Devolution", device_id, None, None)
        return redirect(url_for('all_devices'))
    else:
        flash('Only the user who made the loan or administrators can make the return.', 'error')
        return redirect(url_for('all_devices'))
    
        

@app.route('/transfer_device/<device_id>', methods=['GET', 'POST'])
@login_required
def transfer_device(device_id):
    device = get_device_by_id(device_id)
    users = aba_usuarios.get_all_values()
    user_info = get_info_user()
    del users[0]
    users_table=[]
    if device is None:
        flash('Device not found.', 'error')
        return redirect(url_for('all_devices'))

    if device[0]['Empréstimo'] != current_user.id:
        flash('You can only transfer devices allocated to you.', 'error')
        return redirect(url_for('all_devices'))

    if request.method == 'POST':
        new_user = request.form['new_user']
        comments = request.form['comments']
        new_user = get_core_id(new_user)
        new_user_info = get_info_new_user(new_user)
        if new_user == device[0]['Empréstimo']:
            flash('This type of transfer is not allowed.', 'error')
            return render_template('newalldevices.html', device_id=device_id, users=users, user_info=user_info)
        if not new_user:
            flash('Please enter the username for the transfer.', 'error')
            return render_template('newalldevices.html', device_id=device_id, users=users, user_info=user_info)
        for user in users:
            users_table.append(user[1])
        if new_user not in users_table:
            flash('Username invalid or not registered in the base. Try again.', 'error')
            return render_template('newalldevices.html', device_id=device_id, users=users, user_info=user_info)
        device[0]['Empréstimo'] = new_user
        update_device(device[0])
        register_transfer(None, device[0]['ID'],None,current_user.id, new_user, comments)
        sendMessageWebhook(user_info[7], new_user_info[7], "Transfer", device_id, None, None)
        flash('Device '+ device[0]['ID'] +' successfully transferred to {}'.format(new_user_info[6]), 'success')
        return redirect(url_for('all_devices'))