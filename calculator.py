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
        
if __name__=="__main__":
    # initializing calculator object
    calc=Calculator()

    #Infinite loop to get input from user until specified otherwise
    while True:
        
        print()
        print("Select the option:")
        print("1. Addition")
        opt=input()
        print()

        if opt=="1":
            print("------------------------------------------------------------")
            print("Enter the numbers you want to add with spaces in between: ")
            number_string=input()
            print("Sum = ",calc.add(number_string))
            print("------------------------------------------------------------")
        else:
            print("Please select a valid option.")
