from typing import List
from copy import deepcopy
from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def clone(self):
        pass


class Audio(Component):
    def __init__(self, bitrate):
        self.bitrate = bitrate

    def clone(self):
        print("Cloning Audio")
        target = deepcopy(self)
        return target


class Clip(Component):
    def __init__(self, duration):
        self.duration = duration

    def clone(self):
        print("Cloning a Clip")
        target = deepcopy(self)
        return target


class Text(Component):
    def __init__(self, value):
        self.value = value

    def clone(self):
        print("Cloning a Text")
        target = deepcopy(self)
        return target


class Timeline:
    def __init__(self):
        self.component: List[Component] = []

    def add(self, component: Component):
        self.component.append(component)


# Menu that opens up by right-clicking!
class ContextMenu:
    def duplicate(self, component: Component):
        return component.clone()


def main():
    timeline = Timeline()
    menu = ContextMenu()
    text = Text("Cool programmer")
    clip = Clip(10)
    clip2 = clip.clone()
    text2 = text.clone()

    timeline.add(text)
    timeline.add(clip)
    timeline.add(clip2)
    timeline.add(text2)

    clip3 = menu.duplicate(clip)


if __name__ == '__main__':
    main()
