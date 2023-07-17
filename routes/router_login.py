from flask import redirect, url_for, request, flash, render_template
from flask_login import login_user, current_user, logout_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from helpers.helper_register import *
from app_dc import app, login_required, login_manager
from helpers.helper_devices import *
from helpers.helper_users import *
from helpers.helper_simcards import *
from helpers.helper_accessories import *


class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['user_id']
        password = request.form['password']
        if validate_login(username,password):
            user = User(username)
            login_user(user)
            return redirect(url_for('myresources'))
        else:
            flash('core-id or password is invalid', 'error')
    return render_template('login.html')

# Rota de logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/change_password', methods=['POST'])
@login_required
def change_password():
    current_password = request.form['current_password']
    new_password = request.form['new_password']
    confirm_password = request.form['confirm_password']
    user_atual = get_info_user()
    if check_password_hash(user_atual[4], current_password):
        if new_password == confirm_password:
            user_atual[4] = generate_password_hash(new_password)
            users = aba_usuarios.get_all_values()
            for i, user in enumerate(users, start=1):
                if user[1] == current_user.id:
                    row=i
            if row:
                aba_usuarios.update_cell(row, 5, user_atual[4])
            flash('Password changed successfully', 'success')
        else:
            flash('New password and confirmation do not match', 'error')
    else:
        flash('Incorrect current password', 'error')

    return redirect(url_for('account'))

@app.route('/reset_password', methods=['POST'])
@login_required
def reset_password():
    info_user = get_info_user()
    if info_user[3] == 'ADMIN':
        requestuser = request.form['userSelect']
        users = aba_usuarios.get_all_values()
        for user in users:
            if requestuser == user[1]:
                user[4] = generate_password_hash('12345')
                aba_usuarios.update_cell(int(user[0])+1, 5, user[4])
                flash('Password successfully reset! New Password: 12345 | Ask the user to change the password.', 'success')
        return redirect(url_for('admin_accounts'))
    else:
        flash('Url not allowed for your Profile.', 'error')
        return redirect(url_for('myresources'))