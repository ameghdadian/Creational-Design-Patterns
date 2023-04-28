from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from enum import Enum


class Element:
    pass


class Image(Element):
    def __init__(self, source: str):
        self.source = source

    def __str__(self):
        return self.source


class Text(Element):
    def __init__(self, content: str):
        self.content = content

    def __str__(self):
        return self.content


class ExportFormat(Enum):
    HTML = 0
    TEXT = 1
    PDF = 2


class HtmlElement:
    pass


class HtmlImage(HtmlElement):
    def __init__(self, source):
        self.source = source

    def __str__(self):
        return f"<img src=\"{self.source}\" />"


class HtmlParagraph(HtmlElement):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f"<p>{self.text}</p>"


class HtmlDocument:
    def __init__(self):
        self.elements: List[HtmlElement] = []

    def add(self, element: HtmlElement):
        self.elements.append(element)

    def __str__(self):
        builder = ''
        builder += "<html>"
        for element in self.elements:
            builder += str(element)

        builder += "</html>"
        return builder


class ElementBuilder(ABC):
    @abstractmethod
    def add_image(self, image: Image):
        pass

    @abstractmethod
    def add_text(self, text: Text):
        pass

    def get_builder(self):
        pass


# Representation
class HtmlDocumentBuilder(ElementBuilder):
    def __init__(self):
        self.document = HtmlDocument()

    def add_image(self, image: Image):
        self.document.add(HtmlImage(image.source))

    def add_text(self, text: Text):
        self.document.add(HtmlParagraph(str(text)))

    def get_builder(self):
        return self.document


# Representation
class TextBuilder(ElementBuilder):
    def __init__(self):
        self.text = ""

    def add_image(self, image: Image):
        self.text += image.source

    def add_text(self, text: Text):
        return

    def get_builder(self):
        return self.text


# Problems with previous implementation
# 1. Vioaltes Open-Closed principle
# 2. Tightly-coupled to HtmlDocument and other classes
# 3. Knows so much about their implementation/internals
# 4. Repetition in exporting logic

# Construction
class Document:
    def __init__(self):
        self.elements: List[Element] = []

    def add(self, element: Element):
        self.elements.append(element)

    def export(self, builder: ElementBuilder, filename: str):
        # construction
        content = ""

        for element in self.elements:
            if isinstance(element, Image):
                builder.add_image(element)
            if isinstance(element, Text):
                builder.add_text(element)

        content = str(builder.get_builder())
        with open(filename, 'w') as file:
            file.write(content)


def main():
    document = Document()
    document.add(Text("Hello world"))
    document.add(Image("pic1.jpg"))

    document.export(HtmlDocumentBuilder(), "export.html")

    # Only writes the text elements to the file
    document.export(TextBuilder(), "export.txt")


if __name__ == '__main__':
    main()
