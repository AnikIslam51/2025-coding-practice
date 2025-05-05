def get_number(num):
    while True:
        operand = input("Number " + str(num) + ": ")
        try:
            return float(operand)
        except:
            print("Invalid Number, Try Again..")

operand_1 = get_number(1)
operand_2 = get_number(2)

while True:
    sign = input("Sign: ")
    if (sign == "+") or (sign == "-") or (sign == "*") or (sign == "/"):
        break
    else:
        print("Invalid Operator, Try Again..")

if sign =="+":
    result = operand_1 + operand_2
elif sign == "-":
    result = operand_1 - operand_2
elif sign == "*":
    result = operand_1 * operand_2
elif sign == "/":
    if operand_2 != 0:
        result = operand_1 / operand_2
    else:
        result = "Error!!"
    

print(result)
