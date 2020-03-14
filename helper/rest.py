from support.testdata import TestData as TD


def req():
    return Builder()


class Builder:
    def status(self):
        return self

    def get(self):
        return self

    def post(self):
        return