import flet as ft
import math

class Control(ft.Container):
    def __init__(self, medname:str, quantity:int):
        super().__init__(
            gradient=ft.LinearGradient(colors=["#1b1926", "#1e2125"], rotation=math.degrees(-33)),
            border=ft.border.all(1, "#000000"),
            border_radius=ft.border_radius.all(10),
            height=50,
            padding=ft.padding.symmetric(horizontal=10),
            content=ft.Row([
                ft.Column([
                    ft.Text(medname, color="#e2e7ea", size=18),
                ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Column([
                    ft.Container(alignment=ft.alignment.center,content=ft.Row([
                        ft.Text(f"{quantity} pills left")
                    ]))
                ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        )