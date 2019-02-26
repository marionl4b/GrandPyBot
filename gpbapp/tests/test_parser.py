from gpbapp import parser


class TestParser:
    PARSER = parser.Parser()

    def test_empty_message(self):
        """should return none if user prompt is empty"""
        parsed_message = self.PARSER.parse_usermsg({"userMessage": ""})
        assert parsed_message is None

    def test_stopwords(self):
        """should return none if all words of user message in stopwords list"""
        parsed_message = self.PARSER.parse_usermsg({"userMessage": "zut, alors !"})
        assert parsed_message is None

    def test_valid_location(self):
        """should retrieve expected location after parsing"""
        parsed_message = self.PARSER.parse_usermsg({"userMessage": "Salut GrandPy ! "
                                                                   "Est-ce que tu connais "
                                                                   "l'adresse d'OpenClassrooms"})
        assert parsed_message == "openclassrooms"

    def test_punctuation(self):
        """should return none if all char are punctuation"""
        parsed_message = self.PARSER.parse_usermsg({"userMessage": ": ; !+"})
        assert parsed_message is None
