# Prompt user to enter tow numbers 
num1 = int(input("Please Enter number 1: "))
num2 = int(input("Please Enter number 2: "))

print("\n===== The Result Arithmetic Operations =====\n")
# Add num1 and num2,
sum_result = num1 + num2
# Subtract num2 form num1
diff_result = num2 - num1
# Multiplay num1 and num2 
mul_result = num1 * num2
# Divid num1 by num2
div_result = format (num1 / num2)

arithmetic_operations_result = f"- Sum {num1} and {num2} is: {sum_result} \n - Subtract {num2} from {num1} is: {diff_result} \n - Multiplay {num1} by {num2} is: {mul_result} \n - Divid {num1} by {num2} is: {div_result} "
print(arithmetic_operations_result)

# Check if number1 is grater than number2 
print("\n===== The Grater Number =====\n")
if num1 > num2: 
    print(f" The Number 1: ({num1}) is grater then Number 2: ({num2})")
else: 
    print(f" The Number 2: ({num2}) is grater than Number 1: ({num1}) ")

# Chek of sum oepration even or odd 
print("\n===== Check Even Or Odd For Sum Operation =====\n")
if (sum_result % 2) == 0: 
    print(f"* Result of sum operatin ({sum_result}) is: Odd  ")
else:
    print(f"* Result of sum operatin ({sum_result}) is: Even  ")

# Compare betwen number 1 and number 2 
print("\n===== Compare Result =====\n")
if num1 == num2:
    print(f"* Number 1: ({num1}) is equal Number 2: ({num2})")
elif num1 > num2: 
    print(f"* Number 1: ({num1}) is grater than Number 2: ({num2})")
else:
    print(f"* Number 2: ({num2}) is grater than Number 1: ({num1})")
