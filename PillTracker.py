import flet as ft
from flet_mvc import RouteHandler

# Models
from mvc.models.login import LoginModel
from mvc.models.register import RegisterModel
from mvc.models.home import HomeModel

# Views
from mvc.views.login import LoginView
from mvc.views.register import RegisterView
from mvc.views.home import HomeView

# Controllers
from mvc.controllers.login import LoginController
from mvc.controllers.register import RegisterController
from mvc.controllers.home import HomeController


def main(page: ft.Page):
    ### MVC set-up ###
    routes_handler = RouteHandler(page)

    # Login MVC Initialization
    login_model = LoginModel()
    login_controller = LoginController(page, login_model)
    login_model.controller = login_controller
    login_view = LoginView(login_controller, login_model)
    routes_handler.register_route("/home", login_view.content)

    # Register MVC Initialization
    register_model = RegisterModel()
    register_control = RegisterController(page, register_model)
    register_model.controller = register_control
    register_view = RegisterView(register_control, register_model)
    routes_handler.register_route("/register", register_view.content)

    # Register MVC Initialization
    home_model = HomeModel()
    home_control = HomeController(page, home_model)
    home_model.controller = home_control
    home_view = HomeView(home_control, home_model)
    routes_handler.register_route("/", home_view.content)

    # Global settings for pages
    theme = ft.Theme()
    platforms = ["android", "ios", "macos", "linux", "windows"]
    for platform in platforms:  # Removing animation on route change.
        setattr(theme.page_transitions, platform, ft.PageTransitionTheme.NONE)

    page.fonts = {
        "Despairs" : "fonts/Despairs-X3Wxo.ttf"
    }
    page.title = "PillTracker"
    page.theme = ft.Theme(font_family="Gadugi")
    page.theme = theme
    page.theme_mode = "dark"
    page.window_height = 720
    page.window_width = 1280
    page.on_route_change = routes_handler.route_change  # route change

    # Run PillTracker
    page.go(page.route)


ft.app(target=main, assets_dir="assets")
