from calendar import monthrange


class Date:

    def __init__(self, d: int, m: int, y: int):
        self.day = d
        self.month = m
        self.year = y
        try:
            self.is_valid()
        except:
            raise TypeError("Invalid Date")

    def is_valid(self):
        """
        Check if input is valid
        :return: True or False
        """
        if self.year >= 0:
            if 0 <= self.month <= 12:
                if 0 <= self.day <= 31:
                    if self.month == 1 or self.month == 3 or self.month == 5 or self.month == 7 or self.month == 8 \
                            or self.month == 10 or self.month == 12:
                        return True

                    elif self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11:
                        return True

                    elif self.day == 29:
                        if self.month == 2:
                            if self.year % 4 == 0 or self.year % 400 == 0:
                                return True
                            else:
                                print("Invalid Day")
                                return False

                    else:
                        print("Invalid Day")
                        return False
                else:
                    print("Invalid Day")
                    return False
            else:
                print("Invalid Month")
                return False
        else:
            print("Invalid Year")
            return False

    def __str__(self):
        """
        This Date to str
        :return: str date
        """
        res = f"Date: {self.day}/{self.month}/{self.year}"
        return res

    def __lt__(self, other):
        """
        Check if this date before input date
        :param other: input date
        :return: True/False
        """
        if self.day < other.day and self.month <= other.month and self.year <= other.year:
            return True
        if self.month < other.month and self.year <= other.year:
            return True
        if self.year < other.year:
            return True
        else:
            return False

    def __le__(self, other):
        """
        Check if this date equal or before to input date
        :param other: Date
        :return: True/False
        """
        return self == other or self < other

    def __ge__(self, other):
        """
        Check if this date equal or after to input date
        :param other: Date
        :return: True/False
        """
        return self == other or self > other

    def __gt__(self, obj):
        """
        Check if this date after input date
        :param other: input date
        :return: True/False
        """
        if self.day > obj.day and self.month >= obj.month and self.year >= obj.year:
            return True
        if self.month > obj.month and self.year >= obj.year:
            return True
        if self.year > obj.year:
            return True
        else:
            return False

    def __eq__(self, other):
        """
        Check if this date equal to other date
        :param other: Date
        :return: True/False
        """
        if self.day == other.day and self.month == other.month and self.year == other.year:
            return True
        else:
            return False

    def __sub__(self, other):
        """
        Return date difference between two dates
        if this date before return a negative number
        :param other:input date, days count difference
        :return: days
        """
        days = 0
        d1 = Date(self.day, self.month, self.year)
        d2 = Date(other.day, other.month, other.year)

        while not d1.__eq__(d2):
            # count days
            if d1.day != d2.day:
                if d1.day > d2.day:
                    days += (d1.day - d2.day) * -1
                    d2.day = d1.day
                else:
                    days += d2.day - d1.day
                    d2.day = d1.day
            # count day in month
            elif d1.month != d2.month:
                if d1.month < d2.month:
                    days += monthrange(d2.year, d2.month)[1]
                    d2.month = d2.month - 1
                else:
                    d1.month = d1.month - 1
                    days += monthrange(d1.year, d1.month)[1] * -1
            # count days in year
            elif d1.month == d2.month and d1.year != d2.year:
                print("date1.year", d1.year, "date2.year", d2.year)
                if d1.year < d2.year:
                    d2.year = d2.year - 1
                    d2.month = 12
                else:
                    d2.year = d2.year + 1
                    d2.month = 1

        return days

    def get_next_days(self, others=1):
        """
        Add n days to this date
        1 or user cohise(input others)
        :param others: int
        :return: date + others
        """
        res = Date(self.day, self.month, self.year)
        while others > 0:
            max_day_in_month = monthrange(res.year, res.month)[1]
            if res.day + others > max_day_in_month:
                add = max_day_in_month - res.day
                res.day += add
                others -= add

            if res.day == max_day_in_month and res.month == 12:
                res.month = 1
                res.year += 1

            if res.day == max_day_in_month:
                res.month += 1
                res.day = 0

            else:
                res.day += others
                others = 0

        if others == 1:
            res.day += 1
        print(res)
        return res

    def get_next_day(self):
        res = self.get_next_days()
        print(res)
        return res

def main():
    date1 = Date(31, 12, 2020)
    date2 = Date(1, 1, 2016)
    print(date1.is_valid(), "!!!!")
    print(date1.__lt__(date2))
    print(date1.__le__(date2))
    print(date1.__ge__(date2))
    print(date1.__gt__(date2))
    print(date1.__eq__(date2))
    print(date1.__sub__(date2))
    date2.get_next_day()


if __name__ == "__main__":
    main()
