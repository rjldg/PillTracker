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
                content=ft.Row(
                [
                    ft.Column([
                        ft.Text(ref=model.app_title, size=50, text_align="CENTER"),
                        ft.TextField(label="Username", border_color="#16181b", fill_color="#1e2125",
                                     height=50, ref=model.username),
                        ft.TextField(label="Password", border_color="#16181b", fill_color="#1e2125",
                                     height=50, password=True, can_reveal_password=True, ref=model.password),
                        ft.Row([
                            ft.ElevatedButton("Register"),
                            ft.ElevatedButton("Log In"),
                        ]),
                        
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
                )
            )
        ]
        
        super().__init__(model, view, controller)
