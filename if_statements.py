# control flow with if statements

# weather = "overcast"
#
# if weather == 'sunny':  # if statement returns True, execute next line
#     print("Get in a beer garden")
# elif weather == 'overcast':  # if statement returns True, execute next line
#     print("Take a coat, just in case")
# elif weather != 'sunny':
#     print('Wait for the sun to come out')
# else:  # otherwise print next line
#     print("Grab an umbrella")

age = int(input("Please enter your age as a number: "))
if age >= 18:  # if age is more more than/ equal to 18, print
    print('You can watch this 18+ movie, please proceed to check-out')
elif age >= 16:  # if age is more more than/ equal to 16, print
    print('You can watch this 16+ movie, please proceed to check-out')
elif age >= 12:  # if age is more more than/ equal to 12, print
    print('You can watch this 12+ movie, please proceed to check-out')
elif 12 > age >= 0:  # if age is less than 12 and more than/ equal to 0, print
    print('You can watch any PG and U movie, please proceed to check-out')
else:
    print('Please input a valid age')
