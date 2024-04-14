from mvc.controller.registerController import RegisterController
from mvc.view.registerView import RegisterView
from mvc.model.registerModel import RegisterModel

import flet as ft


def main(page):
    # MVC set-up
    registerModel = RegisterModel()
    registerController = RegisterController(page, registerModel)
    registerModel.controller = registerController
    view = RegisterView(registerController, registerModel)

    # Settings
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = "light"

    # Run
    page.add(*view.content)


ft.app(target=main)
