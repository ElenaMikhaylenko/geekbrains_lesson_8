import task5


EQUIPMENT_TYPES = {"printer": task5.Printer, "scanner": task5.Scanner, "xerox": task5.Xerox}


def add(storage):
    name = filtered_input("Name: ")
    if name not in EQUIPMENT_TYPES:
        print(f"Unknown type: {name}")
        return
    count = get_int("Count: ")
    task5.add_equipment(storage, *[EQUIPMENT_TYPES[name]() for _ in range(count)])
    print("Successful")


def get(storage):
    name = filtered_input("Name: ")
    count = get_int("Count: ")
    try:
        print(task5.get_equipment_to_department(storage, name, count))
        print("Successful")
    except Exception as exc:
        print(exc)


def info(storage):
    for k, v in storage.info().items():
        print(f"{k}: {len(v)}")


def filtered_input(message):
    return input(message).strip().lower()


def get_int(message):
    while not (element := filtered_input(message)).isdigit():
        print(f"Must be int. Got: {element}")
    return int(element)


def main():
    commands = {"add": add, "get": get, "info": info}
    storage = task5.Storage()
    task5.add_equipment(storage, task5.Printer(), task5.Printer(), task5.Xerox(), task5.Printer(), task5.Scanner())
    print(f"Commands: {', '.join(commands.keys())}")
    while (command := filtered_input("Command: ")) != "exit":
        method = commands.get(command)
        if method is not None:
            method(storage)
        else:
            print(f"Unexpected command. Expected: {', '.join(commands.keys())}")


if __name__ == '__main__':
    main()
