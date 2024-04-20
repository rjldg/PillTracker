from flet_mvc import FletView
import flet as ft


class LoginView(FletView):
    def __init__(self, controller, model):
        view = [
            ft.Text(ref=model.example_title, size=30),
            ft.ElevatedButton(
                "Go to register view", on_click=controller.navigate_secundary
            ),
        ]
        super().__init__(model, view, controller)
