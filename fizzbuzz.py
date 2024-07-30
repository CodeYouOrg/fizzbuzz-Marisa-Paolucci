for number in range(1,101): 
 list1 = ''
 
 if number % 3 == 0:
    list1 = list1 + "Fizz"
 
 if number % 5 == 0:
    list1 = list1 + "Buzz"
 
 if number % 5 != 0 and number % 3 != 0:
    list1 = list1 + str(number)
 
 print(list1)

# first line creates a for loop the variable number and the range is 1-100 (have to put 101 to include 100).
# first if statement checks to see if the number is divisible by 3. If so, "Fizz" is added. Second if statement checks to see if the number is divisible by 5. If so, "Buzz" is added. Third if statement checks to see if the number is divisible by 5 and 3. If so, FizzBuzz is added.
# last line prints the list. 