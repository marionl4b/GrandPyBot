from flask import render_template, jsonify, request
from gpbapp import app, parser, gmap

parser = parser.Parser()
gmap = gmap.gMapApi()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/index', methods=['POST'])
def user_message():
    data = request.json
    parser.parse_usermsg(data)
    if parser.error:
        return jsonify({"usr_location": "error"})
    else:
        gmap.api_get_geocode_request(parser.parsed_message)
        if gmap.error:
            return jsonify({"usr_location": "error"})
        else:
            return jsonify({"usr_location": "ok", "gmap": gmap.parsed_results})
