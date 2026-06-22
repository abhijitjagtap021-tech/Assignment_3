# Display Data Type , Memory Address and Memory size allocation

from sys import getsizeof

def main():
    X = 10
    print(type(X))            #Output <class 'int'>
    print(id(X))              #Output 140707774580120
    print(getsizeof(X))       #Output 28

if __name__ == "__main__":
    main()

