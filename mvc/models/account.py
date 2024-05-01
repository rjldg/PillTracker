from flet_mvc import FletModel, data
import flet as ft


class AccountModel(FletModel):
    @data
    def dummy(self):
        return ""