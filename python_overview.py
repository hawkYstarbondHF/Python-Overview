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
   author = Eleanor Wagner, 09/12/2024
   
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
    # Loop in increment via range(): 
    # https://www.geeksforgeeks.org/specifying-the-increment-in-for-loops-in-python/
    
    sum = 0 # sum to be computed

    # 208 is the next divisible by 13 number starting at 200, + 1 to ensure
    # 1287 is included, increment by 13
    for i in range(208, 1287 + 1, 13): 
        sum += i
    print("The sum is:", sum) # print sum

    return sum 

#################################################################

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


def first_longer_shorter(first, second):
    """Raising ValueError: 
       https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python
       
       Takes two strings and returns the first character of each based on 
	   string length. The longer string first, followed by the shorter string
	   If the strings are the same length, the first String parameter is first. 
       
       Raises a ValueError if either parameter isn't a string, is None, or
       is less than 1 character.
       
       Parameters:
       first -- first string to check
       second -- second string to check
       Return:
       string of 2 characters
    """
    # ensuring parameter strings have at least 1 character
    if first is None or second is None or len(first) == 0 or len(second) == 0:
        raise ValueError();
    
    string = "" # string to be returned
    
    # determine which string is longer to be added first
    if len(first) >= len(second): # first is longer/the same
        string += first[0]
        string += second[0]
    else: # second is longer, add second to str first
        string += second[0]
        string += first[0]

    return string

#################################################################

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
    # Printing:
    # https://stackoverflow.com/questions/33905032/how-to-print-on-the-same-line-in-python#:~:text=use%20the%20end%20argument%20in%20the%20print%20function

    one_to_ten = [1,2,3,4,5,6,7,8,9,10] # array to be used

    move_to_end(one_to_ten, 4) # call to helper method

    for i in one_to_ten: # prints properly formatted array
        # last element shouldn't have commas
        if i == one_to_ten[-1]: 
            print(i) # no comma + carriage
        else:
            print(i, end = ", ")


def move_to_end(list, x):
    """This method takes a list and rearranges it so that the element
       at the given index is moved to the end and the others are shifted to 
       the left.
       
       Parameters:
       list -- integer list to be rearranged
       x -- the index of the elemnt to be moved
    """
    temp = list[x] # the list element to be moved

    # starts at the element to be moved's index
    for i in range(x,len(list)-1):
        list[i] = list[i+1] # overwrite indicies to the left

    list[-1] = temp # add temp to end

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
    # ensure appropriate input
    if n < 0: 
        raise ValueError()

    # base cases of indices 0, 1, and 2
    if n <= 2: 
        return n+1
    else: # recursive call and addition
        return recursive_seq(n-3) + recursive_seq(n-1) # returns n-th value

def dynamic_seq(n):
    """Compute the sequence described in the comment for
       exercise 4 using dynamic programming. This will require
       the use of an auxiliary list. DO NOT USE RECURSION!

       Parameters:
       n -- Position in the sequence
       Return: 
       n-th value in the sequence
    """
    # ensure appropriate input
    if n < 0:
        raise ValueError()
    
    # auxiliary list
    list = [] 
   
    if n < 3: # 3 base cases
        return n+1
    else:
        # fill in auxiliary list
        for i in range(n+1):
            if i < 3:  # first are the 3 base cases
                list.append(i+1)
            else:
                # assign sum of previous element with the 2 before it
                list.append(list[i-3] + list[i-1])
    
    return list[n] # returns n-th value


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
    # Error Catching:
    # https://pythonbasics.org/try-except/
    # File Handling:
    # https://www.geeksforgeeks.org/how-to-read-from-a-file-in-python/#
    try:
        # open file to read
        file = open("numbers.txt", "r")

        #start max & sum off with the first value from the file
        max = int(file.readline()) # convert String to int
        sum = float(max) # convert to double
        line_num = 1 # track to calculate average

        # loop through file
        for line in file:
            temp = int(line) # newest integer
            if temp > max: # check against max
                max = temp
            
            sum += temp # add to sum
            line_num += 1 # increment
        
        file.close() # close file

        # print results according to format
        print("Maximum value:", max)
        print("Average value:", sum/line_num)

    except FileNotFoundError: # exception & message specified above
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
        """Class for keeping track of employees, their respective salaray,
           number of hours worked, and whether they have been paid for each hour.
        """
        
        """Constructor to initialize employee, define their salary, and 
           sets their number of hours worked to 0.

           Parameters:
           x -- this employee's salary ($ per hour)
        """
        def __init__(self, x):
            self.salary = x
            self.unpaid_hours = 0

        """This method updates the number of unpaid hours by the amount passed
           in.

           Parameters:
           hours -- number of hours worked
        """
        def work(self, hours):
            self.unpaid_hours += hours
        
        """ Returns the number of unpaid hours.

            Return:
            number of hours
        """
        def get_unpaid_hours(self):
            return self.unpaid_hours
        
        """This method pays all of the currently unpaid hours according to
		   the employee's salary. Then it resets the number of unpaid hours 
		   to 0.

           Return:
           integer of the employee's paycheck
        """
        def pay(self):
            paycheck = self.salary * self.unpaid_hours
            self.unpaid_hours = 0
            return paycheck

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
