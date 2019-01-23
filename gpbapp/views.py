from flask import render_template, jsonify, request
from gpbapp import app, parser

parser = parser.Parser()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/index', methods=['POST'])
def user_message():
    data = request.json
    parser.check_usermsg(data)
    if parser.error:
        return jsonify({"parser": "error"})
    else:
        return jsonify({"parser": "ok"})
