from flask import Flask, request
import requests

app = Flask(__name__)
respuesta = []

url_bot = 'https://api.telegram.org/bot376888244:' \
          'AAEVNjpM9r-q_6KS2lPbVxC_9EzHSGuv2rE'


@app.route('/telegram', methods=['POST'])
def telegram():
    respuesta1 = 'Debes indicarme cuando será la reunión ' \
                 'y una breve descripción.'
    if request.method == 'POST':
        data = request.get_json()
        if 'reply_to_message' in data['message'].keys() and \
                data['message']['reply_to_message']['text'] == respuesta1:
            respuesta.append('**'+data['message']['text']+'**')
            chat_id = data['message']['chat']['id']
            requests.post(url_bot + '/sendMessage',
                          data={'chat_id': chat_id, 'text': 'Para agregar un punto, '
                                                            'debes usar /punto'})

        process_info(data,respuesta1,respuesta)

    return 'ok'

def process_info(data,respuesta1, respuesta):
    chat_id = data['message']['chat']['id']
    if 'entities' in data['message'].keys():
        command = data['message']['text']
        command = command.split(' ')
        if command[0]== '/nuevareu':
            requests.post(url_bot + '/sendMessage',
                          data={'chat_id': chat_id, 'text': respuesta1})
        if command[0]== '/info':
            response = 'información aquí:\n ' \
                       'bla bla bla'
            requests.post(url_bot + '/sendMessage',
                          data={'chat_id': chat_id, 'text': response})
        if command[0]== '/punto':
            punto = ' '.join(command[1::])
            respuesta.append(punto)
            response = 'Punto agregado {} 👌🏾'.format(data['message']['from']['first_name'])
            requests.post(url_bot + '/sendMessage',
                          data={'chat_id': chat_id, 'text': response})
        if command[0] == '/done':
            response = ' '.join(respuesta)
            requests.post(url_bot + '/sendMessage',
                          data={'chat_id': chat_id, 'text': response})











