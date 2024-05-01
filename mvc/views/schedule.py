from flet_mvc import FletView
import flet as ft
import math
from user_controls import *

class ScheduleView(FletView):
    def __init__(self, controller, model):
        schedule_list = [
            # sample preset
            pt_schedule.Control(medname="Darkacetamol", dailyintake=4, totalpills=100),
            pt_schedule.Control(medname="Lanceotoxin B", dailyintake=3, totalpills=50),
            pt_schedule.Control(medname="Mystezol", dailyintake=2, totalpills=500),
            pt_schedule.Control(medname="Usendorfim", dailyintake=2, totalpills=20),
            pt_schedule.Control(medname="Lunaticone", dailyintake=5, totalpills=200),
            pt_schedule.Control(medname="Suispirin", dailyintake=1, totalpills=25),
            pt_schedule.Control(medname="Kaliline", dailyintake=2, totalpills=75),
            pt_schedule.Control(medname="Akaiotic", dailyintake=1, totalpills=125),
            pt_schedule.Control(medname="Shikimide", dailyintake=3, totalpills=150),
        ]

        def add_pill(e):
            print("enter!")
            schedule_list.append(
                pt_schedule.Control(medname="Burgerizer", dailyintake=15, totalpills=1500)
            )
            controller.reload()
        
        view = [
            ft.Container(
                expand=True,
                gradient=ft.LinearGradient(colors=["#1e2125", "#201925", "#1e2125"], rotation=math.degrees(-33)),
                content=
                ft.Stack([
                    ft.Column([
                        pt_navbar.Navbar(title="Schedule",to_home=controller.nav_home, to_schedule=controller.nav_schedule),
                        ft.Container(padding=ft.padding.symmetric(horizontal=70, vertical=20), expand=True, alignment=ft.alignment.top_center ,content=
                            ft.Row(controls=schedule_list, wrap=True, expand=True, scroll=ft.ScrollMode.AUTO)
                        ),
                    ], expand=True),
                    ft.Container(
                        bgcolor="#3c9fae", 
                        border_radius=ft.border_radius.all(255),
                        content=ft.Text("+", weight=ft.FontWeight.BOLD, color="#e2e7ea", size=24),
                        width=50,
                        height=50,
                        alignment=ft.alignment.center,
                        ink=True,
                        on_click=add_pill,
                        margin=ft.margin.all(20),
                        right=0,
                        bottom=0,
                    )
                ])
            )
        ]

        super().__init__(model, view, controller)