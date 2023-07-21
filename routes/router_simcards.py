from flask import redirect, url_for, request, flash,render_template
from helpers.helper_sendMessage import *
from helpers.helper_register import register_loan, register_devolution, register_transfer
from app_dc import app, login_required
from helpers.helper_devices import *
from helpers.helper_users import *
from helpers.helper_simcards import *
from helpers.helper_accessories import *


# Rota para transferência de SIM CARDS
@app.route('/transfer_simcard/<simcard_id>', methods=['POST'])
@login_required
def transfer_simcard(simcard_id):
    simcard = get_simcard_by_id(simcard_id)
    users = aba_usuarios.get_all_values()
    user_info = get_info_user()
    del users[0]
    users_table=[]
    if simcard is None:
        flash('SIM Card not found.', 'error')
        return redirect(url_for('all_sim_cards'))

    if simcard[0]['Empréstimo'] != current_user.id:
        flash('You can only transfer SIM Cards allocated to you.', 'error')
        return redirect(url_for('all_sim_cards'))

    new_user = request.form['new_user']
    comments = request.form['comments']
    new_user = get_core_id(new_user)
    new_user_info = get_info_new_user(new_user)
    if new_user == simcard[0]['Empréstimo']:
        flash('This type of transfer is not allowed.', 'error')
        return render_template('sim_cards.html', simcard_id=simcard_id, users=users, user_info=user_info)
    if not new_user:
        flash('Please enter the username for the transfer.', 'error')
        return render_template('sim_cards.html', simcard_id=simcard_id, users=users, user_info=user_info)
    for user in users:
        users_table.append(user[1])
    if new_user not in users_table:
        flash('Username invalid or not registered in the base. Try again.', 'error')
        return render_template('sim_cards.html', simcard_id=simcard_id, users=users, user_info=user_info)
    simcard[0]['Empréstimo'] = new_user
    update_simcard(simcard[0])
    register_transfer(None, None,simcard[0]['ID'],current_user.id, new_user, comments)
    sendMessageWebhook(user_info[7], new_user_info[7], "Transfer", None, None, simcard_id)
    flash('SIM Card '+ simcard[0]['ID'] +' successfully transferred to {}'.format(new_user_info[6]), 'success')
    return redirect(url_for('all_sim_cards'))

# Rota para devolução de SIMCARD
@app.route('/return_simcard/<simcard_id>')
@login_required
def return_simcard(simcard_id):
    if is_user_allowed(None,None,simcard_id):
        user = get_user_info()
        user_info = get_info_user()
        simcard = get_simcard(simcard_id)
        storeid = request.args['armario']
        simcard['Empréstimo'] = ''
        update_simcard(simcard)
        register_devolution(None,None,simcard_id, user, 'Devolution', storeid)
        flash('SIM Card return '+ simcard_id +' successfully completed.', 'success')
        sendMessageWebhook(user_info[7], None, "Devolution", None,None,simcard_id)
        return redirect(url_for('all_sim_cards'))
    else:
        flash('Only the user who made the loan or administrators can make the return.', 'error')
        return redirect(url_for('all_accessories'))
    
 
# Rota para empréstimo de SIM CARD    
@app.route('/loan_simcard/<simcard_id>')
@login_required
def loan_simcard(simcard_id):
    user = get_user_info()
    user_info = get_info_user()
    simcard = get_simcard(simcard_id)
    if (simcard['Empréstimo'] == ''):
        simcard['Empréstimo'] = user
        update_simcard(simcard)
        register_loan(None, None, simcard_id, user, 'Loan')
        sendMessageWebhook(user_info[7], None, "Loan", None, None, simcard_id)
        flash('SIM Card Loan '+ simcard_id +' successfully done.', 'success')
        return redirect(url_for('all_sim_cards'))
    else:
        flash('It is not possible to carry out the loan! Accessorie already allocated, request transfer', 'error')
        return redirect(url_for('all_sim_cards'))