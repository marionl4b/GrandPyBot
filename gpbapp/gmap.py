import requests


class gMapApi:
    
    def __init__(self):
        self.parsed_results = {}
        self.response = {}
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
                    self.response = r.json()
                    self.api_parsed_results()
        else:
            self.error = True

    def api_parsed_results(self):
        if self.response["status"] == "OK":
            self.parsed_results = {
                "address": self.response["results"][0]["formatted_address"],
                "longitude": self.response["results"][0]["geometry"]["location"]["lng"],
                "latitude": self.response["results"][0]["geometry"]["location"]["lat"]
            }
        else:
            self.error = True
