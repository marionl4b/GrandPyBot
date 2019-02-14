from flask import render_template, jsonify, request
from gpbapp import app, parser, gmap, wiki_api

parser = parser.Parser()
gmap = gmap.gMapApi()
wiki = wiki_api.WikipediaCalls()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/index', methods=['POST'])
def user_message():
    def process_wiki(gmap_results):
        wiki_results = wiki.prepare_data(gmap_results.get("search_term"))
        if wiki_results is None:
            return jsonify({"usr_location": "error"})
        else:
            return jsonify({"usr_location": "ok", "gmap": gmap_results, "wiki": wiki_results})

    data = request.json
    parsed_msg = parser.parse_usermsg(data)

    if parsed_msg is None:
        return jsonify({"usr_location": "error"})
    else:
        gmap_r = gmap.get_geocode(parsed_msg)
        if gmap_r is None:
            return jsonify({"usr_location": "error"})

        gmap_results = gmap.parse_results(gmap_r)
        if gmap_results is None:
            return jsonify({"usr_location": "error"})
        else:
            return process_wiki(gmap_results)
