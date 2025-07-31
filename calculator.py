# CREATING A SIMPLE CALCULATOR PROGRAM
# CREATING A VARIABLES THAT STORE THE USER'S INPUT AFTER PROMPT
first_number = float(input("Please enter the first number: ")) #ACCEPTING FIRST NUMBER
second_number = float(input("Please enter the second number: ")) #ACCEPTING SECOND NUMBER
operator = str(input("Please enter your operator(Either +,-,/,*): "))
# CREATING A LIST OF OPERATORS
operators = ["+","-","/","*"]

# CREATING FUNCTION TO CARRY OUT THE OPERATIONS BASED ON THE USER'S OPERATOR
def calculator():
    # CREATING A CHECK FOR OPERATORS
    if operator not in operators:
        return f"No valid operator!"

    elif operator in operators and operator == "+":
        result = first_number + second_number
        return f"Your sum is {result}"
    
    elif operator in operators and operator == "-":
        result = first_number - second_number
        return f"Your difference is {result}"
    
    elif operator in operators and operator == "*":
        result = first_number * second_number
        return f"Your product is {result}"
    
    elif operator in operators and operator == "/":
        if second_number == 0:
            return f"Division by zero is not possible!"
        else:
            result = first_number / second_number
            return f"Your sum is {result}"
        
print(calculator())