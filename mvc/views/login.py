from flet_mvc import FletView
import flet as ft
import math
import os

images_folder = "../images"
image_filename = "login_bg.png"

class LoginView(FletView):
    def __init__(self, controller, model):
        

        view = [
            ft.Container(
                image_src=os.path.join(os.path.dirname(__file__), "..", images_folder, image_filename),
                image_fit=ft.ImageFit.COVER,
                expand=True,
                content=ft.Column(
                [
                    ft.Row([
                        ft.Text(ref=model.app_title, size=64, text_align="CENTER", font_family="Despairs")  
                    ], alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row([
                        ft.TextField(label="Username", border_color="#16181b", fill_color="#1e2125", height=50, ref=model.username, text_style=ft.TextStyle(font_family="Gadugi", color="#babbc7")),
                    ], alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row([
                        ft.TextField(label="Password", border_color="#16181b", fill_color="#1e2125", height=50, ref=model.password, password=True, can_reveal_password=True),
                    ], alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row([
                        ft.Container(
                            margin=ft.Margin(0, 20, 0, 0),
                            gradient=ft.LinearGradient(colors=["#1c528e", "#3c9fae"], begin=ft.Alignment(0,0.5), end=ft.Alignment(1,0.5)),
                            width=170,
                            height=40,
                            content=ft.Text("Login", weight=ft.FontWeight.BOLD, color="#1e2125", size=20),
                            ink=True,
                            alignment=ft.alignment.center,
                            border=ft.border.all(1, "#1a2440"),
                            border_radius=5,
                            on_click=controller.validate_login
                        )
                    ], alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row([
                        ft.Row([
                            ft.Text("Don't have an account?", size=12),
                            ft.Container(
                                content=ft.Text("Register here", size=12, color="#3c9fae",),
                                ink=True,
                                on_click=lambda e: print("shift registah"),
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
