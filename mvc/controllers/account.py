from flet_mvc import FletController
import flet as ft

class AccountController(FletController):
    def nav_login(self, e):
        # Route change to login view (main)
        self.page.go("/")
    
    def nav_home(self, e):
        self.page.go("/home")
    
    def dummy_func(self, e):
        self.alert("ssh-keygen")