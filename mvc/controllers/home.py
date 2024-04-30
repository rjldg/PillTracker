from flet_mvc import FletController
import flet as ft

class HomeController(FletController):
    def nav_schedule(self, e):
        # Route change to login view (main)
        self.page.go("/schedule")
    
    def dummy_func(self, e):
        self.alert("ssh-keygen")