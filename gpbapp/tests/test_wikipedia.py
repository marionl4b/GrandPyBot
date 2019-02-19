import pytest
import wikipedia
from gpbapp import wiki_api


@pytest.fixture()
def exp_results():
    """return expected data from wikipedia request wrapper"""
    exp_results = {
        "url": "https://fr.wikipedia.org/wiki/Rue_du_Chevalier-de-La-Barre",
        "summary": "La rue du Chevalier-de-La-Barre est une rue de la butte Montmartre à Paris, "
                   "dans le 18e arrondissement."
    }
    return exp_results


class TestWikipedia:
    WIKI = wiki_api.WikipediaCalls()

    def test_results(self, exp_results):
        """should retrieve expected data in a dictionary"""
        parsed_results = self.WIKI.prepare_data("Rue du Chevalier de la Barre")
        assert exp_results == parsed_results

    def test_empty_data(self):
        """should intercept error before sending request"""
        empty = ""
        result = self.WIKI.prepare_data(empty)
        assert result is None

    def test_page_error(self):
        """error with search term matching no wikipedia page title"""
        wrong_data = "fjkqshli"
        with pytest.raises(wikipedia.exceptions.PageError):
            self.WIKI.prepare_data(wrong_data)

    def test_disambiguation_error(self):
        """error with search term matching too many page title"""
        with pytest.raises(wikipedia.exceptions.DisambiguationError):
            self.WIKI.prepare_data("blabla")
