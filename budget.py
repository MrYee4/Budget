# Spencer Nettles
# CS240
# Budget will take in my income and expenses and diplay my monthly budget


class Budget:
    def __init__(self, income, rent, food, gas, fun):
        self.income = income
        self.mIncome = 4 * income
        self.rent = rent
        self.food = food
        self.gas = gas

    def printBudget(self):
        print("")

    def printIncome(self):
        print("weekly income: ", self.income)
        print("Monthly income: ", self.mIncome)




def main():
    pay = float(input("How much do you make an hour: "))
    hours = float(input("How many hours do you work a week: "))
    income = (pay * hours)
    rent = float(input("How much is rent per month: "))
    rent /= 4
    food = float(input("How much do you spend on food per week: "))
    gas = float(input("How much is gas per week: "))
    fun = float(input("How much do you want to spend for fun a week: "))

    b1 = Budget(income, rent, food, gas, fun)
    b1.printIncome()


if __name__ == "__main__":
    main()