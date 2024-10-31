spisak = []

while True:

    a = int(input("vedi: "))
    spisak.append(a)
    if a == 0:
        del spisak[-1]
        break

user_input = input("vedie: ")

if user_input == "+":
    a = sum(spisak)

if user_input == "-":
    

print(spisak)
print(a)






































