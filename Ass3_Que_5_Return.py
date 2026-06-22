# Retrun function is used to send value to the caller.

def Division(No1,No2):
    Div = No1 / No2
    return Div

def main():
    Value1 = int(input("Enter 1st Number :"))   # Value1=20
    Value2 = int(input("Enter 2nd Number :"))   # Value2 =10
    Ret = Division(Value1,Value2)
    print("Division of two number is :" ,Ret)  # Output is 2.0
    
if __name__ =="__main__":
    main()