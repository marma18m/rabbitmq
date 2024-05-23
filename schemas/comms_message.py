import json


class CommsMessageJSON:
    def __init__(self):
        self.message = {
            "timestamp": None,
            "tag": None,
            "value": None,
        }

    def set_timestamp(self, timestamp):
        self.message["timestamp"] = timestamp

    def set_tag(self, tag):
        self.message["tag"] = tag

    def set_value(self, value):
        self.message["value"] = value

    def get_message(self):
        return self.message

    def parse_from_string(self, string):
        self.message = json.loads(string)
