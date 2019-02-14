from gpbapp import parser


class TestParser:
    PARSER = parser.Parser()

    def test_empty_message(self):
        parsed_message = self.PARSER.parse_usermsg({"userMessage": ""})
        assert parsed_message is None

    def test_stopwords(self):
        parsed_message = self.PARSER.parse_usermsg({"userMessage": "zut, alors !"})
        assert parsed_message is None

    def test_valid_location(self):
        parsed_message = self.PARSER.parse_usermsg({"userMessage": "Salut GrandPy ! "
                                                                   "Est-ce que tu connais "
                                                                   "l'adresse d'OpenClassrooms"})
        assert parsed_message == ["openclassrooms"]

    def test_punctuation(self):
        parsed_message = self.PARSER.parse_usermsg({"userMessage": ": ; !+"})
        assert parsed_message is None
