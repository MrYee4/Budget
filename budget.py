# Spencer Nettles
# CS240
# Budget will take in my income and expenses and diplay my monthly budget

#This budget class will contain all the info needed for the budget
class Budget:
    #class constructor
    def __init__(self, income, rent, food, gas, fun):
        self.income = income
        self.mIncome = 4 * income
        self.rent = rent
        self.food = food
        self.gas = gas
        self.fun = fun

    #Will print out budget in a table
    def printBudget(self):
        print("       |   Weekly   |   Monthly   |")
        print("-------|------------|-------------|")
        print("Income |", " "*(9-len(str(self.income))), self.income, "|", " "*(10-len(str(self.mIncome))), self.mIncome, "|")
        print("-------|------------|-------------|")
        print("Rent   |", " "*(9-len(str(self.rent))), self.rent, "|", " "*(10-len(str(self.rent * 4))), self.rent * 4, "|")
        print("Food   |", " "*(9-len(str(self.food))), self.food, "|", " "*(10-len(str(self.food * 4))), self.food * 4, "|")
        print("Gas    |", " "*(9-len(str(self.gas))), self.gas, "|", " "*(10-len(str(self.gas * 4))), self.gas * 4, "|")
        print("Fun    |", " "*(9-len(str(self.fun))), self.fun, "|", " "*(10-len(str(self.fun * 4))), self.fun * 4, "|")
        print("-------|------------|-------------|")
        print("Savings|", " "*(9-len(str(self.calculateSaving()))), self.calculateSaving(), "|", " "*(10-len(str(self.calculateSaving() * 4))), (self.calculateSaving() * 4), "|")

    #displays income to user
    def printIncome(self):
        print("weekly income: ", self.income)
        print("Monthly income: ", self.mIncome)

    #calculates how much money is left over after expenses
    def calculateSaving(self):
        self.saving = self.income - (self.rent + self.food + self.gas + self.fun)
        return self.saving




def main():
    #asks user for budget values
    pay = float(input("How much do you make an hour: "))
    hours = float(input("How many hours do you work a week: "))
    income = (pay * hours)
    rent = float(input("How much is rent per month: "))
    rent /= 4
    food = float(input("How much do you spend on food per week: "))
    gas = float(input("How much is gas per week: "))
    fun = float(input("How much do you want to spend for fun a week: "))

    #budget object
    b1 = Budget(income, rent, food, gas, fun)
    b1.printIncome()
    print("")
    b1.printBudget()


if __name__ == "__main__":
    main()