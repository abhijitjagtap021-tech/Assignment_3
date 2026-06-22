# Function with Parameter.Parameter is a variable written in a fucnction defination.

def Multiplication(No1,No2):
    Mult = No1 * No2          # Multiplication of two numbers
    return Mult

def main():
    Value1 = int(input("Enter First Number : "))
    Value2 = int(input("Enter Second Number: "))
    Ret= Multiplication(Value1,Value2)                 
    print("Multiplcation of two numbers is : ", Ret)  # Display multiplication on console

if __name__ == "__main__":
    main()