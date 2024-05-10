import flet as ft

class Field(ft.TextField):
    def __init__(self, label:str, model, height=50, have_password=False, value="", size=14 ):
        super().__init__(
            label=label, 
            border_color="#16181b", 
            fill_color="#1e2125", 
            height=height, 
            ref=model,
            can_reveal_password=have_password,
            password=have_password,
            text_size=size,
            value=value
        )
