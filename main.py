from flask import Flask, request
import requests

app = Flask(__name__)
lista_user = []

url_bot = 'https://api.telegram.org/bot376888244:AAEVNjpM9r-q_6KS2lPbVxC_9EzHSGuv2rE'

@app.route('/telegram', methods=['POST'])
def telegram():
    if request.method == 'POST':
        data = request.get_json()
        process_info(data, lista_user)


def process_info(data,lista):
    chat_id = data['message']['chat']['id']
    if not chat_id in lista:
        lista.append(chat_id)
    if 'entities' in data['message'].keys():
        command = data['message']['text']
        command = command.split(' ')
        if command[0]== '/start':
            response = 'Bienvenido a PointerBot'
            requests.post(url_bot + '/sendMessage',
                          data={'chat_id': chat_id, 'text': response})
        if command[0]== '/info':
            response = 'información aquí'
            requests.post(url_bot + '/sendMessage',
                          data={'chat_id': chat_id, 'text': response})






