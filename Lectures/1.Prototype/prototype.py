from __future__ import annotations
import copy

'''
    We use Prototype pattern when we need to create new objects by copying
    existing objects
'''


class Component:
    def render(self):
        pass

    def clone(self) -> Component:
        pass


class Circle(Component):
    def __init__(self, radius):
        self.radius = radius

    def render(self):
        print("Rendering a circle")

    def clone(self):
        target = copy.deepcopy(self)
        return target


class ContextMenu:
    def duplicate(self, component: Component):
        new_component = component.clone()
        # Add target to the document
