from flet_mvc import FletView
import flet as ft
from user_controls import *

class RegisterView(FletView):
    def __init__(self, controller, model):
        view = [
            ft.Container(
                image_src=f"/images/register_bg.png",
                image_fit=ft.ImageFit.COVER,
                expand=True,
                content=ft.Column([
                    ft.Row([
                        ft.Text("Register", size=48),
                    ], alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row([
                        ft.Column([
                            ft.Text("Lorem Ipsum", size=24, color="#babbc7"),
                        ]),
                        ft.Column([
                            ft.TextField(label="Placeholder", bgcolor="#242930", color="#babbc7", height=30, width=180),
                        ]),
                    ], alignment=ft.MainAxisAlignment.CENTER
                    )
                    
                ], alignment=ft.MainAxisAlignment.CENTER
                )
            , alignment=ft.alignment.center
            )
        ]
        
        super().__init__(model, view, controller)
