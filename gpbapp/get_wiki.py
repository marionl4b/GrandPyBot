from wikipedia import set_lang, page, summary
from wikipedia.exceptions import DisambiguationError, PageError


class GetWiki:
    """run GET request for the wikipedia API with python wrapper
    GIVEN: search term form gmap api prev request
    THEN: return a dictionary with wikipedia data results for page sumary and page link
    WHEN: search term retrieve a correct page subject"""
    def __init__(self):
        set_lang("fr")

    def get_summary(self, data):
        try:
            return summary(data)
        except (PageError, DisambiguationError):
            return None

    def get_url(self, data):
        r = page(data)
        url = r.url
        return url

    def prepare_data(self, data):
        if data:
            s = self.get_summary(data)
            url = self.get_url(data)
            parsed_results = {
                "summary": s,
                "url": url
            }
            return parsed_results
        else:
            return None
