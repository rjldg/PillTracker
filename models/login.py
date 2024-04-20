from flet_mvc import FletModel, data
import flet as ft


class LoginModel(FletModel):
    @data
    def app_title(self):
        return "PillTracker"
