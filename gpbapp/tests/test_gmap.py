import requests
import requests_mock
import pytest

from gpbapp import gmap
GMAP = gmap.gMapApi()


@pytest.fixture()
def exp_params():
    """return a dictionary for request with right params"""
    params = {
        "key": "key",
        "address": "sacré coeur",
        "region": "fr",
        "language": "fr"
    }
    return params


@pytest.fixture()
def exp_parsed_results():
    """return a dictionary of expected parsed json response"""
    parsed_results = {
        "address": "35 Rue du Chevalier de la Barre, 75018 Paris, France",
        "longitude": 2.3431043,
        "latitude": 48.88670459999999,
        "search_term": "Rue du Chevalier de la Barre"
    }
    return parsed_results


class TestGMap:

    def test_request_ok(self, exp_params):
        """should return json dict with status: OK"""
        with requests_mock.Mocker(real_http=True) as m:
            m.get('mock://maps.googleapis.com/maps/api/geocode/json?',
                  headers=exp_params,
                  status_code=200,
                  json={"status": "OK"})
            r_exp = requests.get('mock://maps.googleapis.com/maps/api/geocode/json?').json()
            r = GMAP.get_geocode("sacré coeur")
            assert r_exp["status"] == r["status"]

    def test_valid_parsed_response(self, exp_parsed_results):
        """should return expected dictionary from json response"""
        r = GMAP.get_geocode("sacré coeur")
        parsed_results = GMAP.parse_results(r)
        assert exp_parsed_results == parsed_results

    def test_error_search_term(self):
        """should return an error if json response doesn't match search term crawling key"""
        response = GMAP.get_geocode("tour eiffel")
        result = GMAP.get_search_term(response)
        assert result is None

    def test_empty_address(self, exp_params):
        """should intercept error before sending request"""
        empty = ""
        result =  GMAP.get_geocode(empty)
        assert result is None

    def test_unknown_address(self, exp_params):
        """should return json dict with status: ZERO_RESULTS"""
        exp_params["address"] = "unknown"
        with requests_mock.Mocker(real_http=True) as m:
            m.get('mock://maps.googleapis.com/maps/api/geocode/json?',
                  headers=exp_params,
                  json={"status": "ZERO_RESULTS"})
            r_exp = requests.get('mock://maps.googleapis.com/maps/api/geocode/json?').json()
            r = GMAP.get_geocode("unknown")
            assert r_exp["status"] == r["status"]

    def test_wrong_key(self, exp_params):
        """should return json dict with status: REQUEST_DENIED"""
        exp_params["key"] = "wrong_key"
        GMAP.KEY = "wrong_key"
        with requests_mock.Mocker(real_http=True) as m:
            m.get('mock://maps.googleapis.com/maps/api/geocode/json?',
                  headers=exp_params,
                  json={"status": "REQUEST_DENIED"})
            r_exp = requests.get('mock://maps.googleapis.com/maps/api/geocode/json?').json()
            r = GMAP.get_geocode("sacré coeur")
            assert r_exp["status"] == r["status"]
