from copy import deepcopy
from collections import defaultdict


class Storage:
    def __init__(self):
        self._storage = defaultdict(list)

    def info(self):
        return deepcopy(self._storage)

    def add_equipment(self, equipment):
        self._storage[str(equipment)].append(equipment)

    def get_equipment(self, name, count):
        result = []
        if name in self._storage:
            equipments = self._storage[name]
            for _ in range(count):
                if not equipments:
                    break
                result.append(equipments.pop(0))
        return result


class OfficeEquipment:

    def __init__(self):
        self._state = "off"

    def on(self):
        self._state = "on"

    def off(self):
        self._state = "off"

    def state(self):
        return self._state

    def __repr__(self):
        return f"{type(self).__name__}()"

    def __str__(self):
        return type(self).__name__.lower()


class Printer(OfficeEquipment):

    class Cartridge:
        ...

    def __init__(self):
        super().__init__()
        self.cartridge = None

    def set_cartridge(self, cartridge):
        self.cartridge = cartridge

    def print(self, text):
        ...


class Scanner(OfficeEquipment):

    def scan(self, document):
        return str(document)


class Xerox(Printer, Scanner):

    def copy(self, document):
        self.print(self.scan(document))
