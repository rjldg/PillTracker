from flet_mvc import FletModel, data
import flet as ft


class LoginModel(FletModel):
    @data
    def username(self):
        return ""
    
    @data
    def password(self):
        return ""
