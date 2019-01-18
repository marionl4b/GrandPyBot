import pytest
from gpbapp import app


class TestViews:

    @pytest.fixture
    def client(self):
        app.testing = True
        test_client = app.test_client()
        return test_client

    def test_home_page(self, client):
        """ test valid server response for index page """
        res = client.get('/')
        assert res.status_code == 200

