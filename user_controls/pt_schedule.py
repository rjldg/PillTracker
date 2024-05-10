import flet as ft
import math
from user_controls import createsched_view, pt_textfield, pt_button

class Control(ft.Container):
    def __init__(self, medname:str, dailyintake, totalpills, pill_id, controller):
        self.pill_id = pill_id
        self.medname = medname

        def show_bs(e):
            bs.open = True
            bs.update()

        def close_bs_cancel(e):
            bs.open = False
            bs.update()

        def close_bs_update(e):
            result = controller.update_pill(u1.value, u2.value, u3.value, pill_id)
            if result == 1:
                bs.open = False
                u1.value = ""
                u2.value = ""
                u3.value = ""
            
            
            

        u1 = pt_textfield.Field(label="Updated Name of Pill", model=None)
        u2 = pt_textfield.Field(label="Updated Total Amount of Pills", model=None)
        u3 = pt_textfield.Field(label="Updated Daily Pill Intake", model=None)

        bs = ft.BottomSheet(
            ft.Container(
                ft.Column(
                    [
                        u1,
                        u2,
                        u3,
                        ft.Row([
                            pt_button.Button(text="Cancel", on_click=close_bs_cancel, btn_type="secondary"),
                            pt_button.Button(text="Update Schedule", on_click=close_bs_update),
                        ], alignment=ft.MainAxisAlignment.END)
                    ],
                    tight=True,
                ),
                padding=10,
            ),
            open=False,
        )

        super().__init__(
            gradient=ft.LinearGradient(colors=["#1b1926", "#1e2125"], rotation=math.degrees(-33)),
            border=ft.border.all(1, "#000000"),
            border_radius=ft.border_radius.all(10),
            padding=ft.padding.only(left=30, right=30, top=20, bottom=20),
            width=300,
            content=ft.Column([
                bs,
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
                        on_click=show_bs,
                        col=6,
                    ),
                ]),
            ])
        )