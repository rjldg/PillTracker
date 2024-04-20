import flet as ft
from flet_mvc import RouteHandler

# Models
from models.login import LoginModel
from models.register import RegisterModel

# Views
from views.login import LoginView
from views.register import RegisterView

# Controllers
from controllers.login import LoginController
from controllers.register import RegisterController


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
    register_model = RegisterModel()
    register_control = RegisterController(page, register_model)
    register_model.controller = register_control
    register_view = RegisterView(register_control, register_model)
    routes_handler.register_route("/register", register_view.content)

    # Global settings for pages
    theme = ft.Theme()
    platforms = ["android", "ios", "macos", "linux", "windows"]
    for platform in platforms:  # Removing animation on route change.
        setattr(theme.page_transitions, platform, ft.PageTransitionTheme.NONE)

    page.title = "PillTracker"
    page.theme = theme
    page.on_route_change = routes_handler.route_change  # route change

    # Run PillTracker
    page.go(page.route)


ft.app(target=main)
