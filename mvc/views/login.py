from flet_mvc import FletView
import flet as ft
import math
import os
from user_controls import *

class LoginView(FletView):
    def __init__(self, controller, model):
        view = [
            ft.Container(
                image_src=f"/images/login_bg.png",
                image_fit=ft.ImageFit.COVER,
                expand=True,
                content=ft.Column(
                [
                    ft.Row([
                        ft.Text("PillTracker", size=64, text_align="CENTER", font_family="Despairs")  
                    ], alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row([
                        pt_textfield.Field(label="Username", model=model.username)
                    ], alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row([
                        pt_textfield.Field(label="Password", model=model.password, have_password=True)
                    ], alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row([
                        pt_button.Button(text="Login", on_click=controller.validate_login),
                    ], alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row([
                        ft.Row([
                            ft.Text("Don't have an account?", size=12),
                            ft.Container(
                                content=ft.Text("Register here", size=12, color="#3c9fae",),
                                ink=True,
                                on_click=controller.nav_register,
                            )
                        ], vertical_alignment=ft.alignment.center)
                    ], alignment=ft.MainAxisAlignment.CENTER
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER
                )
            )
        ]
        
        super().__init__(model, view, controller)
