import flet as ft
from flet_mvc import RouteHandler

# Models
from mvc.models.login import LoginModel
from mvc.models.register import RegisterModel
from mvc.models.home import HomeModel
from mvc.models.schedule import ScheduleModel
from mvc.models.account import AccountModel

# Views
from mvc.views.login import LoginView
from mvc.views.register import RegisterView
from mvc.views.home import HomeView
from mvc.views.schedule import ScheduleView
from mvc.views.account import AccountView

# Controllers
from mvc.controllers.login import LoginController
from mvc.controllers.register import RegisterController
from mvc.controllers.home import HomeController
from mvc.controllers.schedule import ScheduleController
from mvc.controllers.account import AccountController


def main(page: ft.Page):
    ### MVC set-up ###
    routes_handler = RouteHandler(page)
    model_list = [LoginModel(), RegisterModel(), HomeModel(), ScheduleModel(), LoginModel()]
    controller_list = [
        LoginController(page, model_list[0]), 
        RegisterController(page, model_list[1]), 
        HomeController(page, model_list[2]), 
        ScheduleController(page, model_list[3]), 
        AccountController(page, model_list[4])
    ]
    view_list = [
        LoginView(controller_list[0], model_list[0]),
        RegisterView(controller_list[1], model_list[1]),
        HomeView(controller_list[2], model_list[2]),
        ScheduleView(controller_list[3], model_list[3]),
        AccountView(controller_list[4], model_list[4]),
    ]
    pages = [
        [""         , model_list[0], controller_list[0], view_list[0]],
        ["register" , model_list[1], controller_list[1], view_list[1]],
        ["home"     , model_list[2], controller_list[2], view_list[2]],
        ["schedule" , model_list[3], controller_list[3], view_list[3]],
        ["account"  , model_list[4], controller_list[4], view_list[4]]
    ]
    for p in pages:
        p[1].controller = p[2]
        routes_handler.register_route(f"/{p[0]}", p[3].content)

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

    # Resize global settings
    def page_resize(e):
        return [page.window_width, page.window_height]
    
    page.on_resize = page_resize

    # Run PillTracker
    page.go(page.route)


ft.app(target=main, assets_dir="assets")
