import flet as ft
from flet import (
    WEB_BROWSER,
    Column,
    Container,
    ElevatedButton,
    Page,
    Row,
    Text,
    UserControl,
    border_radius,
    TextStyle,
    colors,
    TextAlign,
    AppView,
    TextField
)


class Calculator(UserControl):

    def build(self):
        self.reset()
        self.result = Text(value='0', color=colors.WHITE, size=50)
        self.txt = TextField(bgcolor=colors.WHITE, visible=True, border_radius=border_radius.all(40), width=500, text_size=20, color=colors.BLACK, text_style=TextStyle(weight=ft.FontWeight.BOLD, font_family='Lato'))
        return Container(
            width=600,
            height=650,
            bgcolor=colors.BLACK,
            border_radius=border_radius.all(20),
            padding=50,
            content=Column(
                controls=[
                    Row(controls=[Text(value='My Calculator', color=colors.WHITE, size=60)],
                        alignment=ft.MainAxisAlignment.CENTER),
                    Row(controls=[self.result], alignment='end'),
                    Row(controls=[self.txt], alignment='end'),
                    Row(
                        controls=[
                            ElevatedButton(
                                content=Text("AC", size=30),
                                height=60,
                                bgcolor=colors.WHITE,
                                color=colors.PURPLE_900,
                                expand=1,
                                on_click=self.button_clicked,
                                data='AC',
                            ),
                            ElevatedButton(
                                content=Text("🔙", size=30),
                                height=60,
                                bgcolor=colors.WHITE,
                                color=colors.PURPLE_900,
                                expand=1,
                                on_click=self.back,
                                data='BACK',
                            ),
                            ElevatedButton(
                                content=Text("+/-", size=30),
                                height=60,
                                bgcolor=colors.WHITE,
                                color=colors.PURPLE_900,
                                expand=1,
                                on_click=self.button_clicked,
                                data='+/-',
                            ),
                            ElevatedButton(
                                content=Text("➗", size=30),
                                height=60,
                                bgcolor=colors.WHITE,
                                color=colors.PURPLE_900,
                                expand=1,
                                on_click=self.button_clicked,
                                data='➗',
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                content=Text("7", size=30),
                                height=60,
                                bgcolor=colors.BLACK,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data='7',
                            ),
                            ElevatedButton(
                                content=Text("8", size=30),
                                height=60,
                                bgcolor=colors.BLACK,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data='8',
                            ),
                            ElevatedButton(
                                content=Text("9", size=30),
                                height=60,
                                bgcolor=colors.BLACK,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data='9',
                            ),
                            ElevatedButton(
                                content=Text("✖️", size=30),
                                height=60,
                                bgcolor=colors.WHITE,
                                color=colors.PURPLE_900,
                                expand=1,
                                on_click=self.button_clicked,
                                data='✖️',
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                content=Text("4", size=30),
                                height=60,
                                bgcolor=colors.BLACK,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data='4',
                            ),
                            ElevatedButton(
                                content=Text("5", size=30),
                                height=60,
                                bgcolor=colors.BLACK,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data='5',
                            ),
                            ElevatedButton(
                                content=Text("6", size=30),
                                height=60,
                                bgcolor=colors.BLACK,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data='6',
                            ),
                            ElevatedButton(
                                content=Text("-", size=30),
                                height=60,
                                bgcolor=colors.WHITE,
                                color=colors.PURPLE_900,
                                expand=1,
                                on_click=self.button_clicked,
                                data='-',
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                content=Text("1", size=30),
                                height=60,
                                bgcolor=colors.BLACK,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data='1',
                            ),
                            ElevatedButton(
                                content=Text("2", size=30),
                                height=60,
                                bgcolor=colors.BLACK,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data='2',
                            ),
                            ElevatedButton(
                                content=Text("3", size=30),
                                height=60,
                                bgcolor=colors.BLACK,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data='3',
                            ),
                            ElevatedButton(
                                content=Text("+", size=30),
                                height=60,
                                bgcolor=colors.WHITE,
                                color=colors.PURPLE_900,
                                expand=1,
                                on_click=self.button_clicked,
                                data='+',
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                content=Text("%", size=30),
                                height=60,
                                bgcolor=colors.BLACK,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data='%',
                            ),
                            ElevatedButton(
                                content=Text("0", size=30),
                                height=60,
                                bgcolor=colors.BLACK,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data='0',
                            ),
                            ElevatedButton(
                                content=Text(".", size=30),
                                height=60,
                                bgcolor=colors.BLACK,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data='.',
                            ),
                            ElevatedButton(
                                content=Text("=", size=30),
                                height=60,
                                bgcolor=colors.BLUE,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data='=',
                            ),
                        ]
                    ),
                ]
            )
        )

    def back(self, e):
        data = self.result.value[:-1]
        return data

    def button_clicked(self, e):
        data = e.control.data
        if self.result.value == "Error" or data == "AC":
            self.result.value = "0"
            self.reset()

        elif data in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.'):
            if self.result.value == '0' or self.new_operand == True:
                self.result.value = data
                self.new_operand = False
            else:
                self.result.value += data
        elif data in ('+', '-', '✖️', '➗'):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.operator = data
            if self.result.value == "Error":
                self.operand1 = '0'
            else:
                self.operand1 = float(self.result.value)
            self.new_operand = True
        elif data in ('='):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.reset()
        elif data in ('%'):
            self.result.value = float(self.result.value) / 100
            self.reset()

        elif data in ('+/-'):
            if float(self.result.value) > 0:
                self.result.value = '-' + str(self.result.value)
            elif float(self.result.value) < 0:
                self.result.value = str(
                    self.format_number(abs(float(self.result.value)))
                )

        elif data in ('🔙'):
            self.result.value = self.result.value[:-1]
            return self.result.value
        self.update()

    def format_number(self, num):
        if num % 1 == 0:
            return int(num)
        else:
            return num

    def calculate(self, operand1, operand2, operator):
        if operator == '+':
            return self.format_number(operand1 + operand2)
        elif operator == '-':
            return self.format_number(operand1 - operand2)
        elif operator == '✖️':
            return self.format_number(operand1 * operand2)
        elif operator == '➗':
            if operand2 != 0:
                return self.format_number(operand1 / operand2)
            else:
                return "Error"

    def reset(self):
        self.operator = '+'
        self.operand1 = 0
        self.new_operand = True


def main(page: ft.Page):
    page.title = "Calculator"
    page.vertical_alignment = 'center',
    page.horizontal_alignment = 'center',
    cal = Calculator()
    page.add(cal)


if __name__ == '__main__':
    ft.app(target=main, view=AppView.WEB_BROWSER, assets_dir='assets')
