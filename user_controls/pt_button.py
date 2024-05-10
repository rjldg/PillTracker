import flet as ft

class Button(ft.Container):
    def __init__(self, text : str, on_click, btn_type="primary"):
        if btn_type=="primary":
            super().__init__(
                margin=ft.Margin(0, 20, 0, 0),
                width=170,
                height=40,
                ink=True,
                alignment=ft.alignment.center,
                border_radius=5,
                on_click=on_click,
                border=ft.border.all(1, "#1a2440"),
                content=ft.Text(text, weight=ft.FontWeight.BOLD, color="#1e2125", size=20),
                gradient=ft.LinearGradient(colors=["#1c528e", "#3c9fae"], begin=ft.Alignment(0,0.5), end=ft.Alignment(1,0.5)), 
            )
        elif btn_type=="warning":
            super().__init__(
                margin=ft.Margin(0, 20, 0, 0),
                width=170,
                height=40,
                ink=True,
                alignment=ft.alignment.center,
                border_radius=5,
                on_click=on_click,
                border=ft.border.all(1, "#d93148"),
                content=ft.Text(text, weight=ft.FontWeight.NORMAL, color="#e2e7ea", size=20),
                gradient=ft.LinearGradient(colors=["#1e2125", "#1e2125"], begin=ft.Alignment(0,0.5), end=ft.Alignment(1,0.5)), 
            )
        else:
            super().__init__(
                margin=ft.Margin(0, 20, 0, 0),
                width=170,
                height=40,
                ink=True,
                alignment=ft.alignment.center,
                border_radius=5,
                on_click=on_click,
                border=ft.border.all(1, "#1f3a89"),
                content=ft.Text(text, weight=ft.FontWeight.NORMAL, color="#e2e7ea", size=20),
                gradient=ft.LinearGradient(colors=["#1e2125", "#1e2125"], begin=ft.Alignment(0,0.5), end=ft.Alignment(1,0.5)), 
            )

class FloatingButton(ft.Container):
    def __init__(self, on_click):
        super().__init__(
            bgcolor="#3c9fae", 
            border_radius=ft.border_radius.all(255),
            content=ft.Text("+", weight=ft.FontWeight.BOLD, color="#e2e7ea", size=24),
            width=50,
            height=50,
            alignment=ft.alignment.center,
            ink=True,
            on_click=on_click,
            margin=ft.margin.all(20),
            right=0,
            bottom=0,
        )
        