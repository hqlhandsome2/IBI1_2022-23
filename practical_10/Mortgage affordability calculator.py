# buy_house is the name of the function, (value, salary) are the parameters of the function. These are the values that you pass to the function when calling it. In this case, value represents the total value of the house and salary represents the purchaser’s annual salary.
def buy_house(value, salary):
    # Check if the value of the house is less than or equal to 5 times the purchaser's salary
    if value <= 5 * salary:
        # If it is, return 'Yes' indicating that the purchaser can buy the house
        return 'Yes'
    else:
        # Otherwise, return 'No' indicating that the purchaser cannot buy the house
       return 'No'

# The example
value = 180000
salary = 35000
result = buy_house(value, salary)
print(result) # Answer is "NO"

# Input of value and salary
value = int(input("value of the house:"))
salary = int(input("your annual salary:"))
result = buy_house(value, salary)
print(result)
