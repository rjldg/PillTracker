from flet_mvc import FletView
import flet as ft


class RegisterView(FletView):
    def __init__(self, controller, model):
        view = [
            ft.Text(ref=model.example_title, size=30),
            ft.ElevatedButton("Go to login view", on_click=controller.nav_login),
        ]
        super().__init__(model, view, controller)
