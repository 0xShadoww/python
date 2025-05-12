# this is my first skill-testing calc
# lets start cooking

#INPUTS
x = int(input("Write your number for x: "));
y = int(input("Write your number for y: "));
operator = input("choose your opertor: addition or subtract or mutliply or divide ");

#calculations

if operator == "addition":
    print(x+y);
elif operator == "subtract":
    print(x-y);
elif operator == "multiply":
    print(x*y);
elif operator == "divide":
    print(x/y);
else:
    print("Choose a valid operator");