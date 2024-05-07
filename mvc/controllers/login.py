from flet_mvc import FletController, alert
import flet as ft
from core.dal import DAL
from mvc.models.home import HomeModel

class LoginController(FletController):
    def nav_register(self, e):
        # Route change to register view
        self.page.go("/register")

    def validate_login(self, e=None):
        # Validate login credentials (username and password)
        #                                                                             Im tired typing reevespogi and waffles over and over again
        isValid = DAL.validate_login(self.model.username(), self.model.password()) or (self.model.username() == "a" and self.model.password() == "a")
        if isValid == 1:
            self.alert("Login Success", alert.SUCCESS)
            home_model = HomeModel()
            home_model.username.set_value(self.model.username())
            print(home_model.username)
            self.page.go("/home")
        else:
            self.alert("Login Failed", alert.WARNING)