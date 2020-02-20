class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self):
        wd = self.app.wd
        self.app.open_home_page()