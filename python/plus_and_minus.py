number = int(input("vedi: "))
number_2 = int(input("vedi: "))

choose = input("vedi | +, -, *, / | : ")

if choose == "+":
    result = number + number_2
elif choose == "-":
    result = number - number_2
if choose == "*":
    result = number * number_2
elif choose == "/":
    result = number / number_2

print(f"vash result {result}")























