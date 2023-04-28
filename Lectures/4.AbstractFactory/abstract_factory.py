from __future__ import annotations
from enum import Enum

'''
    Abstract Factory pattern provides an interface
    for creating families of related objects.
'''


class Widget:
    def __init__(self):
        self.render()

    def render(self):
        pass


# Abstract Factory(interfac)
class WidgetFactory:
    def create_button(self) -> Button:
        pass

    def create_textbox(self) -> TextBox:
        pass


class Button(Widget):
    def render(self):
        pass


class TextBox(Widget):
    def render(self):
        pass


class MaterialWidgetFactory(WidgetFactory):
    def create_button(self) -> Button:
        return MaterialButton()

    def create_textbox(self) -> TextBox:
        return MaterialTextBox()


class AntWidgetFactory(WidgetFactory):
    def create_button(self) -> Button:
        return AntButton()

    def create_textbox(self) -> TextBox:
        return AntTextBox()


class MaterialButton(Button):
    def render(self):
        print("Material button")


class MaterialTextBox(TextBox):
    def render(self):
        print("Material TextBox")


class AntButton(Button):
    def render(self):
        print("Ant button")


class AntTextBox(TextBox):
    def render(self):
        print("Ant TextBox")


class Theme(Enum):
    MATERIAL = 0
    ANT = 1


class ContactForm:
    def render(self, factory: WidgetFactory):
        factory.create_textbox()
        factory.create_button()


def main():
    ContactForm().render(MaterialWidgetFactory())


if __name__ == '__main__':
    main()
