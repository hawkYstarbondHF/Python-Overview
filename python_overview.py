"""Assignment that provides an overview of basic features
   of the Python programming language.                 
 
   This code will be executed by running the following commands from the console:
   python python_overview.py
  
   I recommend using either VSCode or GitHub codespaces to work on this code,     
   but you should make sure that it behaves as expected when executed as described above. 

   You are expected to complete all exercises according          
   to the specifications. Do not change the names or headers
   for any existing functions. You may add new functions, and
   will specifically be required to for some exercises. 
   Absolutely all functions in this file must have complete
   PEP 257 style docstring comments, including specification of
   return values and parameters. Additional documentation           
   is required within function bodies as appropriate. Some
   function stubs currently return a dummy result to allow
   execution, but you will need to replace these with
   proper return values. Whenever console output is required,
   all formatting must match the specification exactly.
   
   author = Jacob Schrum, Last modified 6/11/2023
   author = Eleanor Wagner, ADD DATE
   
   DO NOT IMPORT ANY MODULES! USE ONLY STANDARD PYTHON FEATURES
"""

def main():
    """Launches code for all exercises. Do not change."""
    print_divider(1)
    exercise1()
    print_divider(2)
    exercise2()
    print_divider(3)
    exercise3()                         
    print_divider(4)
    exercise4()
    print_divider(5)
    exercise5()
    print_divider(6)
    exercise6()

def print_divider(exercise_number):  
    """Prints a dividing line between each exercise.

    Parameters:
    exercise_number -- Problem number printed in output
    """
    print("--Exercise {}----------------------------------".format(exercise_number))

#################################################################

def exercise1():
    """Exercise 1: Loops         
       6 points functionality, 4 points documentation 
    
       Write code inside of this function that computes the sum of all numbers between
       200 and 1287 inclusive that are divisible by 13. You will both print your result,
       AND return it directly from the function. The format of your printed output should
       be a single line with carriage return, and look like the following:
   
       The sum is: XXX
	   
       where XXX is the resulting sum.
       
       Return:           
       Computed sum
    """
    # https://www.w3schools.com/python/python_for_loops.asp
    sum = 200 + 13-(200%13)
    for x in range(sum+13, 1288, 13): # 1287+1 because range is non-inclusive
        sum += x
    
    print("The sum is: {}".format(sum))
    return sum

#################################################################

def first_longer_shorter(first, second):
    # https://www.w3schools.com/python/ref_exception_valueerror.asp XXX
    # https://www.digitalocean.com/community/tutorials/python-valueerror-exception-handling-examples
    if first is None or second is None or len(first) == 0 or len(second) == 0:
        raise ValueError
    
    str = ""
    if(len(first) >= len(second)):
        str = first[0] + second[0]
    else:           
        str = second[0] + first[0]
    
    return str

def exercise2():
    """Exercise 2: Strings
       6 points functionality, 7 points documentation
      
       Define a method called "first_longer_shorter" that takes
       two String parameters that each have at least one
       character. Raise a ValueError if this precondition 
       is not satisfied. This method will return a String 
       consisting of exactly two characters: The first character 
       of the longer String, followed by the first character of 
       the shorter String. If both Strings have equal length, 
       then the first character of the first String parameter 
       should come first in the result.
      
       After defining your function, uncomment the test calls
       below which call your function. Note that your function
       must work for any valid input, not just for these
       examples.
    """
    print(first_longer_shorter("Hello","Bye"))
    print(first_longer_shorter("Bye","Hello"))
    print(first_longer_shorter("1","abc"))
    print(first_longer_shorter("abc","1"))
    print(first_longer_shorter("abc","123"))
    print(first_longer_shorter("123","abc"))                

#################################################################

def move_to_end(list, index):
    x = 0
    temp = list[index]
    for x in range(index, len(list)-1):
        list[x] = list[x+1]
    
    list[len(list)-1] = temp;

def exercise3():
    """Exercise 3: Lists
       8 points functionality, 7 points documentation
      
       Define a method called "move_to_end" that takes a list of integers
       and an index within that list. Modify the list so the item at the 
       designated index is now at the end of the list, and items at later 
       indices are now shifted one position to the left. All items originally
       in the list are still present.
       
       Test your method by completing the code below. This code should
       create an int list called one_to_ten containing 1, 2, ..., 10 in
       order, and then send it to your move_to_end method with an index 
       of 4. Afterward, print the contents of one_to_ten to the console 
       on a single line with a carriage return at the end, and a comma 
       and space between each entry. The result should look like the following:
      
       1, 2, 3, 4, 6, 7, 8, 9, 10, 5

    """
    # testing array
    one_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # method call
    move_to_end(one_to_ten, 4)
    
    # 
    result = ""
    count = 0

    # 
    for x in one_to_ten:
        result += str(x)
        if(count < len(one_to_ten)-1):
            result += ", "
        count += 1
    
    print(result)

#################################################################

def exercise4():
    """Exercise 4: Recursion
       10 points functionality, 6 points documentation
       
       Define a sequence in the following way. The first three
       numbers are 1, 2, and 3. Every subsequent number is the sum of
       the previous number, and the number two entries before that
       one. So, the first few numbers in the sequence are:
       F(0) = 1
       F(1) = 2                
       F(2) = 3
       F(3) = 1+3 = 4
       F(4) = 2+4 = 6
       
       This sequence is similar to, but different from the Fibonacci
       sequence. You will write two functions defining this sequence.
       One uses pure recursion, the other uses dynamic programming.
       Note that your dynamic programming solution should not use 
       recursion at all. This is not a strict requirement of dynamic 
       programming, but it is a requirement of this assignment.
       
       The function stubs for each approach are provided below. Once they
       are complete, you can uncomment the code in this function to test
       them. Note that these functions should raise ValueErrors
       for inappropriate inputs.
    """
    # TODO: Uncomment to test your completed functions.
    #       Turn in your code with these lines uncommented. 
    print(recursive_seq(5))
    print(dynamic_seq(5))
    print(recursive_seq(8))
    print(dynamic_seq(8))
    print(recursive_seq(15))
    print(dynamic_seq(15))

def recursive_seq(n):
    """Recursively compute the sequence described in the comment for
       exercise 4.

       Parameters:
       n -- Position in the sequence
       Return: 
       n-th value in the sequence
    """
    if n < 0:
        raise ValueError()
    if(n <= 2):
        return n + 1
    
    return recursive_seq(n-3) + recursive_seq(n-1) # TODO: Change this

def dynamic_seq(n):
    """Compute the sequence described in the comment for
       exercise 4 using dynamic programming. This will require
       the use of an auxiliary list. DO NOT USE RECURSION!

       Parameters:
       n -- Position in the sequence
       Return: 
       n-th value in the sequence
    """
    # parameter handling
    if n < 0:
        raise ValueError()
    
    # https://www.w3schools.com/python/python_lists_loop.asp#:~:text=Looping%20Using%20List%20Comprehension
    # since you can't declare a list of a certain size in python, this fills it with -1
    # auxiliary list
    list = [-1 for x in range(n)]
    
    # base cases
    if n <= 2:
        return n+1
    else:
        # replace all items in list with proper values
        for x in range(len(list)):
            if x <= 2: # base cases
                list[x] = x+1
            else:
                list[x] = list[x-3] + list[x-1]
    
    return list[n-3] + list[n-1] # n-th value


#################################################################

def exercise5():
    """Exercise 5: File I/O
       10 points functionality, 6 points documentation
      
       This function should read from the file "numbers.txt" which
       contains only integers, exactly one per line. The function should
       compute and print the maximum and average of the numbers in the file.
       The maximum should be formatted as an int, but the average should be
       formatted as a float (compute a floating point average). The output
       will consist of exactly two lines, each followed by a carriage return.
       Here is an example:                    
       
       Maximum value: XXX
       Average value: XXX
       
       where the XXX portions will be replaced with actual values calculated
       from the file. Note that your code must work for arbitrary input files,
       not just the provided example. However, you can assume the file is
       named "numbers.txt". If a file with this name does not exist, then
       do not crash with an exception. Instead, print the error message below
       followed by a carriage return:
       
       The file "numbers.txt" does not exist. Exiting.
       
    """
    try:
        # https://www.w3schools.com/python/python_file_handling.asp
        f = open("numbers.txt")
        
        sum = float(f.readline())
        max = int(sum)
        count = 1
        
        for line in f:
            # difficulties with casting to int, so all lines are floats
            temp = float(line)
            if temp > max:
                max = int(temp)
            sum += temp
            count += 1
        f.close()

        print("Maximum value: {}".format(max))
        print("Average value: {}".format(sum/count))
    except FileNotFoundError:
        print("The file \"numbers.txt\" does not exist. Exiting.")
#################################################################

def exercise6():
    """Exercise 6: Classes
       10 points functionality, 10 points documentation
       
       Implement a class inside of this method called "Employee"
       that is defined in the following way:
       - An instance variable defining how much
         the employee is paid per hour.
       - An instance variable defining the number
         of worked hours that the employee has not been paid for yet.
       - A constructor that defines the hourly rate and sets worked
         hours to 0.
       - A method called "work" with an int parameter that increases
         the number of worked but unpaid hours by the specified number.
       - A method called "get_unpaid_hours" that returns the number of
         worked but unpaid hours.
       - A method "pay" that resets the unpaid worked hours to 0 and
         returns a floating point number which is the amount the 
         employee should be paid for the worked hours (multiply 
         the rate by the hours).
    """
    class Employee:
        """TODO: Descriptive comment."""
        def __init__(self, x):
            self.rate = x
            self.hours = 0
        
        """TODO: Descriptive comment."""
        def work(self, x):
            self.hours += x
        
        """TODO: Descriptive comment."""
        def get_unpaid_hours(self):
            return self.hours
        
        """TODO: Descriptive comment."""
        def pay(self):
            paycheck = float(self.rate * self.hours)
            self.hours = 0
            return paycheck


        
        # TODO: Define the class as described above.

    # TODO: Uncomment to test your completed class.
    #       Turn in your code with these lines uncommented. 
    e1 = Employee(8.25)
    e1.work(8)
    e1.work(8)
    e1.work(8)
    e1.work(8)
    e1.work(8)
    hours1 = e1.get_unpaid_hours()
    paycheck1 = e1.pay()
    print("Employee 1 earns ${:,.2f} for {} hours of work.".format(paycheck1,hours1))
    e1.work(10)
    e1.work(8)
    e1.work(8)
    hours2 = e1.get_unpaid_hours()
    paycheck2 = e1.pay()
    print("Employee 1 earns ${:,.2f} for {} hours of work.".format(paycheck2,hours2))

    e2 = Employee(15.10)
    e2.work(8)
    e2.work(10)
    e2.work(10)
    e2.work(6)
    e2.work(6)
    hours3 = e2.get_unpaid_hours()
    paycheck3 = e2.pay()
    print("Employee 2 earns ${:,.2f} for {} hours of work.".format(paycheck3,hours3))

#################################################################

if __name__ == "__main__":                
    # execute only if run as a script
    main()