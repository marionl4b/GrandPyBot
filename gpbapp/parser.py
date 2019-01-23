import re
import os
import json

from gpbapp import app


class Parser:
    def __init__(self):
        self.message = ""
        self.stopwords_file = os.path.join(app.static_folder, 'stopwords.json')
        self.parsed_message = ""
        self.error = False

    def check_usermsg(self, data):
        json_data = json.dumps(data)
        message = json.loads(json_data)
        if message.get("userMessage") != "":
            self.message = message.get("userMessage")
            self.stopwords()
        else:
            self.error = True

    def stopwords(self):
        message = self.message.lower()
        ready_to_parse = list(re.findall(r"\w+", message))
        with open(self.stopwords_file) as f:
            data = json.load(f)
        stopwords = list(data)
        self.parsed_message = [x for x in ready_to_parse if x not in stopwords]
        self.error_message()

    def error_message(self):
        message = self.parsed_message
        if len(message) != 0:
            self.error = False
        else:
            self.error = True
