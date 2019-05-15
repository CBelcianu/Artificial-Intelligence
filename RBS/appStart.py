from problem import Problem

print("\n\t\t\tRBS - The Washing Machine")
problem = Problem("problem.in")
texture = float(input("Enter a value for the texture:"))
capacity = float(input("Enter a value for the capacity:"))
print("\n\n")
problem.solve(texture, capacity)
