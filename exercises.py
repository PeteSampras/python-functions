
#A function is a block of code (a series of instructions) designed to execute a certain task. Functions allow you to reuse code.
 
#Below are some specifications for Functions to be built.

#1 
#Declare two variables box_1 and box_2 and assign any number value of your choosing. These two variables will be used to invoke functions #2 - #5.
box_1 = 4
box_2 = 5

#2
#Function - add
#Create a function named `add` which will take two parameters: `num_1` and `num_2`.
def add(num_1,num_2):
    sum1 = num_1 + num_2
    return sum1

#This function will add two numbers (the parameters, `num_1` and `num_2`) and return the sum of these two numbers. Invoke the function and assign it to a variable named `sum`.
sum=add(box_1,box_2)
#Print the sum variable to see your result.

print(sum)

#3
#Function - subtract
#Create a function named `subtract` which will take two parameters: `num_1` and `num_2`.
def subtract(num_1,num_2):
    return num_1-num_2

#This function will subtract two numbers and return the difference of these two numbers. Invoke the function and assign it to a variable named `difference`.
difference = subtract(box_1,box_2)

#Print the difference variable to see your result.
print(difference)

#4
# Function - multiply
#Create a function named `multiply` which will take two parameters: `num_1` and `num_2`.
def multiply(num_1,num_2):
    return num_1*num_2
#This function will multiply two numbers and return the product of these two numbers. Invoke the function and assign it to a variable named `product`.
product = multiply(box_1,box_2)
#Print the product variable to see your result.
print(product)

#5
#Function - divide
#Create a function named `divide` which will take two parameters: `num_1` and `num_2`.
#This function will divide two numbers and return the quotient of these two numbers. Invoke the function and assign it to a variable named `quotient`.
def divide(num_1,num_2):
    return num_1-num_2
quotient = divide(box_1,box_2)
#Print the quotient variable to see your result.
print(quotient)

#6
#Function - check_sum
#Create a function named `check_sum` which will take a parameter: `x`.
#This function will return the string "Mariah Carey has been married `x` amount of times." Where `x` is the value stored in the sum variable from exercise 2. Invoke this function and assign it to a variable named `da_diva`.
def check_sum(value):
    return "Mariah Carey has been married " + str(value) + " times."
#Print the da_diva variable to see your result.
print(check_sum(sum))


#7
#Function - check_difference
#Create a function named `check_difference` which will take a parameter `x`.
def check_difference(x):
    return "Last night I dreamt that I ate " + str(x) + " Big Macs."
#This function will return the string "Last night I dreamt that I ate `x` Big Macs."  Where `x` is the value stored in the difference variable from exercise 3. Invoke this function and assign it to a variable named `loving_it`
loving_it=check_difference(difference)

#Print the loving_it variable to see your result.
print(loving_it)


#8
#Function - check_product
#Create a function named `check_product` which does not require any parameters.
def check_product():
    return sum * product

#This function will multiply the values stored in the sum and product variables. Invoke this function and print your result.
print(check_product())

#9
#Function - check_quotient
#Create a function named `check_quotient` which does not require any parameters.
def check_quotient():
    return product/quotient
#This function will multiply the values stored in the product and quotient variables. Invoke this function and print your result.
print(check_quotient())

#10
#Function - create_full_name
#Create a function named create_full_name which takes two parameters: `first_name`, `last_name`.
def create_full_name(first_name,last_name):
    return first_name + " " + last_name
#This function will return a string which represents someone's full name. Invoke this function by passing in your first and last name into the function. Store the return value into a variable named `my_full_name`.
my_full_name=create_full_name("Matt","Gluck")
#Print the my_full_name variable to see your result.
print(my_full_name)






