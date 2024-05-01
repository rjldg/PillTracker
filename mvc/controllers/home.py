from flet_mvc import FletController
import flet as ft

class HomeController(FletController):
    def nav_schedule(self, e):
        self.page.go("/schedule")
    
    def nav_home(self, e):
        self.page.go("/home")
    
    def nav_account(self, e):
        self.page.go("/account")
    
    def dummy_func(self, e):
        self.alert("ssh-keygen")