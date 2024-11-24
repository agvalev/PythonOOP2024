from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    MONEY_NEED = 1_000_000

    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < self.MONEY_NEED:
            raise ValueError(f"F1 is an expensive sport, find more sponsors!")
        self.__budget = value
    @property
    @abstractmethod
    def team_data(self):
        pass



    def calculate_revenue_after_race(self, race_pos):
        expenses, sponsors = self.team_data
        revenue = 0

        for sponsor in sponsors.values():
            for position, money in sponsor.items():
                if race_pos <= position:
                    revenue += money
                    break

        revenue -= expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"


