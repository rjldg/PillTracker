from flet_mvc import FletController, alert
import flet as ft

class RegisterController(FletController):
    def enter(self, e=None):
        self.model.first_name.set_value(self.model.first_name)
        self.model.first_name.reset()

        self.update()