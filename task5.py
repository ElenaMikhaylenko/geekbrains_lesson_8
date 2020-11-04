from task4 import Storage, Printer, Scanner, Xerox


def add_equipment(storage, *equipments):
    for equipment in equipments:
        storage.add_equipment(equipment)


def get_equipment_to_department(storage, name, count):
    equipments = storage.get_equipment(name, count)
    if len(equipments) != count:
        for equipment in equipments:
            storage.add_equipment(equipment)
        raise Exception(f"Can't get {name}. Needed: {count}, current: {len(equipments)}")
    return equipments


def main():
    storage = Storage()
    add_equipment(storage, Printer(), Printer(), Xerox(), Printer(), Scanner())
    print(storage.info())
    print(get_equipment_to_department(storage, "printer", 2))
    print(storage.info())
    print(get_equipment_to_department(storage, "printer", 4))


if __name__ == '__main__':
    main()
