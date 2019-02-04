from gpbapp import gmap


class TestGMap:

        GMAP = gmap.gMapApi()
        EXP_RES = {
            "formatted_address": "Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France",
            "longitude": 2.2944813,
            "latitude": 48.85837009999999
        }
        EXP_STATUS = ["OK", "INVALID_REQUEST", "REQUEST_DENIED", "ZERO_RESULTS"]

        def test_gmap_api_server_response(self):
            """test if google map geocode API response is valid"""
            self.GMAP.api_get_geocode_request("Tour Eiffel")
            assert self.EXP_STATUS[0] == self.GMAP.response["status"]

        def test_gmap_api_data_retrieved(self):
            """test if google map geocode API parsed response contains expected data"""
            self.GMAP.api_get_geocode_request("Tour Eiffel")
            assert self.EXP_RES["formatted_address"] == self.GMAP.parsed_results["formatted_address"]

        def test_gmap_api_empty_address(self):
            """test google map API with empty address parameter """
            empty = ""
            self.GMAP.api_get_geocode_request(empty)
            assert self.GMAP.error

        def test_gmap_api_unknown_address(self):
            """test google map API with wrong address parameter """
            self.GMAP.api_get_geocode_request("unknown_address")
            assert self.EXP_STATUS[3] == self.GMAP.response["status"]

        def test_gmap_api_bad_key(self):
            """test wrong google map API key """
            self.GMAP.key = "wrongkey"
            self.GMAP.api_get_geocode_request("Tour Eiffel")
            assert self.EXP_STATUS[2] == self.GMAP.response["status"]
