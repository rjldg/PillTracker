from flet_mvc import FletController, alert
import flet as ft
from core.dal import DAL

class LoginController(FletController):
    def nav_register(self, e):
        # Route change to register view
        self.page.go("/register")