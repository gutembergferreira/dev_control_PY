import requests

def sendMessageWebhook(user_one, user_two, action, device=None, accessorie=None, simcard=None):
    try:
        ## WEBHOOK DE PRODUÇÃO
        url_webhook = "https://chat.googleapis.com/v1/spaces/AAAA0DJtNoU/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=YVn-fwD5B3IIkeQu4UfSNcsEHJW04fBBAUtNW8MifgU"
        ## WEBHOOK DE TESTE
        #url_webhook = "https://chat.googleapis.com/v1/spaces/AAAAci2yLXI/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=pgSZlYiwlz_NPC7Q66o64RV8zCM9rq8mv1-6GgTKB3I"
        if (action == 'Loan'):
            if (device):
                msg = f"<users/{user_one}> realizou o Empréstimo do dispositivo {device}."
                payload = {"text": msg}
                response = requests.post(url_webhook, json=payload)
                response.raise_for_status()
                print("Mensagem enviada com sucesso!")
            if (accessorie):
                msg = f"<users/{user_one}> realizou o Empréstimo do acessório {accessorie}."
                payload = {"text": msg}
                response = requests.post(url_webhook, json=payload)
                response.raise_for_status()
                print("Mensagem enviada com sucesso!")         
            if (simcard):
                msg = f"<users/{user_one}> realizou o Empréstimo do SIM Card {simcard}."
                payload = {"text": msg}
                response = requests.post(url_webhook, json=payload)
                response.raise_for_status()
                print("Mensagem enviada com sucesso!")     

        if (action == 'Devolution'):
            if (device):
                msg = f"<users/{user_one}> realizou a Devolução do dispositivo {device}."
                payload = {"text": msg}
                response = requests.post(url_webhook, json=payload)
            if (accessorie):
                msg = f"<users/{user_one}> realizou a Devolução do acessório {accessorie}."
                payload = {"text": msg}
                response = requests.post(url_webhook, json=payload)
            if (simcard):
                msg = f"<users/{user_one}> realizou a Devolução do SIM Card {simcard}."
                payload = {"text": msg}
                response = requests.post(url_webhook, json=payload)

        if (action == 'Transfer'):
            if (device):
                if (user_two != ''):
                    msg = f"<users/{user_one}> realizou a Transferência do dispositivo {device} para o usuário <users/{user_two}>"
                    payload = {"text": msg}
                    response = requests.post(url_webhook, json=payload)
                    response.raise_for_status()
                    print("Mensagem enviada com sucesso!")
            if (accessorie):
                if (user_two != ''):
                    msg = f"<users/{user_one}> realizou a Transferência do acessório {accessorie} para o usuário <users/{user_two}>"
                    payload = {"text": msg}
                    response = requests.post(url_webhook, json=payload)
                    response.raise_for_status()
                print("Mensagem enviada com sucesso!")
            if (simcard):
                if (user_two != ''):
                    msg = f"<users/{user_one}> realizou a Transferência do SIM Card {simcard} para o usuário <users/{user_two}>"
                    payload = {"text": msg}
                    response = requests.post(url_webhook, json=payload)
                    response.raise_for_status()
                    print("Mensagem enviada com sucesso!")
    except requests.exceptions.RequestException as e:
        print("Erro ao enviar a mensagem para o webhook:", e)
    except Exception as e:
        print("Erro inesperado:", e)