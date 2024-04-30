from flet_mvc import FletModel, data
import flet as ft


class HomeModel(FletModel):
    @data
    def totalconsumption(self):
        return ""