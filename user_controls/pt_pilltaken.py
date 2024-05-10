from flet_mvc import alert
import flet as ft
import math

class Control(ft.Container):
    def __init__(self, pill_id:int, medname:str, controller, defaultvalue=0):

        def increment_pills_taken(e):
            pills_taken_text.value = str(int(pills_taken_text.value) + 1)
            self.update()

            decrement_button.visible = True if int(pills_taken_text.value) > 0 else False
            decrement_button.update()

            controller.increment_pills_taken(self)

        def decrement_pills_taken(e):
            pills_taken_text.value = str(int(pills_taken_text.value) - 1)
            self.update()
            
            decrement_button.visible = False if int(pills_taken_text.value) <= 0 else True
            decrement_button.update()

            controller.decrement_pills_taken(self)

        self.pill_id = pill_id
        self.defaultvalue = defaultvalue

        pills_taken_text = ft.Text(value=self.defaultvalue, color="#3c9fae", size=18, weight=ft.FontWeight.BOLD)
        decrement_button = ft.Container(
                            bgcolor="#3c9fae", 
                            border_radius=ft.border_radius.all(255),
                            content=ft.Text("-", weight=ft.FontWeight.BOLD, color="#e2e7ea", size=10),
                            width=25,
                            height=25,
                            alignment=ft.alignment.center,
                            ink=True,
                            on_click=decrement_pills_taken,
                            visible=int(pills_taken_text.value) > 0
                        )

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
                        decrement_button,
                        pills_taken_text,
                        ft.Container(
                            bgcolor="#3c9fae", 
                            border_radius=ft.border_radius.all(255),
                            content=ft.Text("+", weight=ft.FontWeight.BOLD, color="#e2e7ea", size=10),
                            width=25,
                            height=25,
                            alignment=ft.alignment.center,
                            ink=True,
                            on_click=increment_pills_taken
                        ),
                    ]))
                ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        )

        

    
    