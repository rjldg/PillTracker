from flet_mvc import FletModel, data
import flet as ft


class AccountModel(FletModel):
    @data
    def example_title(self):
        return "This is the account view!"
    
    @data
    def firstname(self):
        return ""
    
    @data
    def lastname(self):
        return ""
    
    @data
    def username(self):
        return ""
    
    @data
    def email(self):
        return ""
    
    @data
    def gender(self):
        return ""
    
    @data
    def password(self):
        return ""
    
    @data
    def confirm_password(self):
        return ""
    
    @data
    def logged_in_username(self):
        return ""