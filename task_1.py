from pulp import LpMaximize, LpProblem, LpVariable, lpSum, value

model = LpProblem("Maximize_Total_Production", LpMaximize)

lemonade = LpVariable("Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

model += lpSum([lemonade, fruit_juice]), "Total_Production"

model += 2 * lemonade + 1 * fruit_juice <= 100
model += 1 * lemonade <= 50
model += 1 * lemonade <= 30
model += 2 * fruit_juice <= 40

model.solve()

total_production = value(model.objective)

print(f"Максимальна кількість вироблених продуктів: {int(total_production)}")
