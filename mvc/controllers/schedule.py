from flet_mvc import FletController, alert
import flet as ft

from user_controls import *
from core.dal import DAL

class ScheduleController(FletController):

    def build(self):
        self.model.sched_pillsInfo.reset()
        self.model.sched_pillControls.reset()

        self.model.sched_pillsInfo.set_value(DAL.read_pills_schedule_page(self.model.username.value))
        self.model.sched_pillsInfo.set_value(sorted(self.model.sched_pillsInfo.value, key=lambda x: x[0]))

        self.model.sched_pillControls.set_value([
            pt_schedule.Control(medname=pill[0], dailyintake=pill[1], totalpills=pill[2], pill_id=pill[3], controller=self)
            for pill in self.model.sched_pillsInfo.value
        ])

    def build_reload(self):
        self.model.sched_pillsInfo.reset()
        self.model.sched_pillControls.reset()

        self.model.sched_pillsInfo.set_value(DAL.read_pills_schedule_page(self.model.username.value))
        self.model.sched_pillsInfo.set_value(sorted(self.model.sched_pillsInfo.value, key=lambda x: x[0]))

        self.model.sched_pillControls.set_value([
            pt_schedule.Control(medname=pill[0], dailyintake=pill[1], totalpills=pill[2], pill_id=pill[3], controller=self)
            for pill in self.model.sched_pillsInfo.value
        ])

        self.reload()


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
                self.reload()

                self.model.pill_name.reset()
                self.model.pill_total_amt.reset()
                self.model.pill_daily_intake.reset()
                return 1
            else: 
                self.alert("FAILED TO CREATE PILL. Please fill up all text fields. Ensure none of the fields are null or zero.", alert.WARNING)
                return -1
        
    def delete_pill(self, control):
        print("DELETING PILL WITH ID: ", control.pill_id)
        isDeleted = DAL.delete_pill(control.pill_id)

        self.alert(f"Deleted {control.medname} successfully.", alert.SUCCESS) if isDeleted else self.alert(f"Failed to delete {control.medname}.", alert.WARNING)

        self.build_reload()


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
    