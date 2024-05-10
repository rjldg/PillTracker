from flet_mvc import FletView
import flet as ft
import math
from user_controls import *

class HomeView(FletView):
    def __init__(self, controller, model):
        adh_data = chart_data.AdhData(expected_datapoints=[5,6,4,5,5,8,7], actual_datapoints=[5,5,4,6,4,10,5])
        
        refill_list = [
            pt_refillreminder.Control(medname="Darkacetamol", quantity=149),
            pt_refillreminder.Control(medname="Anti-Gluthathione", quantity=124),
            pt_refillreminder.Control(medname="Blackezol", quantity=499),
        ]

        refill_reminder_content = [
            ft.Text("Refill Reminders", size=24, weight=ft.FontWeight.BOLD, color="#e2e7ea"),
            # If empty:     
            ft.Text("All your pill bottles are plenty enough, take more!", size=16,color="#e2e7ea", italic=True),
            # Else:
            ft.Column(ref=model.home_refillReminders)
        ]

        #refill_reminder_content.extend(model.home_refillReminders.value)

        view = [
            ft.Container(
                expand=True,
                gradient=ft.LinearGradient(colors=["#1e2125", "#201925", "#1e2125"], rotation=math.degrees(-33)),
                content=
                ft.Column([
                    pt_navbar.Navbar(title="Home", model=model, to_home=controller.nav_home, to_schedule=controller.nav_schedule, to_account=controller.nav_account),
                    ft.Container(padding=ft.padding.symmetric(horizontal=70, vertical=20), content=
                        ft.ResponsiveRow([
                            ### first column
                            ft.Column([
                                ft.Text("Daily Medication", size=24, weight=ft.FontWeight.BOLD, color="#e2e7ea"),
                                ft.Column(ref=model.home_pillControls),
                                ft.Text("Adherance Statistics", size=24, weight=ft.FontWeight.BOLD, color="#e2e7ea"),
                                ft.LineChart(
                                    data_series=adh_data.adherance_data,
                                    border=ft.border.only(bottom=ft.BorderSide(4, "#e2e7ea"), left=ft.BorderSide(4, "#e2e7ea")),
                                    min_y=0,
                                    max_y=10,
                                    min_x=1,
                                    max_x=7,
                                    left_axis=ft.ChartAxis(
                                        labels=adh_data.y_labels,
                                        labels_size=12,
                                    ),
                                    bottom_axis=ft.ChartAxis(
                                        labels=adh_data.x_labels
                                    )
                                )
                            ], col=8),
                            ### second column
                            ft.Column(refill_reminder_content, col=4)
                        ], spacing=50)

                    ),
                ], scroll=ft.ScrollMode.ALWAYS)
            )
        ]
        super().__init__(model, view, controller)