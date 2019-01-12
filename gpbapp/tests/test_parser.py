from flask_testing import LiveServerTestCase
from gpbapp import app


class TestUserTakesTheTest(LiveServerTestCase):

    def create_app(self):

        # use special conftest file.
        app.config.from_object('fbapp.tests.conftest')
        return app


class TestParser:
    pass
    # Parser
    # test views index.html
    # test input value is not empty
    # test input value is correct and ready to parse
    # test parse result is correct
