from flet_mvc import FletController


class RegisterController(FletController):
    def nav_login(self, e):
        """Example route change"""
        self.page.go("/")