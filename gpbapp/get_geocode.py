import requests
from gpbapp import settings


class GetGeocode:
    """run GET request for google map API with geocode
    GIVEN: parsed location term
    THEN: return a dictionary with address, longitude, latitude and search_term
    in order to display a javascript google map in frontend and requesting wikipedia API
    WHEN: parameters of the request are correct and result for search term valid"""

    KEY = settings.KEY

    def api_request_constructor(self, parsed_data):
        url = "https://maps.googleapis.com/maps/api/geocode/json?"
        payload = {
            "key": self.KEY,
            "region": "fr",
            "language": "fr",
            "address": parsed_data
        }
        return url, payload

    def get_geocode(self, parsed_data):
        if len(parsed_data) != 0:
            url, payload = self.api_request_constructor(parsed_data)
            r = requests.get(url=url, params=payload)
            if r.status_code == 200:
                response = r.json()
                return response
        return None

    def parse_results(self, response):
        if response["status"] == "OK":
            parsed_results = {
                "address": response["results"][0]["formatted_address"],
                "longitude": response["results"][0]["geometry"]["location"]["lng"],
                "latitude": response["results"][0]["geometry"]["location"]["lat"],
                "search_term": self.get_search_term(response)
            }
            return parsed_results
        else:
            return None

    def get_search_term(self, response):
        address_comp_dict = response["results"][0]["address_components"][1]
        if address_comp_dict["types"] == ["route"]:
            search_term = address_comp_dict.get("short_name")
            return search_term
        else:
            return None
