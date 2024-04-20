from flet_mvc import FletController


class LoginController(FletController):
    def navigate_secundary(self, e):
        """Example route change"""
        self.page.go("/register")
