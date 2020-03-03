from support import config


class TestData:

    def murl(self):
        return config.get("murl")

    def url(self):
        return config.get("url")

    def username_(self):
        return config.get("username")

    def password_(self):
        return config.get("password")

    def headers(self):
        return {"Content-Type": "application/json"}
