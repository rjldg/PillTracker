from flet_mvc import FletView
import flet as ft
import math
from user_controls import pt_textfield, pt_button

class OverlayPanel(ft.Container):
    def __init__(self, toggle, visible=False, opacity=0.3,):
        super().__init__(
            bgcolor="#000000",
            expand=True,
            opacity=opacity,
            animate_opacity=750,
            visible=visible,
            on_click=toggle,
            # ref=model.create_view_overlay,
        )

class Panel(ft.Container):
    def __init__(self, model_pillname, model_pilltotal, model_dailyintake, controller, toggle, offset=ft.transform.Offset(-1,0)):
        super().__init__(
            offset=offset,
            animate_offset=ft.animation.Animation(750, ft.AnimationCurve.EASE_OUT_QUINT),
            padding=ft.padding.all(50), 
            expand=True, 
            bgcolor="#1e2125", 
            margin=ft.margin.only(right=100), 
            border_radius=ft.border_radius.only(top_right=25, bottom_right=25), 
            border=ft.border.all(1, "#000000"),
            # ref=model.create_view,
            content=ft.Column([
                ft.Text("Create Pill Information & Schedule", size=28, color="#e2e7ea", weight=ft.FontWeight.BOLD,),
                ft.ResponsiveRow([
                    ft.Text("Pill Name:", size=20, color="#e2e7ea", col=3),
                    ft.Column(col=9, controls=[pt_textfield.Field(label="Name of Pill", model=model_pillname)])
                ], vertical_alignment=ft.CrossAxisAlignment.CENTER),
                ft.ResponsiveRow([
                    ft.Text("Total Pills:", size=20, color="#e2e7ea", col=3),
                    ft.Column(col=9, controls=[pt_textfield.Field(label="Total Amount of Pills", model=model_pilltotal)])
                ], vertical_alignment=ft.CrossAxisAlignment.CENTER),
                ft.ResponsiveRow([
                    ft.Text("Daily Intake:", size=20, color="#e2e7ea", col=3),
                    ft.Column(col=9, controls=[pt_textfield.Field(label="Daily Pill Intake", model=model_dailyintake)])
                ], vertical_alignment=ft.CrossAxisAlignment.CENTER),
                ft.Row([
                    pt_button.Button(text="Cancel", on_click=toggle, btn_type="secondary"),
                    pt_button.Button(text="Create", on_click=controller.create_new_pill),
                ],alignment=ft.MainAxisAlignment.END)
            ])
        )