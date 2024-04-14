from flet_mvc import FletView
import flet as ft

class RegisterView(FletView):
    def __init__(self, registerController, registerModel):
        registerView = [
            ft.Column(
                width=700,
                controls=[
                    ft.TextField(
                        ref=registerModel.first_name,
                        hint_text="First Name"
                    ),
                    ft.FloatingActionButton(
                        icon=ft.icons.ADD,
                        on_click=registerController.enter
                    ),
                    ft.Text(ref=registerModel.first_name)
                ]
            )
        ]
        super().__init__(registerModel, registerView, registerController)