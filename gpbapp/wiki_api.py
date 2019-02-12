import wikipedia


class WikipediaCalls:
    def __init__(self):
        wikipedia.set_lang("fr")
        self.error = False

    def get_summary(self, data):
        try:
            summary = wikipedia.summary(data)
            return summary
        except wikipedia.exceptions.PageError:
            self.error = True
        except wikipedia.exceptions.DisambiguationError:
            self.error = True

    def get_url(self, data):
        r = wikipedia.page(data)
        url = r.url
        return url

    def dict_results_constructor(self, data):
        if len(data) != 0:
            summary = self.get_summary(data)
            url = self.get_url(data)
            parsed_results = {
                "summary": summary,
                "url": url
            }
            return parsed_results
        else:
            self.error = True
