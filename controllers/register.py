from flet_mvc import FletController


class RegisterController(FletController):
    def return_home(self, e):
        """Example route change"""
        self.page.go("/")