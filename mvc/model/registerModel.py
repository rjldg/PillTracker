import flet as ft
from flet_mvc import data, FletModel

# Model for PillTracker's Register Page

class RegisterModel(FletModel):
    @data
    def first_name(self):
        return ""
    
    @data
    def last_name(self):
        return ""
    
    @data
    def username(self):
        return ""
    
    @data
    def email(self):
        return ""
    
    @data
    def password(self):
        return ""
    
    @data
    def gender(self):
        return ""