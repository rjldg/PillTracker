from flet_mvc import FletController
import flet as ft

class RegisterController(FletController):
    def nav_login(self, e):
        # Route change to login view (main)
        self.page.go("/")
    
    def dummy_func(self, e):
        self.alert("ssh-keygen")