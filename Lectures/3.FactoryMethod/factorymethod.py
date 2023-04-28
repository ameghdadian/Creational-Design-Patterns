from typing import Mapping
from abc import ABC, abstractmethod


'''
    Defer the creation of an object to subclasses.
    Factory Method pattern relies on inheritance and polymorphism
'''


class ViewEngine(ABC):
    @abstractmethod
    def render(self, viewname, context):
        pass


class MatchaViewEngine(ViewEngine):
    def render(self, viewname: str, context: Mapping[str, object]) -> str:
        return "View rendered by Matcha"


class SharpViewEngine(ViewEngine):
    def render(self, viewname, context):
        print("View rendered by Sharp")


class Controller:
    def render(self, viewname, context: Mapping[str, object]):
        engine = self._create_view_engine()
        html = engine.render(viewname, context)
        print(html)

    def _create_view_engine(self) -> ViewEngine:
        return MatchaViewEngine()


class SharpController(Controller):
    def _create_view_engine(self) -> ViewEngine:
        return SharpViewEngine()


# We can substitue the inherited class to get different View Engine!
class ProductsController(SharpController):
    def list_products(self):
        # Get products from database
        context: Mapping[str, object] = {}
        # context[..] = products
        self.render("products.html", context)
