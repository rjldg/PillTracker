from flet_mvc import FletModel, data
import flet as ft


class ScheduleModel(FletModel):
    @data
    def dummy(self):
        return ""
    
    @data
    def username(self):
        return ""