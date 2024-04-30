from flet_mvc import FletView
import flet as ft
from user_controls import *

class HomeView(FletView):
    def __init__(self, controller, model):
        view = [
            ft.Text("mic check!!!")
        ]
        super().__init__(model, view, controller)