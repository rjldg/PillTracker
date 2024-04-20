from flet_mvc import FletController


class LoginController(FletController):
    def nav_register(self, e):
        """Example route change"""
        self.page.go("/register")
