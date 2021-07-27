import json

from src.Common.Http import Http


class Login(Http):

    def login_ecshop(self, data, headers):
        self.set_url("/ecshop/user.php")
        self.set_headers(headers)
        self.set_data(json.dumps(data))
        response = self.post()
        return response
