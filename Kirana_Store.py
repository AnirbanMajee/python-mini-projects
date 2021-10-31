# Write a program which will keep adding a stream of number enter by the user. The adding will be stop as soon as user press the 'q' button.

sum = 0
while (True):
    userInput = input("Enter product price and press 'q' to quit : ")
    if (userInput != 'q'):
        sum += int(userInput)
        print(f"Your order total so far : {sum}")
    else:
        print(
            f"Your total bill is {sum}, thanks for shopping from our store 😊")
        break
