from flask import redirect, url_for, request, flash, render_template
from app_dc import app, login_required, auditoria
from helpers.helper_users import *
import pandas as pd
import plotly.express as px
from werkzeug.security import generate_password_hash
import re

@app.route('/info-dash')
@login_required
def info_dash():
    info_user = get_info_user()
    if info_user[3] == 'ADMIN':
        transactions = auditoria.get_all_values()
        devices = new_dispositivos.get_all_values()
        users= aba_usuarios.get_all_values()


        # Número total de transações
        filtered_transactions = [transaction for transaction in transactions if not transaction[4].startswith('transferred from')]
        total_transactions = len(filtered_transactions) -1
        total_devices = len(devices) - 1
        df_devices = pd.DataFrame(devices)
        total_devices_ext = len(df_devices[df_devices[1] == 'Empréstimo interno Eldorado'])
        total_devices_block = len(df_devices[df_devices[1] == 'Bloqueado/Defeito'])
        total_devices_ana_devolution = len(df_devices[df_devices[1] == 'Em analise para devolução'])
        total_devices_devolution = len(df_devices[df_devices[1] == 'Amostra devolvida'])
        total_devices_loan = len(df_devices[df_devices[1] != '']) - total_devices_ext - total_devices_block - total_devices_ana_devolution - total_devices_devolution - 1
        total_devices_free = len(df_devices[df_devices[1] == ''])
        total_users= len(users) - 5

        # Gráfico de ações
        actions_df = pd.DataFrame(transactions, columns=['DATE', 'ID_DEVICE', 'USER', 'ACTION', 'COMMENTS', 'STORE_ID', 'ID_TRANSACTION'])
        actions_df['ACTION'] = actions_df['ACTION'].apply(lambda x: re.sub(r'Transfer to*', 'Transfers to', x))
        actions_df['ACTION'] = actions_df['ACTION'].apply(lambda x: re.sub(r'transferred from.*', 'Transferred from', x))
        actions_df['ACTION'] = actions_df['ACTION'].apply(lambda x: re.sub(r'Transfer.*|transferred from.*', 'Transfers', x))
        actions_df['ACTION'] = actions_df['ACTION'].apply(lambda x: re.sub(r'Devolution.*', 'Devolutions', x))
        actions_df['ACTION'] = actions_df['ACTION'].apply(lambda x: re.sub(r'Loan.*', 'Loans', x))
        actions_counts = actions_df['ACTION'].value_counts()
        #actions_counts = actions_counts[actions_counts.index != 'Transferido']
        actions_counts = actions_counts[actions_counts.index != 'ACTION']
        actions_fig = px.bar(actions_counts, x=actions_counts.index, y=actions_counts.values)
        actions_fig.update_layout(yaxis=dict(title='Amount'), xaxis=dict(title='Actions'))
        actions_fig.update_traces(hovertemplate='Action: %{x}<br>Amount: %{y}')
        actions_graphJSON = actions_fig.to_json()

        # Atividade por usuário
        user_counts = actions_df['USER'].value_counts()
        user_counts = user_counts[user_counts.index != 'USER']
        user_fig = px.bar(user_counts, x=user_counts.index, y=user_counts.values)
        user_fig.update_layout(yaxis=dict(title='Transactions'), xaxis=dict(title='Users'))
        user_fig.update_traces(hovertemplate='User: %{x}<br>Transactions: %{y}')
        user_graphJSON = user_fig.to_json()

        # Atividade por dispositivo
        device_counts = actions_df['ID_DEVICE'].value_counts()
        device_counts = device_counts[device_counts.index != 'ID']
        device_fig = px.bar(device_counts, x=device_counts.index, y=device_counts.values)
        device_fig.update_layout(yaxis=dict(title='Transactions'))
        device_fig.update_traces(hovertemplate='Device ID: %{x}<br>Transactions: %{y}')
        device_graphJSON = device_fig.to_json()

        # Devices Alocados Por Usuários
        dispositivos_df = pd.DataFrame(new_dispositivos.get_all_values()[1:], columns=new_dispositivos.get_all_values()[0])
        dispositivos_alocados = dispositivos_df[dispositivos_df['Empréstimo'] != '']
        valores_indesejados = ['Em analise para devolução', 'Empréstimo interno Eldorado', 'Amostra devolvida', 'Bloqueado/Defeito']
        dispositivos_alocados = dispositivos_alocados[~dispositivos_alocados['Empréstimo'].isin(valores_indesejados)]
        alocacao_por_usuario = dispositivos_alocados['Empréstimo'].value_counts()
        fig = px.bar(alocacao_por_usuario, x=alocacao_por_usuario.index, y=alocacao_por_usuario.values)
        fig.update_layout(yaxis=dict(title='number of devices'))
        #fig.update_layout(title='Quantidade de Dispositivos Alocados por Usuário',yaxis=dict(title='Quantidade de Devices'))
        fig.update_traces(hovertemplate='User: %{x}<br>Number of devices: %{y}')

        devices_user_graphJSON = fig.to_json()


        dispositivos_df2 = pd.DataFrame(new_dispositivos.get_all_values()[1:], columns=new_dispositivos.get_all_values()[0])
        contagem_storage = dispositivos_df2['Storage ID'].value_counts()

        # Criação do gráfico de barras
        def custom_sort(x):
            try:
                return int(x)
            except ValueError:
                return float('inf')
        
        
        contagem_storage_sorted = contagem_storage.sort_index(key=lambda x: x.map(custom_sort))
        fig = px.bar(contagem_storage_sorted, x=contagem_storage_sorted.index, y=contagem_storage_sorted.values)
        fig.update_layout(xaxis=dict(title='Storage ID'), yaxis=dict(title='Number of Devices'))
        fig.update_traces(hovertemplate='Storage ID: %{x}<br>Number of Devices: %{y}')

        # Obtém o JSON do gráfico
        storage_graphJSON = fig.to_json()

        dispositivos_df3 = pd.DataFrame(new_dispositivos.get_all_values()[1:], columns=new_dispositivos.get_all_values()[0])
        contagem_storage = dispositivos_df3['Device'].value_counts()

        # Criação do gráfico de barras
        fig = px.bar(contagem_storage, x=contagem_storage.index, y=contagem_storage.values)
        fig.update_layout(xaxis=dict(title='Devices'), yaxis=dict(title='Number of Devices'))
        fig.update_traces(hovertemplate='Device: %{x}<br>Number of Devices: %{y}')

        # Obtém o JSON do gráfico
        devices_graphJSON = fig.to_json()

        return render_template('info_dash.html',
                            transactions=transactions, info_user=info_user, total_transactions=total_transactions,
                            actions_graphJSON=actions_graphJSON, user_graphJSON=user_graphJSON, device_graphJSON=device_graphJSON,
                            total_devices=total_devices,total_devices_loan=total_devices_loan,
                            total_devices_free=total_devices_free,total_devices_block=total_devices_block,total_devices_ext=total_devices_ext,
                            total_devices_ana_devolution=total_devices_ana_devolution, total_devices_devolution=total_devices_devolution,
                            total_users=total_users, devices_user_graphJSON=devices_user_graphJSON, storage_graphJSON=storage_graphJSON,
                            devices_graphJSON=devices_graphJSON)
    else:
        flash('Url not allowed for your Profile.', 'error')
        return redirect(url_for('myresources'))
    
@app.route('/admin-accounts')
@login_required
def admin_accounts():
    info_user = get_info_user()
    if info_user[3] == 'ADMIN':
        users = aba_usuarios.get_all_records()
        return render_template('admin_accounts.html', info_user=info_user, users=users)
    else:
        flash('Url not allowed for your Profile.', 'error')
        return redirect(url_for('myresources'))
    
@app.route('/admin-history')
@login_required
def admin_history():
    info_user = get_info_user()
    if info_user[3] == 'ADMIN':
        user = current_user.id
        all_transactions = get_user_transactions("", "")
        loan_transactions = get_user_transactions(None, "Loan")
        devolution_transactions = get_user_transactions(None, "Devolution")
        transfer_transactions = get_user_transactions(None, "Transfer")
        return render_template('admin_history.html', info_user=info_user, transactions=all_transactions, user=user, loan_transactions=loan_transactions,
                               devolution_transactions=devolution_transactions, transfer_transactions=transfer_transactions)
    else:
        flash('Url not allowed for your Profile.', 'error')
        return redirect(url_for('myresources'))
    
@app.route('/admin-users', methods=['POST', 'GET'])
@login_required
def admin_users():
    info_user = get_info_user()
    if info_user[3] == 'ADMIN':
        if request.method == 'POST':
            username = request.form['username']
            password = generate_password_hash('123')
            email = request.form['email']
            permission = request.form['permission']
            name = request.form['name']
            user_id_google = request.form['userid']
            all_users = aba_usuarios.get_all_values()
            users = aba_usuarios.get_all_records()
            for user in all_users:
                if user[1] == username:
                    flash('Core-id already registered in the Base. Use another username or edit the user.', 'error')
                    return redirect(url_for('admin_accounts'))
                if user[7] == user_id_google:
                    flash('Google Chat ID already registered in the Base.', 'error')
                    return redirect(url_for('admin_accounts'))

            aba_usuarios.append_row([None, username, email, permission, password, True, name, user_id_google])
            flash('User successfully added', 'success')
            users = aba_usuarios.get_all_records()
            return render_template('admin_accounts.html', users=users, info_user=info_user)
        if request.method == 'GET':
            userselected = request.args['userSelect_edit']
            username = request.args['username_edit']
            email = request.args['email_edit']
            permission = request.args['permission_edit']
            is_active = 'true' if 'is_active_edit' in request.args and request.args['is_active_edit'] == 'on' else 'false'

            name = request.args['name_edit']
            user_id_google = request.args['userid_edit']
            all_users = aba_usuarios.get_all_values()
            info_user = get_info_user()
            users = aba_usuarios.get_all_records()
            for user in all_users:
                if (user[1] == userselected):
                    aba_usuarios.update_cell(int(user[0])+1, 2, username)
                    aba_usuarios.update_cell(int(user[0])+1, 3, email)
                    aba_usuarios.update_cell(int(user[0])+1, 4, permission)
                    aba_usuarios.update_cell(int(user[0])+1, 6, is_active)
                    aba_usuarios.update_cell(int(user[0])+1, 7, name)
                    aba_usuarios.update_cell(int(user[0])+1, 8, user_id_google)
                    dispositivos = new_dispositivos.get_all_values()
                    for index, disposivo in enumerate(dispositivos):
                        if disposivo[1] == userselected:
                            new_dispositivos.update_cell(index+1, 2, username)
                    auditorias = auditoria.get_all_values()
                    for index, audit in enumerate(auditorias):
                        if audit[2] == userselected:
                            auditoria.update_cell(index+1, 3, username )
                    flash('User Information: '+ username +' successfully updated', 'success')

                    return redirect(url_for('admin_accounts'))
    else:
        flash('Url not allowed for your Profile.', 'error')
        return redirect(url_for('myresources'))