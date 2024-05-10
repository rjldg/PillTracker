import flet as ft

class Navbar(ft.ResponsiveRow):
    def __init__(self, title:str, model, to_home, to_schedule, to_account):
        navbar_content = ft.Container(
            padding=ft.padding.symmetric(horizontal=70),
            content=
            ft.ResponsiveRow(
                vertical_alignment=ft.CrossAxisAlignment.CENTER, 
                height=70,
                controls=[
                    ft.Column([
                        ft.Text(title, size=32, weight=ft.FontWeight.BOLD, color="#e2e7ea", text_align=ft.TextAlign.CENTER),
                    ], col=6, alignment=ft.MainAxisAlignment.CENTER),
                    ft.Column([
                        ft.Container(
                            content=ft.Text("Home", size=20, color="#e2e7ea"),
                            ink=True, margin=ft.Margin(left=20, right=20, top=0, bottom=0),
                            width=100, height=70, alignment=ft.alignment.center,
                            on_click=to_home,
                        ),
                    ], col=2),
                    ft.Column([
                        ft.Container(
                            content=ft.Text("Schedule", size=20, color="#e2e7ea"),
                            ink=True, margin=ft.Margin(left=20, right=20, top=0, bottom=0),
                            width=100, height=70, alignment=ft.alignment.center,
                            on_click=to_schedule,
                        ),
                    ], col=2),
                    ft.Column([
                        ft.Container(
                            content=ft.Row([
                                ft.Image(src="/images/account_circle.png", height=40, width=40),
                                ft.Text(ref=model.username, color="#e2e7ea", size=18)
                            ], alignment=ft.CrossAxisAlignment.CENTER),
                            margin=ft.Margin(left=20, right=20, top=0, bottom=0),
                            height=70, alignment=ft.alignment.center,
                            on_click=to_account, ink=True,
                        ),
                    ], col=2),
                ]
            )
        )

        navbar_stack = ft.Stack(
            col=12,
            controls=[
                # ft.Container(
                #     shadow=ft.BoxShadow(spread_radius=10, blur_radius=30, color="#000000"),
                #     height=70,
                #     bgcolor=ft.colors.TRANSPARENT,
                #     opacity=0.17,
                # ),
                ft.Container(
                    bgcolor="#1e2125", 
                    blend_mode=ft.BlendMode.COLOR_DODGE, 
                    height=70
                ), 
                ft.Container(
                    content=navbar_content
                )
            ]
        )

        super().__init__(
            controls=[navbar_stack],
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )