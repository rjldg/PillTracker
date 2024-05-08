from flet_mvc import FletModel, data
import flet as ft
from user_controls import *

from mvc.controllers.home import HomeController


class HomeModel(FletModel):
    @data
    def totalconsumption(self):
        return ""
    
    @data
    def username(self):
        return ""
    
    @data
    def home_pillsInfo(self):
        return []
    
    @data
    def home_pillControls(self):
        return []
    