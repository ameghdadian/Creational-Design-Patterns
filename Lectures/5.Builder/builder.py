from __future__ import annotations
from enum import Enum
from typing import List
'''
    We use Builder pattern to separate the construction
    of an object from its representation.
'''


class Slide:
    def __init__(self, text) -> None:
        self.text = text


class PresentationFormat(Enum):
    PDF = 0
    IMAGE = 1
    POWERPOINT = 2
    MOVIE = 3


'''
 Problems with current implementation
 1. Violates Open-Closed principle
 2. Tight-coupling between Presentation and classes
    like PdfDocument, Movie etc, as we support more
    presentation format, our coupling increases.
 3. Our Presentation class should have the knowledge
    of the these classes(i.e., Movie etc), for example
    it knows that a PdfDocument has pages, or Movie has
    frames.
 4. Repetition in our exporting logic.
class Presentation:
    def __init__(self):
        self.slides: List[Slide] = []

    def add_slide(self, slide: Slide):
        self.slides.append(slide)

    def export(self, format: PresentationFormat):
        if format == PresentationFormat.PDF:
            pdf = PdfDocument()
            for slide in self.slides:
                pdf.add_page(slide.text)
        elif format == PresentationFormat.MOVIE:
            movie = Movie()
            for slide in self.slides:
                movie.add_frame(slide.text, 3)
'''


class PresentationBuilder:
    def add_slide(self, slide: Slide):
        pass


# Representation
class PdfDocumentBuilder(PresentationBuilder):
    def __init__(self) -> None:
        self.document = PdfDocument()

    def add_slide(self, slide: Slide):
        self.document.add_page(slide.text)

    def get_pdf_document(self):
        return self.document


# Representation
class MovieBuilder(PresentationBuilder):
    def __init__(self) -> None:
        self.movie = Movie()

    def add_slide(self, slide: Slide):
        self.movie.add_frame(slide.text, 3)

    def get_movie(self):
        return self.movie


# Construction
class Presentation:
    def __init__(self) -> None:
        self.slides: List[Slide] = []

    def add_slide(self, slide: Slide):
        self.slides.append(slide)

    def export(self, builder: PresentationBuilder):
        # construction
        builder.add_slide(Slide("Copyright"))
        for slide in self.slides:
            builder.add_slide(slide)


class PdfDocument:
    def add_page(self, text: str):
        print("Adding a page to PDF.")


class Movie:
    def add_frame(self, text: str, duration: int):
        print("Adding a frame to the movie")


def main():
    presentation = Presentation()
    presentation.add_slide(Slide("Slide 1"))
    presentation.add_slide(Slide("Slide 2"))

    builder = MovieBuilder()
    presentation.export(builder)
    movie = builder.get_movie()


if __name__ == '__main__':
    main()
