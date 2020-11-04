class MyZeroDivisionError(ZeroDivisionError):
    ...


try:
    while number := int(input("Enter divider: ")):
        ...
    raise MyZeroDivisionError(number)
except MyZeroDivisionError as exc:
    print(f"My exception: {exc}")
