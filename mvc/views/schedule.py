from flet_mvc import FletView
import flet as ft
import math
from user_controls import *

class ScheduleView(FletView):
    is_create = False
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
        
        def in_create(e):
            self.is_create = not self.is_create # toggle
            if self.is_create:
                create_view_overlay.visible = True
                create_view.offset = ft.transform.Offset(0,0)
                create_view_overlay.opacity = 0.3
            else:
                create_view.offset = ft.transform.Offset(-1,0)
                create_view_overlay.opacity = 0
                create_view_overlay.visible = False
                
            controller.reload()

        # for main schedule page
        main_view = ft.Container(
                expand=True,
                gradient=ft.LinearGradient(colors=["#1e2125", "#201925", "#1e2125"], rotation=math.degrees(-33)),
                content=
                ft.Stack([
                    ft.Column([
                        pt_navbar.Navbar(title="Schedule",to_home=controller.nav_home, to_schedule=controller.nav_schedule, to_account=controller.nav_account),
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
                        on_click=in_create,
                        margin=ft.margin.all(20),
                        right=0,
                        bottom=0,
                    )
                ])
            )
        
        # for create pill schedile
        create_view_overlay = ft.Container(
            bgcolor="#000000",
            expand=True,
            opacity=0.3,
            animate_opacity=750,
            visible=False,
            on_click=in_create,
        )
        create_view = ft.Container(
                    offset=ft.transform.Offset(-1,0),
                    animate_offset=ft.animation.Animation(750, ft.AnimationCurve.EASE_OUT_QUINT),
                    padding=ft.padding.all(50), 
                    expand=True, 
                    bgcolor="#1e2125", 
                    margin=ft.margin.only(right=100), 
                    border_radius=ft.border_radius.only(top_right=25, bottom_right=25), 
                    border=ft.border.all(1, "#000000"), 
                    content=ft.Column([
                        ft.Text("Create Pill Schedule", size=28, color="#e2e7ea", weight=ft.FontWeight.BOLD,),
                        ft.ResponsiveRow([
                            ft.Text("Pill Name:", size=20, color="#e2e7ea", col=3),
                            ft.Column(col=9, controls=[pt_textfield.Field(label="Name", model=model.dummy)])
                        ], vertical_alignment=ft.CrossAxisAlignment.CENTER),
                        ft.ResponsiveRow([
                            ft.Text("Total Pills:", size=20, color="#e2e7ea", col=3),
                            ft.Column(col=9, controls=[pt_textfield.Field(label="Total Pills in Bottle", model=model.dummy)])
                        ], vertical_alignment=ft.CrossAxisAlignment.CENTER),
                        ft.ResponsiveRow([
                            ft.Text("Daily Intake:", size=20, color="#e2e7ea", col=3),
                            ft.Column(col=9, controls=[pt_textfield.Field(label="Take n times a day", model=model.dummy)])
                        ], vertical_alignment=ft.CrossAxisAlignment.CENTER),
                        ft.Row([
                            pt_button.Button(text="Cancel", on_click=in_create, btn_type="secondary"),
                            pt_button.Button(text="Create", on_click=in_create,),
                        ],alignment=ft.MainAxisAlignment.END)
                ]))
        
        view = [
            ft.Stack(expand=True, controls=[
                main_view,
                create_view_overlay,
                create_view
            ])
        ]

        super().__init__(model, view, controller)