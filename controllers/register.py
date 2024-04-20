from flet_mvc import FletController


class RegisterController(FletController):
    def nav_login(self, e):
        # Route change to login view (main)
        self.page.go("/")