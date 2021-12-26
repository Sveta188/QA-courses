class Investment:

    def __init__(self, invest):
        self.sum_of_investment = invest[0]
        self.period_of_investment = invest[1]


class Banking(Investment):

    def deposit(self):
        sum_of_investment = self.sum_of_investment
        period_of_investment = self.period_of_investment * 12
        percent = 0.1 / 12
        print(percent)
        periodical_result = 1.0 + percent
        result_of_pow = pow(periodical_result, period_of_investment)
        result = sum_of_investment * result_of_pow
        return round(result, 2)


investment = [350000, 1]
investment_end = Banking(investment)
print(investment_end.deposit())
