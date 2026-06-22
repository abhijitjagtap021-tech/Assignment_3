# User Defined Function created by programmer by using def function. If program start from def then it is user defined function.

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