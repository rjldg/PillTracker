from flet_mvc import FletController, alert
import flet as ft

class LoginController(FletController):
    def nav_register(self, e):
        # Route change to register view
        self.page.go("/register")
    
    # implement validate_login() here
