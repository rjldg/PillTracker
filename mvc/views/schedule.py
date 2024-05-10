from flet_mvc import FletView
import flet as ft
import math
from user_controls import *

class ScheduleView(FletView):   
    is_create = False 
    def __init__(self, controller, model):
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
                        pt_navbar.Navbar(title="Schedule", model=model, to_home=controller.nav_home, to_schedule=controller.nav_schedule, to_account=controller.nav_account),
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
        create_view = createsched_view.Panel(
            model_pillname=model.pill_name, 
            model_pilltotal=model.pill_total_amt, 
            model_dailyintake=model.pill_daily_intake,
            controller=controller,
            toggle=in_create,
            offset=ft.transform.Offset(-1,0),
        )
        create_view_overlay = createsched_view.OverlayPanel(
            toggle=in_create, 
            visible=False,
            opacity=0,
        )
        
        view = [
            ft.Stack(expand=True, controls=[
                main_view,
                create_view_overlay,
                create_view
            ])
        ]

        super().__init__(model, view, controller)