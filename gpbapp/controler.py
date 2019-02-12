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
    data = request.json
    parser.parse_usermsg(data)
    gmap_r = gmap.api_get_geocode_request(parser.parsed_message)
    gmap_parsed_results = gmap.api_parsed_results(gmap_r)
    wiki_parsed_results = wiki.dict_results_constructor(gmap_parsed_results.get("search_term"))
    if parser.error or gmap.error or wiki.error:
        return jsonify({"usr_location": "error"})
    else:
        return jsonify({"usr_location": "ok",
                        "gmap": gmap_parsed_results,
                        "wiki": wiki_parsed_results})
