import json
import os
import re

from gpbapp import app


class Parser:
    """Run a parser after checking user post prompt is not empty
    Then lower user message, remove punctuation and stopwords
    finally return parsed location for gmap api"""
    def __init__(self):
        self.stopwords_file = os.path.join(app.static_folder, 'stopwords.json')
        self.error = False

    def check_usermsg(self, prompt):
        json_data = json.dumps(prompt)
        message = json.loads(json_data)
        if message.get("userMessage") != "":
            checked_msg = "{}".format(message.get("userMessage"))
            return checked_msg
        else:
            return None

    def parse_usermsg(self, prompt):
        parse_msg = self.check_usermsg(prompt)
        if parse_msg:
            parse_msg = parse_msg.lower()
            parse_msg = list(re.findall(r"\w+", parse_msg))
            with open(self.stopwords_file) as f:
                data = json.load(f)
            stopwords = list(data)
            parsed_message = [x for x in parse_msg if x not in stopwords]
            if len(parsed_message) != 0:
                parsed_message = " ".join(parsed_message)
                return parsed_message
        return None
