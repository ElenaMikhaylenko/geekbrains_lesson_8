class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def extract_from_str(cls, date, delimiter="-"):
        return cls(*map(int, date.split(delimiter)))

    @staticmethod
    def validate_date(date):
        if not isinstance(date.day, int) or not (1 <= date.day <= 31):
            raise Exception(f"Invalid day")
        if not isinstance(date.month, int) or not (1 <= date.month <= 12):
            raise Exception(f"Invalid month")
        if not isinstance(date.year, int):
            raise Exception(f"Invalid year")

    def __repr__(self):
        return f"Date(day={self.day}, month={self.month}, year={self.year})"


def main():
    date = Date(1, 2, 3)
    Date.validate_date(date)
    date = Date.extract_from_str("01-11-2020")
    Date.validate_date(date)
    print(date)
    Date.validate_date(Date(-1, -2, -3))


if __name__ == '__main__':
    main()
