#code starts of here 
class Calculator:
    def add(self, num_string):
        '''Add method to return the sum of all numbers in the string'''
        sum=0
        try:
            for i in num_string.split(" "):
                sum+=int(i)
            return sum
        except ValueError:
            return "Please enter valid integers with spaces in between"
    
    def divide(self,num,den):
        '''Divide method to perform division of two numbers'''
        if den == 0:
            return "Denominator cannot be 0"
        else:
            return num/den

if __name__=="__main__":
    # initializing calculator object  in the code
    calc=Calculator()

    #Infinite loop to get input from user until specified otherwise to get desired result 
    while True:
        
        print()
        print("Select the option:")
        print("1. Addition\n2. Division\n3.Exit")
        opt=input()
        print()

        if opt=="1":
            print("------------------------------------------------------------")
            print("Enter the numbers you want to add with spaces in between: ")
            number_string=input()
            print("Sum = ",calc.add(number_string))
            print("------------------------------------------------------------")
        elif opt == "2":
            print("------------------------------------------------------------")
            try:
                num=int(input("Enter the numerator: "))
                den=int(input("Enter the denominator: "))
                print(f'{num}/{den} = ',calc.divide(num,den))
            except ValueError:
                print("Please enter an integer")
            print("------------------------------------------------------------")
        elif opt == "3":
            print("--------------------------------------------------------------")
            break
        else:
            print("Please select a valid option.")

        

