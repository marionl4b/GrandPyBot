import pytest
from flask import json
from gpbapp import app


class TestViews:

    @pytest.fixture
    def test_client(self):
        """ reproduce the gpbapp with client for testing"""
        app.testing = True
        client = app.test_client()
        return client

    def test_home_page(self, test_client):
        """ test valid server response for home page """
        res = test_client.get('/')
        assert res.status_code == 200

    def test_index_page(self, test_client):
        """ test valid server response for index page """
        res = test_client.get('/index')
        assert res.status_code == 200

    def test_json(self, test_client):
        """ test valid server response for post request in /index in json format """
        res = test_client.post("/index",
                               data=json.dumps({"userMessage": "test"}),
                               content_type='application/json')
        assert res.status_code == 200
