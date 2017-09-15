from flask import Flask, request

app = Flask(__name__)
lista_user = []

tokenbot = '376888244:AAEVNjpM9r-q_6KS2lPbVxC_9EzHSGuv2rE'
url_bot = 'https://api.telegram.org/bot' + tokenbot

@app.route('/telegram', methods=['GET', 'POST'])
def telegram():
    if request.method == 'POST':
        data = request.get_json()
        process_info(data, lista_user)
        chat_id = data['message']['chat']['id']
        print(chat_id)
    pass



def process_info(data,lista_user):
    print(data)

    

