import json

from src.Common.Http import Http


class Message(Http):

    def post_message(self,data,headers):
        self.set_url("/ecshop/message.php")
        self.set_headers(headers)
        self.set_data(json.dumps(data))
        response = self.post()
        return response
