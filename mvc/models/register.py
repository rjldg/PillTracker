from flet_mvc import FletModel, data
import flet as ft


class RegisterModel(FletModel):
    @data
    def example_title(self):
        return "This is the register view!"
