from flask import render_template, request, json
from gpbapp import app


@app.route('/')
def index():
    return render_template('index.html', title='Home')


@app.route('/index', methods=['POST'])
def user_message():
    usermsg = request.form['usermsg']

    # validate the received values
    if usermsg:
        return json.dumps({'status': 'OK', 'user message': usermsg})
    else:
        return json.dumps({'message': 'error'})
