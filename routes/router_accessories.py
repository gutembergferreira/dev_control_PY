from flask import redirect, url_for, request, flash, render_template
from helpers.helper_sendMessage import *
from helpers.helper_register import register_loan, register_devolution, register_transfer
from flask import redirect, url_for
from helpers.helper_register import *
from app_dc import app, login_required
from helpers.helper_devices import *
from helpers.helper_users import *
from helpers.helper_simcards import *
from helpers.helper_accessories import *


# Rota para devolução de acessorio
@app.route('/return_acessorie/<accessorie_id>')
@login_required
def return_accessorie(accessorie_id):
    if is_user_allowed(None,accessorie_id, None):
        user = get_user_info()
        user_info = get_info_user()
        accessorie = get_accessorie(accessorie_id)
        storeid = request.args['armario']
        accessorie['Empréstimo'] = ''
        update_accessorie(accessorie)
        register_devolution(accessorie_id, None, None, user, 'Devolution', storeid)
        flash('Accessorie return '+ accessorie_id +' successfully completed.', 'success')
        sendMessageWebhook(user_info[7], None, "Devolution", None, accessorie_id, None)
        return redirect(url_for('all_accessories'))
    else:
        flash('Only the user who made the loan or administrators can make the return.', 'error')
        return redirect(url_for('all_accessories'))
    
# Rota para empréstimo de acessorio
@app.route('/loan_accessorie/<accessorie_id>')
@login_required
def loan_accessorie(accessorie_id):

    user = get_user_info()
    user_info = get_info_user()
    accessorie = get_accessorie(accessorie_id)
    if (accessorie['Empréstimo'] == ''):
        accessorie['Empréstimo'] = user
        update_accessorie(accessorie)
        register_loan(accessorie_id,None, None, user, 'Loan')
        sendMessageWebhook(user_info[7], None, "Loan", None, accessorie_id, None)
        flash('Accessorie Loan '+ accessorie_id +' succssesfully done.', 'success')
        return redirect(url_for('all_accessories'))
    else:
        flash('It is not possible to carry out the loan! Accessorie already allocated, request transfer', 'error')
        return redirect(url_for('all_accessories'))
    

# Rota para transferência de acessorios
@app.route('/transfer_accessorie/<accessorie_id>', methods=['POST'])
@login_required
def transfer_accessorie(accessorie_id):
    accessorie = get_accessorie_by_id(accessorie_id)
    users = aba_usuarios.get_all_values()
    user_info = get_info_user()
    del users[0]
    users_table=[]
    if accessorie is None:
        flash('Accessorie not found.', 'error')
        return redirect(url_for('all_accessories'))

    if accessorie[0]['Empréstimo'] != current_user.id:
        flash('You can only transfer Accessorie allocated to you.', 'error')
        return redirect(url_for('all_accessorie'))

    new_user = request.form['new_user']
    comments = request.form['comments']
    new_user = get_core_id(new_user)
    new_user_info = get_info_new_user(new_user)
    if new_user == accessorie[0]['Empréstimo']:
        flash('This type of transfer is not allowed.', 'error')
        return render_template('accessories.html', accessorie_id=accessorie_id, users=users, user_info=user_info)
    if not new_user:
        flash('Please enter the username for the transfer.', 'error')
        return render_template('accessories.html', accessorie_id=accessorie_id, users=users, user_info=user_info)
    for user in users:
        users_table.append(user[1])
    if new_user not in users_table:
        flash('Username invalid or not registered in the base. Try again.', 'error')
        return render_template('accessories.html', accessorie_id=accessorie_id, users=users, user_info=user_info)
    accessorie[0]['Empréstimo'] = new_user
    update_accessorie(accessorie[0])
    register_transfer(accessorie[0]['ID'], None, None,current_user.id, new_user, comments)
    sendMessageWebhook(user_info[7], new_user_info[7], "Transfer", None, accessorie_id, None)
    flash('Device '+ accessorie[0]['ID'] +' successfully transferred to {}'.format(new_user_info[6]), 'success')
    return redirect(url_for('all_accessories'))