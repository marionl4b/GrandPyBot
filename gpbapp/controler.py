from flask import render_template, jsonify, request
from gpbapp import app, parser, get_geocode, get_wiki

parser = parser.Parser()
gmap = get_geocode.GetGeocode()
wiki = get_wiki.GetWiki()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/index', methods=['POST'])
def user_message():
    """
    run the process of parsing user message and post location and wikipedia data to display
    for frontend in json format
    GIVEN : user prompt in json format
    THEN : return a dictionary with user location status, gmap api results and wikipedia api results
    WHEN : each step of the process return is not None
    """
    def process_parser(data):
        parsed_msg = parser.parse_usermsg(data)
        if parsed_msg is None:
            return jsonify({"usr_location": "error"})
        else:
            return process_gmap(parsed_msg)

    def process_gmap(parsed_msg):
        gmap_r = gmap.get_geocode(parsed_msg)
        if gmap_r is None:
            return jsonify({"usr_location": "error"})
        gmap_results = gmap.parse_results(gmap_r)
        if gmap_results is None:
            return jsonify({"usr_location": "error"})
        else:
            return process_wiki(gmap_results)

    def process_wiki(gmap_results):
        wiki_results = wiki.prepare_data(gmap_results.get("search_term"))
        if wiki_results is None:
            return jsonify({"usr_location": "error"})
        else:
            return jsonify({"usr_location": "ok", "gmap": gmap_results, "wiki": wiki_results})

    usr_data = request.json
    return process_parser(usr_data)
