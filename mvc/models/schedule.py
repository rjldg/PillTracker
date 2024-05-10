from flet_mvc import FletModel, data
import flet as ft
from user_controls import *

from mvc.controllers.schedule import ScheduleController



class ScheduleModel(FletModel):

    @data
    def username(self):
        return ""
    @data
    def pill_name(self):
        return ""
    
    @data
    def pill_total_amt(self):
        return ""
    
    @data
    def pill_daily_intake(self):
        return ""
    
    @data
    def sched_pillsInfo(self):
        return []
    
    @data
    def sched_pillControls(self):
        return []

    @data
    def create_view_overlay(self):
        return createsched_view.OverlayPanel(
            toggle=None, 
            visible=False,
            opacity=0,
            ref=self,
        )
    
    @data
    def create_view(self):
        schedule_controller = ScheduleController(ft.Page, self)
        return createsched_view.Panel(
            model_pillname=self.pill_name, 
            model_pilltotal=self.pill_total_amt, 
            model_dailyintake=self.pill_daily_intake,
            controller=schedule_controller,
            toggle=None,
            offset=ft.transform.Offset(-1,0),
            ref=self,
        )
