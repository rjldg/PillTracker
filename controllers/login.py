from flet_mvc import FletController, alert
import flet as ft
from core.dal import DAL

dal = DAL()

class LoginController(FletController):
    def nav_register(self, e):
        # Route change to register view
        self.page.go("/register")

    def validate_login(self, e=None):
        # Validate login credentials (username and password)
        isValid = DAL.validate_login(self.model.username(), self.model.password())

        if isValid == 1:
            self.alert("Login Success", alert.SUCCESS)
        else:
            self.alert("Login Failed", alert.WARNING)