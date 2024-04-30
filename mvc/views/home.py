from flet_mvc import FletView
import flet as ft
import math
from user_controls import *

class HomeView(FletView):
    def __init__(self, controller, model):
        adherance_data = [
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(1,5),
                    ft.LineChartDataPoint(2,6),
                    ft.LineChartDataPoint(3,4),
                    ft.LineChartDataPoint(4,5),
                    ft.LineChartDataPoint(5,5),
                    ft.LineChartDataPoint(6,8),
                    ft.LineChartDataPoint(7,7),
                ],
                stroke_width=2,
                stroke_cap_round=False,
                curved=False,
                color="#2e3192",
            ),
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(1,5),
                    ft.LineChartDataPoint(2,5),
                    ft.LineChartDataPoint(3,4),
                    ft.LineChartDataPoint(4,6),
                    ft.LineChartDataPoint(5,4),
                    ft.LineChartDataPoint(6,10),
                    ft.LineChartDataPoint(7,5),
                ],
                stroke_width=2,
                stroke_cap_round=False,
                curved=False,
                color="#0072bc",
            ),
        ]

        view = [
            ft.Container(
                expand=True,
                gradient=ft.LinearGradient(colors=["#1e2125", "#201925", "#1e2125"], rotation=math.degrees(-33)),
                content=
                ft.Column([
                    pt_navbar.Navbar(to_home=controller.nav_home, to_schedule=controller.nav_schedule),
                    ft.Container(padding=ft.padding.symmetric(horizontal=70, vertical=20), content=
                        ft.ResponsiveRow([
                            ft.Column([
                                ft.Text("Daily Medication", size=24, weight=ft.FontWeight.BOLD, color="#e2e7ea"),
                                pt_pilltaken.Control(medname="Darkacetamol"),
                                pt_pilltaken.Control(medname="Blackezol", defaultvalue=2),
                                pt_pilltaken.Control(medname="Anti-Gluthathione", defaultvalue=1),
                                pt_pilltaken.Control(medname="Darkacetamol"),
                                pt_pilltaken.Control(medname="Blackezol", defaultvalue=2),
                                pt_pilltaken.Control(medname="Anti-Gluthathione", defaultvalue=1),
                                pt_pilltaken.Control(medname="Darkacetamol"),
                                pt_pilltaken.Control(medname="Blackezol", defaultvalue=2),
                                pt_pilltaken.Control(medname="Anti-Gluthathione", defaultvalue=1),
                                pt_pilltaken.Control(medname="Darkacetamol"),
                                pt_pilltaken.Control(medname="Blackezol", defaultvalue=2),
                                pt_pilltaken.Control(medname="Anti-Gluthathione", defaultvalue=1),
                            ], col=8),
                            ft.Column([
                                ft.Text("Refill Reminder", size=24, weight=ft.FontWeight.BOLD, color="#e2e7ea"),
                                ft.Text("All your pill bottles are plenty enough, take more!", size=16,color="#e2e7ea", italic=True),
                                ft.Text("Adherance", size=24, weight=ft.FontWeight.BOLD, color="#e2e7ea"),
                                ft.LineChart(
                                    data_series=adherance_data,
                                    border=ft.border.only(bottom=ft.BorderSide(4, "#e2e7ea"), left=ft.BorderSide(4, "#e2e7ea"))
                                )
                            ], col=4)
                        ], spacing=50)

                    ),
                ], scroll=ft.ScrollMode.ALWAYS)
            )
        ]
        super().__init__(model, view, controller)