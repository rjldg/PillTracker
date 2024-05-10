import flet as ft
import math

class Control(ft.Container):
    def __init__(self, medname:str, dailyintake, totalpills, pill_id, controller):
        self.pill_id = pill_id
        self.medname = medname

        super().__init__(
            gradient=ft.LinearGradient(colors=["#1b1926", "#1e2125"], rotation=math.degrees(-33)),
            border=ft.border.all(1, "#000000"),
            border_radius=ft.border_radius.all(10),
            padding=ft.padding.only(left=30, right=30, top=20, bottom=20),
            width=300,
            content=ft.Column([
                ft.Text(medname, color="#e2e7ea", size=24, weight=ft.FontWeight.BOLD),
                ft.Text(f"Take {dailyintake} times a day", color="#e2e7ea", size=14,),
                ft.Text(f"{totalpills} Total Pills", color="#e2e7ea", size=14),
                ft.ResponsiveRow([
                    ft.Container(
                        bgcolor=ft.colors.TRANSPARENT, 
                        content=ft.Text("Delete", weight=ft.FontWeight.BOLD, color="#3c9fae", size=14),
                        alignment=ft.alignment.center,
                        ink=True,
                        on_click=lambda e: controller.delete_pill(self),
                        col=6,
                    ),
                    ft.Container(
                        bgcolor=ft.colors.TRANSPARENT, 
                        content=ft.Text("Update", weight=ft.FontWeight.BOLD, color="#3c9fae", size=14),
                        alignment=ft.alignment.center,
                        ink=True,
                        on_click=lambda e: print("dummy text!"),
                        col=6,
                    ),
                ])
            ])
        )