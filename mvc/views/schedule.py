from flet_mvc import FletView
import flet as ft
import math
from user_controls import *

class ScheduleView(FletView):
    def __init__(self, controller, model):
        view = [
            ft.Container(
                expand=True,
                gradient=ft.LinearGradient(colors=["#1e2125", "#201925", "#1e2125"], rotation=math.degrees(-33)),
                content=
                ft.Column([
                    pt_navbar.Navbar(title="Schedule",to_home=controller.nav_home, to_schedule=controller.nav_schedule),
                    ft.Container(padding=ft.padding.symmetric(horizontal=70, vertical=20), content=
                        ft.ResponsiveRow([

                        ])
                    )
                ])
            )
        ]
        super().__init__(model, view, controller)