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
                return parsed_message
        return None
