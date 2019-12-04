def prime(num):
    """ 
    Return: 
        True if number is prime.
        False if number is not prime. 
    
    Implementation: 
        Loops through the numbers 2 - 9 
        Uses modulo to check if the number returns a remainder. 
            Remainder = not divisible 
            No Remainder = divisible 
        Checks if current number is not the input number.  t 
    """

    for number in range(2, 10): 
        if (num % number == 0) & (num != number):
           return False
    return True 

user_input = input("Welcome to Is It Prime? \nEnter a number: "); 
print(f"{user_input} is prime!" if prime(int(user_input)) else f"{user_input} is not prime.")

