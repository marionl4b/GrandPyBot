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
        else:
            self.error = True

    def parse_usermsg(self, data):
        self.check_usermsg(data)
        message = self.message.lower()
        message = list(re.findall(r"\w+", message))
        with open(self.stopwords_file) as f:
            data = json.load(f)
        stopwords = list(data)
        self.parsed_message = [x for x in message if x not in stopwords]
        self.result()

    def result(self):
        if len(self.parsed_message) != 0:
            self.error = False
        else:
            self.error = True
