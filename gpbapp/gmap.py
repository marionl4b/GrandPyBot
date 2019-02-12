import requests


class gMapApi:
    
    def __init__(self):
        self.error = False
        self.key = "AIzaSyBOl-QtMVnN0TEeRwt6jJAcUqQC0W9_2rU"

    def api_request_constructor(self, parsed_data):
        url = "https://maps.googleapis.com/maps/api/geocode/json?"
        payload = {
            "key": self.key,
            "region": "fr",
            "language": "fr",
            "address": parsed_data
        }
        return url, payload

    def api_get_geocode_request(self, parsed_data):
        if len(parsed_data) != 0:
            url, payload = self.api_request_constructor(parsed_data)
            r = requests.get(url=url, params=payload)
            if r.status_code == 200:
                response = r.json()
                return response
        else:
            self.error = True

    def api_parsed_results(self, response):
        if response["status"] == "OK":
            parsed_results = {
                "address": response["results"][0]["formatted_address"],
                "longitude": response["results"][0]["geometry"]["location"]["lng"],
                "latitude": response["results"][0]["geometry"]["location"]["lat"],
                "search_term": self.api_get_search_term(response)
            }
            return parsed_results
        else:
            self.error = True

    def api_get_search_term(self, response):
        address_comp_dict = response["results"][0]["address_components"][1]
        if address_comp_dict["types"] == ["route"]:
            search_term = address_comp_dict.get("short_name")
            return search_term
        else:
            self.error = True

