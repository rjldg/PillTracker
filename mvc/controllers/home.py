from flet_mvc import FletController, alert
import flet as ft

from core.dal import DAL
from user_controls import *
from datetime import datetime

class HomeController(FletController):

    def build(self):
        self.model.home_pillsInfo.reset()
        self.model.home_pillControls.reset()

        self.model.home_pillsInfo.set_value(DAL.read_pills_home_page(self.model.username.value))
        self.model.home_pillsInfo.set_value(sorted(self.model.home_pillsInfo.value, key=lambda x: x[0]))

        self.model.home_pillControls.set_value([
            pt_pilltaken.Control(medname=pill[0], defaultvalue=pill[1], pill_id=pill[2], controller=self)
            for pill in self.model.home_pillsInfo.value
        ])

    def increment_pills_taken(self, control):
        new_value = DAL.increment_pills_taken(control.pill_id, datetime.today().strftime("%Y-%m-%d"))

        print("New_Value: ", new_value)
        control.defaultvalue = new_value

        self.build()    # Refresh the list of pilltaken controls

    def decrement_pills_taken(self, control):
        new_value = DAL.decrement_pills_taken(control.pill_id, datetime.today().strftime("%Y-%m-%d"))

        print("New_Value: ", new_value)
        control.defaultvalue = new_value

        self.build()    # Refresh the list of pilltaken controls

    def nav_schedule(self, e):
        self.page.go("/schedule")
    
    def nav_home(self, e):
        self.page.go("/home")
    
    def nav_account(self, e):
        self.page.go("/account")
    
    def dummy_func(self, e):
        self.alert("ssh-keygen")