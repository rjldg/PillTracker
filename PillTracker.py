import flet as ft
from flet_mvc import RouteHandler

# Models
from mvc.models.login import LoginModel
from mvc.models.register import RegisterModel

# Views
from mvc.views.login import LoginView
from mvc.views.register import RegisterView

# Controllers
from mvc.controllers.login import LoginController
# from mvc.controllers.register import RegisterController


def main(page: ft.Page):
    ### MVC set-up ###
    routes_handler = RouteHandler(page)

    # Login MVC Initialization
    login_model = LoginModel()
    login_controller = LoginController(page, login_model)
    login_model.controller = login_controller
    login_view = LoginView(login_controller, login_model)
    routes_handler.register_route("/", login_view.content)

    # Register MVC Initialization
    # register_model = RegisterModel()
    # register_control = RegisterController(page, register_model)
    # register_model.controller = register_control
    # register_view = RegisterView(register_control, register_model)
    # routes_handler.register_route("/register", register_view.content)

    # Global settings for pages
    theme = ft.Theme()
    platforms = ["android", "ios", "macos", "linux", "windows"]
    for platform in platforms:  # Removing animation on route change.
        setattr(theme.page_transitions, platform, ft.PageTransitionTheme.NONE)

    page.fonts = {
        "Despairs" : "font/Despairs-X3Wxo"
    }
    page.title = "PillTracker"
    page.theme = theme
    page.theme_mode = "dark"
    page.window_height = 720
    page.window_width = 1280
    page.on_route_change = routes_handler.route_change  # route change

    # Run PillTracker
    page.go(page.route)


ft.app(target=main)
