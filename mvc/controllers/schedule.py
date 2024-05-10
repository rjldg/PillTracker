from flet_mvc import FletController, alert
import flet as ft

from user_controls import *
from core.dal import DAL

from mvc.models.home import HomeModel
from mvc.controllers.home import HomeController

class ScheduleController(FletController):
    is_create = False
    def in_create(self, create_view, create_view_overlay, control):
        self.is_create = not self.is_create # toggle
        print(create_view, create_view_overlay)
        if self.is_create:
            create_view_overlay.visible = True
            create_view.offset = ft.transform.Offset(0,0)
            create_view_overlay.opacity = 0.3
        else:
            create_view.offset = ft.transform.Offset(-1,0)
            create_view_overlay.opacity = 0
            create_view_overlay.visible = False
        control.update()
    
    def build(self):
        self.model.sched_pillsInfo.reset()
        self.model.sched_pillControls.reset()

        self.model.sched_pillsInfo.set_value(DAL.read_pills_schedule_page(self.model.username.value))
        self.model.sched_pillsInfo.set_value(sorted(self.model.sched_pillsInfo.value, key=lambda x: x[0]))

        self.model.sched_pillControls.set_value([
            pt_schedule.Control(medname=pill[0], dailyintake=pill[1], totalpills=pill[2], pill_id=pill[3], controller=self, panel=self.model.create_view, paneloverlay=self.model.create_view_overlay)
            for pill in self.model.sched_pillsInfo.value
        ])

    def build_and_update(self):
        self.model.sched_pillsInfo.reset()
        self.model.sched_pillControls.reset()

        self.model.sched_pillsInfo.set_value(DAL.read_pills_schedule_page(self.model.username.value))
        self.model.sched_pillsInfo.set_value(sorted(self.model.sched_pillsInfo.value, key=lambda x: x[0]))

        self.model.sched_pillControls.set_value([
            pt_schedule.Control(medname=pill[0], dailyintake=pill[1], totalpills=pill[2], pill_id=pill[3], controller=self, panel=self.model.create_view, paneloverlay=self.model.create_view_overlay)
            for pill in self.model.sched_pillsInfo.value
        ])

        self.page.update()


    def create_new_pill(self, e=None):
        if(self.model.pill_total_amt == 0 or self.model.pill_daily_intake == 0):
            self.alert("Pill Total Amount or Pill Daily Intake cannot be null or zero.", alert.WARNING)
            return -1
        else:
            isPillCreated = DAL.create_pill(self.model.username(), self.model.pill_name(), self.model.pill_total_amt(), self.model.pill_daily_intake())
            print(isPillCreated)
            if isPillCreated is True:
                self.alert("Pill '{}' successfully.".format(self.model.pill_name()), alert.SUCCESS)

                self.build()
                self.build_home()
                self.reload()

                self.model.pill_name.reset()
                self.model.pill_total_amt.reset()
                self.model.pill_daily_intake.reset()
                return 1
            else: 
                self.alert("FAILED TO CREATE PILL. Please fill up all text fields. Ensure none of the fields are null or zero.", alert.WARNING)
                return -1
        
    def delete_pill(self, control):
        isDeleted = DAL.delete_pill(control.pill_id)

        self.alert(f"Deleted {control.medname} successfully.", alert.SUCCESS) if isDeleted else self.alert(f"Failed to delete {control.medname}.", alert.WARNING)

        self.build_and_update()
        self.build_home()

    def build_home(self):
        home_model = HomeModel()
        home_controller = HomeController(ft.Page, home_model)
        home_controller.build()

    def reload(self):
        self.page.update()
    
    def nav_schedule(self, e):
        self.page.go("/schedule")
    
    def nav_home(self, e):
        self.page.go("/home")
    
    def nav_account(self, e):
        self.page.go("/account")
    
    def dummy_func(self, e):
        self.alert("ssh-keygen")
    