from flet_mvc import FletController, alert
import flet as ft
from core.dal import DAL

class RegisterController(FletController):
    def nav_login(self, e):
        # Route change to login view (main)
        self.page.go("/")
    
    def dummy_func(self, e):
        self.alert("ssh-keygen")

    def register_account(self, e=None):
        if(self.model.password() != self.model.confirm_password()):
            self.alert("Passwords do not match", alert.WARNING)
            print(self.model.password(), self.model.confirm_password())
        else:
            isRegistered = DAL.create_user(self.model.firstname(), self.model.lastname(), self.model.username(), self.model.email(), self.model.password(), self.model.gender())
            print(isRegistered)
            self.alert("Registered user '{}' successfully. Please Log-in".format(self.model.firstname()), alert.SUCCESS) if isRegistered else self.alert("FAILED TO REGISTER USER. Please fill up all text fields. Please check if email address is valid.", alert.WARNING)
            
