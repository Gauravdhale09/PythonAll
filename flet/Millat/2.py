import flet
from flet import *
from functools import partial
import time


class NavBar(UserControl):
    def __init__(self):
        super().__init__()

    def highlight(self, e):
        if e.data == 'true':
            e.control.bgcolor = 'white10'
            e.control.update()
            e.control.content.controls[0].icon_color = 'white'
            e.control.content.controls[0].color = 'white'
            e.control.update()

        else:
            e.control.bgcolor = None
            e.control.update()
            e.control.content.controls[0].icon_color = 'white54'
            e.control.content.controls[0].color = 'white54'
            e.control.update()

    def head(self):
        return Container(
            content=Row(
                spacing=0,
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    Text(
                        'Millat.',
                        size=30,
                        font_family='Josefin Sans',
                        weight=FontWeight.BOLD,

                    ),
                    Text(
                        'AI',
                        size=30,
                        weight=FontWeight.W_900,
                        color=colors.BLUE_900,
                    )
                ]
            )
        )

    def user(self, initials: str, name: str, description: str):
        return Container(
            content=Row(
                controls=[
                    Container(
                        width=50,
                        height=50,
                        alignment=alignment.center,
                        bgcolor='bluegrey900',
                        border_radius=8,
                        content=Text(
                            value=initials,
                            size=20,
                            weight='bold',
                        )
                    ),
                    Column(
                        spacing=1,
                        alignment='center',
                        controls=[
                            Text(
                                value=name,
                                size=20,
                                weight='bold',
                                opacity=1,
                                animate_opacity=200,

                            ),
                            Text(
                                value=description,
                                size=15,
                                weight='w400',
                                color='white54',
                                opacity=1,
                                animate_opacity=200,

                            ),
                        ]
                    )
                ]
            )
        )
    def search_bar(self, icon):
        return Container(
            height=45,
            border_radius=10,
            on_hover=lambda em: self.highlight(em),

            content=Row(
                controls=[
                    IconButton(
                        icon=icon,
                        icon_size=20,
                        icon_color='white54',
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=7)
                            },
                        )
                    ),
                    TextField(
                        hint_text='Search',
                        border_color='transparent',
                        content_padding=padding.only(right=10, bottom=10, left=0, top=10),
                        hint_style=TextStyle(
                            bgcolor='transparent',
                            color='white',
                            size=20,
                        ),
                    )

                ]
            ),
        )
    def pri(self, e):
        pass
    def _content_icon(self, icon_name: str, text_name: str):
        return Container(
            height=45,
            border_radius=10,
            on_click=lambda e: self.pri(e),
            on_hover=lambda em: self.highlight(em),
            content=Row(
                controls=[
                    IconButton(
                        icon=icon_name,
                        icon_size=20,
                        icon_color='white54',
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=7)
                            },
                        )
                    ),
                    Text(
                        value=text_name,
                        size=20,
                        opacity=1,
                        animate_opacity=200,
                    )

                ]
            ),
        )

    def build(self):
        return Container(
            width=300,
            padding=15,
            height=630,
            bgcolor='black',
            border_radius=10,
            animate=animation.Animation(500, 'decelerate'),
            content=Column(
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment='center',
                controls=[
                    self.head(),
                    Divider(height=15, color='white54'),
                    # sidebar icons
                    self.user("GRD", 'Gaurav Dhale', 'student'),
                    Divider(height=5, color='transparent'),
                    self.search_bar(icons.SEARCH),
                    self._content_icon(icons.PERSON_ROUNDED, 'HR'),
                    self._content_icon(icons.PUBLISH, 'Purchasing'),
                    self._content_icon(icons.INVENTORY, 'Inventory Control'),
                    self._content_icon(icons.ENGINEERING_ROUNDED, 'Engineering'),
                    self._content_icon(icons.DOCUMENT_SCANNER, 'Legal'),
                    Divider(height=5, color='white54'),
                    self._content_icon(icons.LOGOUT, 'Logout'),
                ]
            )

        )


class MainContent(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return Container(
            width=1000,
            height=630,
            bgcolor='black',
            border_radius=10,
            content=None,
        )


def main(page: flet.Page):
    page.title = 'Millat.AI/Home'
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.add(
        Container(
            width=1340,
            height=650,
            padding=padding.all(30),
            content=Container(
                Row(
                    spacing=10,
                    controls=[
                        NavBar(),
                        MainContent(),
                    ]

                ),
            ),

        )
    )
    page.update()


if __name__ == '__main__':
    try:
        flet.app(target=main, view=AppView.WEB_BROWSER)
    except Exception as e:
        print(e)
