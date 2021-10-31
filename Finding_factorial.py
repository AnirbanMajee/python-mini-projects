# Calculate the factorial of given number  and  Find the number of trailing zeros in that factroial


"""num = int(input("enter a number : "))
factorial = 1

for i in range(1, num+1):
    factorial = factorial * i
    
print(f"the factorial of {num} is {factorial}")"""

def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number *factorial(number - 1)
def factorialTrailingZeroes(number):
    count = 0 
    i = 5
    while (number // i != 0):
        count += int(number / i )
        i = i*5
        return count
    
if __name__ == '__main__':
    number = int(input("Enter a number : "))    
    print(factorialTrailingZeroes(number))
    