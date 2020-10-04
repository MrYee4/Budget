# Spencer Nettles
# CS240
# Budget will take in my income and expenses and diplay my monthly budget

#This budget class will contain all the info needed for the budget
class Budget:
    #class constructor
    def __init__(self):
        self.pay = 0
        self.income = 0
        self.mIncome = 0
        self.hours = 0
        self.rent = 0
        self.food = 0
        self.gas = 0
        self.fun = 0

    #asks user for budget data
    def getExpense(self):
        self.pay = float(input("How much do you make an hour: "))
        self.hours = float(input("How many hours do you work a week: "))
        self.income = (self.pay * self.hours)
        self.mIncome = self.income * 4
        self.rent = float(input("How much is rent per month: "))
        self.rent /= 4
        self.food = float(input("How much do you spend on food per week: "))
        self.gas = float(input("How much is gas per week: "))
        self.fun = float(input("How much do you want to spend for fun a week: "))

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
        print("Savings|", " "*(9-len(str(self.calculateSaving()))), self.calculateSaving(), "|", " "*(10-len(str(self.calculateSaving() * 4))), (self.calculateSaving() * 4), "|\n")

    #displays income to user
    def printIncome(self):
        print("weekly income: ", self.income)
        print("Monthly income: ", self.mIncome, "\n")

    #calculates how much money is left over after expenses
    def calculateSaving(self):
        self.saving = self.income - (self.rent + self.food + self.gas + self.fun)
        return self.saving




def main():
    b1 = Budget()
    b1.getExpense()
    b1.printIncome()
    b1.printBudget()

    #asks if the user wants to make another budget to allow him to make as many as he needs
    again = input("Do you want to make another bugdet(y/n): ")
    while again == "y":
        b1.getExpense()
        b1.printIncome()
        b1.printBudget()
        again = input("Do you want to make another bugdet(y/n): ")


if __name__ == "__main__":
    main()