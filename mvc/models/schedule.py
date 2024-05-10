from flet_mvc import FletModel, data
import flet as ft


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
