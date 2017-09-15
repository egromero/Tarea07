from flask import Flask, request

app = Flask(__name__)
lista_user = []

url_bot = 'https://api.telegram.org/bot376888244:AAEVNjpM9r-q_6KS2lPbVxC_9EzHSGuv2rE'

@app.route('/', methods=['GET', 'POST'])
def telegram():
    if request.method == 'POST':
        data = request.get_json()
        process_info(data, lista_user)
        print('DATAAAAA', data)



def process_info(data,lista_user):
    print(data)



