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
                        ft.TextField(label="Username", border_color="#16181b", fill_color="#1e2125", height=50, ref=model.username),
                    ], alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row([
                        ft.TextField(label="Password", border_color="#16181b", fill_color="#1e2125", height=50, ref=model.password),
                    ], alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row([
                        ft.FilledButton(text="Login", style=ft.ButtonStyle(
                            bgcolor="#2d7a9f",
                            color="#1e2125",
                        ))
                    ], alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row([
                        ft.Text("Don't have an account? Register here")
                    ], alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER
                )
            )
        ]
        
        super().__init__(model, view, controller)
