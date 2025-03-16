def func1():
    print("this will be executed")
    print("function to perform printing of tables")
def input_value():
    a=int(input("Enter the value of the table to be printed:"))

    for i in range(0,11):
        print(a,"x",i,"=", a*i)

if __name__== "__main__":
 func1()
 input_value()
