from flet_mvc import FletController, alert
import flet as ft
from core.dal import DAL

class AccountController(FletController):

    def update_user_information(self, e):
        if(self.model.password() != self.model.confirm_password()):
            self.alert("Passwords do not match", alert.WARNING)
        else:
            isUpdated, isUsernameChanged, isPasswordChanged = DAL.update_user(self.model.logged_in_username() ,self.model.firstname(), self.model.lastname(), self.model.username(), self.model.email(), self.model.password(), self.model.gender())
            
            if(isUsernameChanged or isPasswordChanged):
                self.alert("Username or password was changed. Please log-in again.", alert.INFO)
                self.page.go("/")
            else:
                self.alert("Updated user information successfully.".format(self.model.logged_in_username()), alert.SUCCESS) if isUpdated else self.alert("FAILED TO UPDATE USER INFORMATION. Please fill up all text fields. Please check if email address is valid.", alert.WARNING)

    def nav_login(self, e):
        # Route change to login view (main)
        self.page.go("/")
    
    def nav_home(self, e):
        self.page.go("/home")
    
    def dummy_func(self, e):
        self.alert("ssh-keygen")