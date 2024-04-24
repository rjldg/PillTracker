import flet as ft

class Button(ft.Container):
    def __init__(self, in_text : str, on_click):
        super().__init__(
            margin=ft.Margin(0, 20, 0, 0),
            gradient=ft.LinearGradient(colors=["#1c528e", "#3c9fae"], begin=ft.Alignment(0,0.5), end=ft.Alignment(1,0.5)),
            width=170,
            height=40,
            ink=True,
            alignment=ft.alignment.center,
            border=ft.border.all(1, "#1a2440"),
            border_radius=5,
            on_click=on_click,
            content=ft.Text(in_text, weight=ft.FontWeight.BOLD, color="#1e2125", size=20)
        )
        