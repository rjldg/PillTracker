from flet_mvc import FletView
import flet as ft


class LoginView(FletView):
    def __init__(self, controller, model):
        view = [
            ft.Container(
                image_src='../images/login_bg.png',
                image_fit=ft.ImageFit.COVER,
                expand=True,
                content=ft.Row(
                [
                    ft.Column([
                        ft.Text(ref=model.app_title, size=50, text_align="CENTER"),
                        ft.TextField(label="Email", border_color="#16181b", fill_color="#1e2125",
                                     height=50),
                        ft.TextField(label="Password", border_color="#16181b", fill_color="#1e2125",
                                     height=50, password=True, can_reveal_password=True),
                        ft.ElevatedButton(
                        "Go to register view", on_click=controller.nav_register),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
                )
            )
        ]
        
        super().__init__(model, view, controller)
