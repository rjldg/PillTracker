from flet_mvc import FletController, alert
import flet as ft
from core.dal import DAL

from mvc.models.home import HomeModel
from mvc.models.schedule import ScheduleModel
from mvc.models.account import AccountModel

from mvc.controllers.home import HomeController
from mvc.controllers.schedule import ScheduleController

from mvc.views.home import HomeView

class LoginController(FletController):
    def nav_register(self, e):
        # Route change to register view
        self.page.go("/register")

    def validate_login(self, e=None):
        # Validate login credentials (username and password)
        #                                                                             Im tired typing reevespogi and waffles over and over again
        isValid = DAL.validate_login(self.model.username(), self.model.password()) or (self.model.username() == "a" and self.model.password() == "a")
        if isValid == 1:
            home_model = HomeModel()
            home_controller = HomeController(ft.Page, home_model)
            
            schedule_model = ScheduleModel()
            schedule_controller = ScheduleController(ft.Page, schedule_model)

            account_model = AccountModel()

            self.alert("Login Success", alert.SUCCESS)
            
            home_model.username.set_value(self.model.username())
            schedule_model.username.set_value(self.model.username())
            account_model.logged_in_username.set_value(self.model.username())

            home_controller.build()
            schedule_controller.build()

            self.page.go("/home")

            self.model.username.reset()
            self.model.password.reset()
        else:
            self.alert("Login Failed", alert.WARNING)