from flet_mvc import FletView
import flet as ft
import math
from user_controls import *

class ScheduleView(FletView):
    is_create = False
    def __init__(self, controller, model):
        
        """NO LONGER NEEDED"""
        '''
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
        '''
        def in_create(e=None):
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
        
        def create_new_pill(e):
            
            result = controller.create_new_pill()

            if result == 1:
                in_create()
            
            controller.reload()

        # for main schedule page
        main_view = ft.Container(
                expand=True,
                gradient=ft.LinearGradient(colors=["#1e2125", "#201925", "#1e2125"], rotation=math.degrees(-33)),
                content=
                ft.Stack([
                    ft.Column([
                        pt_navbar.Navbar(title="Home", model=model, to_home=controller.nav_home, to_schedule=controller.nav_schedule, to_account=controller.nav_account),
                        ft.Container(content=ft.SearchBar(
                            divider_color="#3c9fae",
                            bar_hint_text="Search for Pills",
                            bar_bgcolor="#1e2125",
                            bar_overlay_color="#3c9fae",
                            height=35,
                            expand=True,
                        ), alignment=ft.alignment.center, margin=ft.margin.only(top=10), expand=True,),
                        ft.Container(padding=ft.padding.symmetric(horizontal=70, vertical=20), expand=True, alignment=ft.alignment.top_center ,content=
                            #ft.Row(controls=schedule_list, wrap=True, scroll=ft.ScrollMode.AUTO)
                            ft.Row(ref=model.sched_pillControls, wrap=True, scroll=ft.ScrollMode.AUTO)
                        ),
                    ], expand=True),
                    pt_button.FloatingButton(in_create)
                ])
            )
        
        # for create pill schedule
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
                        ft.Text("Create Pill Information & Schedule", size=28, color="#e2e7ea", weight=ft.FontWeight.BOLD,),
                        ft.ResponsiveRow([
                            ft.Text("Pill Name:", size=20, color="#e2e7ea", col=3),
                            ft.Column(col=9, controls=[pt_textfield.Field(label="Name of Pill", model=model.pill_name)])
                        ], vertical_alignment=ft.CrossAxisAlignment.CENTER),
                        ft.ResponsiveRow([
                            ft.Text("Total Pills:", size=20, color="#e2e7ea", col=3),
                            ft.Column(col=9, controls=[pt_textfield.Field(label="Total Amount of Pills", model=model.pill_total_amt)])
                        ], vertical_alignment=ft.CrossAxisAlignment.CENTER),
                        ft.ResponsiveRow([
                            ft.Text("Daily Intake:", size=20, color="#e2e7ea", col=3),
                            ft.Column(col=9, controls=[pt_textfield.Field(label="Daily Pill Intake", model=model.pill_daily_intake)])
                        ], vertical_alignment=ft.CrossAxisAlignment.CENTER),
                        ft.Row([
                            pt_button.Button(text="Cancel", on_click=in_create, btn_type="secondary"),
                            pt_button.Button(text="Create", on_click=create_new_pill),
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