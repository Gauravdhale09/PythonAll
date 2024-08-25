import flet as f


def main(page: f.Page):
    page.title = "Calculator"
    page.update()


if __name__ == '__main__':
    f.app(target=main)
import flet as ft


def main(page: ft.Page):
    page.title = "Test Page"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    txt = ft.Text(
        value="Hello, World!",
        text_size=20,
        text_align=ft.TextAlign.CENTER,
        width=200,
        height=50,
        autofocus=True
    )
    page.add(
        ft.Row(
            [txt],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    ft.app(target=main)


import flet as ft


def main(page: ft.Page):
    def route_change(e: ft.RouteChangeEvent):
        page.add(ft.Text(f"New route: {e.route}"))

    def go_store(e):
        page.route = "/store"

    page.on_route_change = route_change
    page.add(ft.ElevatedButton("Go to Store", on_click=go_store))


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
import flet
from flet import Page, Text


def main(page: Page):
    page.add(Text("Hello, world!"))


flet.app(target=main, assets_dir="assets", view=flet.WEB_BROWSER)

import flet as ft


def main(page: ft.Page):
    def btn_click(e):
        print(txt_name.value)

    txt_name = ft.TextField(label="Your name")
    page.add(txt_name, ft.ElevatedButton("Print to console", on_click=btn_click))


ft.app(target=main)

from flet import App, Text, Password, Button, Checkbox, on

app = App(title="Login Page")


@app.route("/")
def login():
    return [
        Text("Username"),
        Text(value="", placeholder="Enter Username"),
        Text("Password"),
        Password(value="", placeholder="Enter Password", show_toggle=True),
        Checkbox("Remember me"),
        Button("Login", on_click=on('login'))
    ]


@app.on('login')
def on_login(data):
    print(f"User logged in with data: {data}")


app.run()

from flet import TextField, app, Page


def main(page: Page):
    page.add(
        TextField(
            label="Password with reveal button",
            password=True,
            can_reveal_password=True
        )
    )


app(target=main)
import flet as ft


def main(page: ft.Page):
    page.title = "Flet Button Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def button_click(e):
        print("Hello")

    page.add(
        ft.Row(
            [
                ft.TextButton("Button 1", on_click=button_click, hover_color=ft.Colors.BLUE),
                ft.Spacer(width=20),
                ft.TextButton("Button 2", on_click=button_click, hover_color=ft.Colors.BLUE),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(main)

import flet as ft


def main(page: ft.Page):
    page.title = "Test App"
    page.window_width = 200
    page.window_height = 200

    def on_hover(e):
        e.control.bgcolor = "#404050" if e.data == "true" else "#DBE09D"
        e.control.text = "Hovering" if e.data == "true" else "Not Hovering"
        e.control.update()

    page.add(
        ft.ElevatedButton(text="Hover over me", on_hover=on_hover),
    )


ft.app(target=main)

import flet as ft
from routes.login import LoginPage
from routes.register import RegisterPage
from routes.home import HomePage
from routes.user_profile import UserProfilePage


class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.routes = {
            "/login": LoginPage(page),
            "/register": RegisterPage(page),
            "/": HomePage(page),
            "/:username": UserProfilePage(page)
        }
        self.body = ft.Container(content=self.routes["/login"])

    def change_route(self, event: ft.RouteChangeEvent):
        self.body.content = self.routes[event.route]
        self.body.content.init_page()
        self.page.update()


import flet as ft


def main(page: ft.Page):
    page.title = "Card with Button Example"

    def on_button_click(e):
        print("Button clicked!")

    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Spacer(),
                                ft.ElevatedButton("Button", on_click=on_button_click)
                            ]
                        ),
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("The Enchanted Nightingale"),
                            subtitle=ft.Text("Music by Julie Gable. Lyrics by Sidney Stein."),
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )
    )


ft.app(target=main)

import flet as ft


def main(page: ft.Page):
    page.title = "Rotating Card Example"

    card1 = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.ALBUM),
                        title=ft.Text("The Enchanted Nightingale"),
                        subtitle=ft.Text("Music by Julie Gable. Lyrics by Sidney Stein."),
                    ),
                ]
            ),
            width=400,
            padding=10,
        )
    )

    card2 = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.ALBUM),
                        title=ft.Text("The Enchanted Nightingale"),
                        subtitle=ft.Text("Music by Julie Gable. Lyrics by Sidney Stein."),
                    ),
                ]
            ),
            width=400,
            padding=10,
        )
    )

    def on_button_click1(e):
        card1.transform = "rotateY(180deg)"
        card2.transform = "rotateY(0deg)"
        page.update()

    def on_button_click2(e):
        card2.transform = "rotateY(180deg)"
        card1.transform = "rotateY(0deg)"
        page.update()

    page.add(card1)
    page.add(ft.ElevatedButton("Rotate Card 1", on_click=on_button_click1))
    page.add(card2)
    page.add(ft.ElevatedButton("Rotate Card 2", on_click=on_button_click2))


ft.app(target=main)

import flet as ft


class UsernameField(ft.TextField):
    def __init__(self):
        super().__init__(placeholder="Username")


class PasswordField(ft.TextField):
    def __init__(self):
        super().__init__(placeholder="Password", obscure_text=True)


class SignInButton(ft.RaisedButton):
    def __init__(self, username_field, password_field):
        super().__init__("Sign In", on_click=self.on_click)
        self.username_field = username_field
        self.password_field = password_field

    def on_click(self, e):
        print(f"Username: {self.username_field.value}")
        print(f"Password: {self.password_field.value}")


def main(page: ft.Page):
    page.title = "Flet Sign In Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    username_field = UsernameField()
    password_field = PasswordField()
    sign_in_button = SignInButton(username_field, password_field)

    page.add(
        ft.Column(
            [
                username_field,
                password_field,
                sign_in_button
            ]
        )
    )


ft.run(main)
class User(UserControl):
    def __init__(self, icon_name, placeholder, hide):
        super().__init__()
        self.icon_name = icon_name
        self.placeholder = placeholder
        self.hide = hide
        self.text = ''  # Add this line

    def on_text_change(self, text):  # Add this method
        self.text = text


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
                        on_change=self.on_text_change,  # Modify this line
                        can_reveal_password=True,
                        on_blur=None,
                    ),
                ]
            )
        )
import flet as ft

def main(page: ft.Page):
    def pick_files_result(e: ft.FilePickerResultEvent):
        if e.files:
            upload_list = []
            for f in e.files:
                upload_list.append(ft.FilePickerUploadFile(f.name, upload_url=page.get_upload_url(f.name, 600)))
            file_picker.upload(upload_list)

    file_picker = ft.FilePicker(file_type=ft.FilePickerFileType.IMAGE, on_result=pick_files_result)
    page.overlay.append(file_picker)

    page.add(ft.ElevatedButton("Pick and upload images", icon=ft.icons.UPLOAD))

import flet as fl

def main():
    app = fl.App()

    @app.route('/')
    def home():
        return fl.Upload(on_upload=on_upload)

    @fl.action
    def on_upload(file):
        return fl.Text(f'You uploaded: {file.name}')

    app.run()

if __name__ == '__main__':
    main()

import os
from flet import App, FileUpload

app = App()


@app.route("/")
def home():
    return """
    <h1>Image Upload</h1>
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="image">
        <input type="submit" value="Upload">
    </form>
    """


@app.route("/", methods=["post"])
def upload_image():
    image = FileUpload("image")

    if not os.path.exists('images_dir'):
        os.makedirs('images_dir')

    image.save(f"images_dir/{image.filename}")

    return f"<h1>Image {image.filename} uploaded successfully!</h1>"


if __name__ == "__main__":
    app.run()

import flet as ft

def main(page: ft.Page):
    # Create a TextField for user input
    name_text = ft.TextField(label="Your Name")

    # Create a Text control for displaying messages
    message_text = ft.Text(value="")

    # Create a button
    def button_clicked(e):
        # Check if the TextField is empty
        if name_text.value == "":
            # Display an error message
            message_text.value = "Error: Please enter your name."
            message_text.color = ft.colors.RED
        else:
            # Display a success message
            message_text.value = "Success: Your name is " + name_text.value + "."
            message_text.color = ft.colors.GREEN

        # Update the page to reflect the changes
        page.update()

    submit_button = ft.ElevatedButton(text="Submit", on_click=button_clicked)

    # Add the controls to the page
    page.add(name_text, submit_button, message_text)

ft.app(target=main, view=ft.WEB_BROWSER)
