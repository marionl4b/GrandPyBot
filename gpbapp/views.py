from flask import render_template, jsonify
from gpbapp import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/index', methods=['POST'])
def user_message():
    return jsonify({"status": "ok"})
