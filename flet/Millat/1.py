import flet as ft
from flet import *
from math import pi
import time

cred_list = []


class SignInButton(UserControl):
    def __init__(self, btn_name):
        super().__init__()
        self.btn_name = btn_name

    def get_btn_name(self):
        print(cred_list)

    def build(self):
        return Container(
            content=ElevatedButton(
                content=Text(
                    self.btn_name,
                    size=20,
                    weight='bold',
                ),
                style=ButtonStyle(
                    shape={
                        "": RoundedRectangleBorder(radius=8)
                    },
                    color={
                        "": "black"
                    },
                    bgcolor={"": '#7df6dd'}
                ),
                height=50,
                width=500,
                on_click=self.btn_name
            )
        )


class Animation_box(UserControl):
    def __init__(self, border_color, bg_color, rotate_angle):
        self.border_color = border_color
        self.bg_color = bg_color
        self.rotate_angle = rotate_angle
        super().__init__()

    def build(self):
        return Container(
            width=48,
            height=48,
            content=Row(
                alignment='center',
                controls=[
                    Text("M", size=30)
                ]
            ),
            border=border.all(2.5, self.border_color),
            bgcolor=self.bg_color,
            border_radius=2,
            rotate=transform.Rotate(self.rotate_angle, alignment.center),
            animate_rotation=animation.Animation(700, 'easeInOut'),
        )


class User(UserControl):
    def __init__(self, icon_name, placeholder, hide):
        super().__init__()
        self.icon_name = icon_name
        self.placeholder = placeholder
        self.hide = hide
        self.text = ''

    def on_text(self, data):
        self.text = data
        print("appended")
        cred_list.append(self.text)

    def build(self):
        return Container(
            width=500,
            height=40,
            border=border.only(bottom=border.BorderSide(0.5, 'white54')),
            content=Row(
                spacing=20,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Icon(
                        name=self.icon_name,
                        size=40,
                        opacity=0.5,
                    ),
                    TextField(
                        border_color='transparent',
                        bgcolor='transparent',
                        height=30,
                        width=440,
                        text_size=20,
                        content_padding=5,
                        cursor_color='white',
                        hint_text=self.placeholder,
                        hint_style=TextStyle(size=20),
                        password=self.hide,
                        on_change=self.on_text,
                        can_reveal_password=True,
                        on_blur=None,
                    ),
                ]
            )
        )


def main(page: ft.Page):
    page.title = "Millat.AI"
    # dimensions
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.bgcolor = '#1f262f',

    def on_button_click1(e):
        card_sign_in.transform = "rotateY(180deg)"
        card_sign_up.transform = "rotateY(0deg)"
        page.update()

    def on_button_click2(e):
        card_sign_up.transform = "rotateY(180deg)"
        card_sign_in.transform = "rotateY(0deg)"
        page.update()

    card_sign_in = Card(
        width=850,
        height=600,
        elevation=10,
        content=Container(
            bgcolor='#23262a',
            border_radius=6,
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Divider(height=2, color='transparent'),
                    Row(
                        alignment=MainAxisAlignment.END,
                        controls=[
                            ElevatedButton(text='Go to Sign Up', icon=icons.ARROW_RIGHT, elevation=0, bgcolor='#23262a',
                                           on_click=on_button_click1)
                        ]
                    ),
                    Divider(height=2, color='transparent'),
                    Stack(
                        controls=[
                            Animation_box('#7df6dd', '#23262a', pi / 4),
                            Animation_box('#e9665a', '#23262a', 0),
                        ]
                    ),
                    Divider(height=20, color='transparent'),
                    Column(
                        alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        spacing=5,
                        controls=[
                            Text('Sign In', size=22, weight='bold'),
                            Divider(height=10, color='transparent'),
                            Text('Welcome to Millat.AI, please Login to proceed', size=15, weight='bold'),

                        ]
                    ),

                    Divider(height=30, color='transparent'),
                    User(icons.PERSON_ROUNDED, 'xyz123@gmail.com', False),
                    Divider(height=50, color='transparent'),
                    User(icons.LOCK_ROUNDED, 'password', True),
                    Divider(height=1, color='transparent'),

                    Row(
                        spacing=125,
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            ElevatedButton(
                                content=Text(
                                    'new user? Go to SignUp!',
                                    size=17,
                                ),
                                elevation=10,
                                bgcolor='transparent',
                            ),
                            ElevatedButton(

                                content=Text(
                                    'Forgot Password?',
                                    size=17,
                                ),
                                elevation=10,
                                bgcolor='transparent',
                            )
                        ]
                    ),
                    Divider(height=10, color='transparent'),
                    SignInButton("Sign In")
                ]
            )
        )
    )
    card_sign_up = Card(
        width=850,
        height=600,
        elevation=10,
    )
    page.add(
        card_sign_in
    )
    page.update()


if __name__ == '__main__':
    ft.app(target=main, view=AppView.WEB_BROWSER)


ft.app(target=main)
