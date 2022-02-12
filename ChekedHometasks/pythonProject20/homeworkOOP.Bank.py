class Investment:

    def __init__(self, invest):
        self.sum_of_investment = invest[0]
        self.period_of_investment = invest[1]


class Bank(Investment):

    def __init__(self, invest):
        super().__init__(invest)

    def deposit(self):
        sum_of_investment = self.sum_of_investment
        period_of_investment = self.period_of_investment * 12
        percent = 0.1 / 12
        print(percent)
        periodical_result = 1.0 + percent
        p = pow(periodical_result, period_of_investment)
        result = sum_of_investment * p
        return round(result, 2)


investment = [350000, 1]
investment_end = Bank(investment)
print(investment_end.deposit())
