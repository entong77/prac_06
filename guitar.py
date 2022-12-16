from datetime import date
current_date = date.today()
current_year = current_date.year


class Guitar:
    """Store values for guitar class"""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50