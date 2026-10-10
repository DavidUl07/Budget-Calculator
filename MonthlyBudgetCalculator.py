class BudgetCalculator(object):
    def __init__(self, income):
        self.income = income
        self.expenses = 0
        self.explist = []
    def CalcExpenses(self):
        for i in self.explist:
            self.expenses += i
        return self.expenses
    def CalculateBudget(self):
        budget = self.income - self.expenses
        return budget
    
b1 = BudgetCalculator(1000)
b1.explist = [506, 40, 45, 20]
b1.CalcExpenses()
BudgetString = str(b1.CalculateBudget()) + "€"
print(BudgetString)
