from flet_mvc import FletView
import flet as ft
import math
from user_controls import *

class AccountView(FletView):
    def __init__(self, controller, model):
        view = [
            ft.Container(
                image_src=f"/images/register_bg.png",
                image_fit=ft.ImageFit.COVER,
                expand=True,
                content=ft.Column([
                    ft.Row([
                        ft.Text("Edit Account Information", size=48),
                    ], alignment=ft.MainAxisAlignment.CENTER
                    ),

                    ft.Divider(color=ft.colors.TRANSPARENT, height=15),

                    # FULL NAME
                    ft.Row([
                        ft.Column([
                            ft.Text("Full Name", size=24, color="#babbc7"),
                        ], width=200,
                        ),
                        ft.ResponsiveRow([
                            ft.Column([
                                pt_textfield.Field(label="First Name", model=model.firstname, height=40, size=12)
                            ], col=6
                            ),
                            ft.Column([
                                pt_textfield.Field(label="Last Name", model=model.lastname, height=40, size=12)
                            ], col=6
                            ),
                        ], width=300
                        )
                    ], alignment=ft.MainAxisAlignment.CENTER,
                    ),

                    # USERNAME
                    ft.Row([
                        ft.Column([
                            ft.Text("Username", size=24, color="#babbc7"),
                        ], width=200,
                        ),
                        ft.Column([
                            pt_textfield.Field(label="Username", model=model.username, height=40, size=12)
                        ]),
                    ], alignment=ft.MainAxisAlignment.CENTER,
                    ),

                    # EMAIL ADDRESS
                    ft.Row([
                        ft.Column([
                            ft.Text("Email Address", size=24, color="#babbc7"),
                        ], col=6, width=200,
                        ),
                        ft.Column([
                            pt_textfield.Field(label="Email", model=model.email, height=40, size=12)
                        ]),
                    ], alignment=ft.MainAxisAlignment.CENTER,
                    ),

                    # GENDER
                    ft.Row([
                        ft.Column([
                            ft.Text("Gender", size=24, color="#babbc7"),
                        ], col=6, width=200,
                        ),
                        ft.RadioGroup(
                            content=ft.ResponsiveRow([
                                ft.Column([
                                    ft.Radio(label="Male", value="Male", fill_color={ft.MaterialState.DEFAULT: "#4c5158", ft.MaterialState.SELECTED: "#3c9fae"},)
                                ], col=6
                                ),
                                ft.Column([
                                    ft.Radio(label="Female", value="Female", fill_color={ft.MaterialState.DEFAULT: "#4c5158", ft.MaterialState.SELECTED: "#3c9fae"})
                                ], col=6
                                ),
                            ], width=300
                            ), ref=model.gender
                        )
                    ], alignment=ft.MainAxisAlignment.CENTER,
                    ),

                    # PASSWORD
                    ft.Row([
                        ft.Column([
                            ft.Text("New Password", size=24, color="#babbc7"),
                        ], col=6, width=200,
                        ),
                        ft.Column([
                            pt_textfield.Field(label="Password", model=model.password, height=40, have_password=True, size=12)
                        ]),
                    ], alignment=ft.MainAxisAlignment.CENTER,
                    ),

                    # CONFIRM PASSWORD
                    ft.Row([
                        ft.Column([
                            ft.Text("Confirm Password", size=24, color="#babbc7"),
                        ], col=6, width=200,
                        ),
                        ft.Column([
                            pt_textfield.Field(label="Confirm Password", model=model.confirm_password, height=40, have_password=True, size=12)
                        ]),
                    ], alignment=ft.MainAxisAlignment.CENTER,
                    ),

                    ft.Row([
                        pt_button.Button(text="Sign Out", on_click=controller.nav_login, btn_type="warning"),
                        pt_button.Button(text="Cancel", on_click=controller.nav_home, btn_type="secondary"),
                        pt_button.Button(text="Confirm", on_click=controller.update_user_information)
                    ], alignment=ft.MainAxisAlignment.CENTER
                    )
                    
                ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            , alignment=ft.alignment.center
            )
        ]
        super().__init__(model, view, controller)