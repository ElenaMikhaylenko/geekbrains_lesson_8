class NotNumeric(Exception):
    ...


result = []
while (el := input("Введите элемент: ")) != "stop":
    try:
        if not el.isdigit():
            raise NotNumeric(el)
    except NotNumeric as exc:
        print(f"{exc} - не число.")
        continue
    result.append(el)
print(result)
