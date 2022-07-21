# Task_01
print("Task 01")

a = "reverse"   # a,b & c are string data type, showing them in reverse
b = "in"
c = "Hello"


print(c, b, a)

# Task_02
print("Task 02")
lower_case = "y"   # Python is case-sensitive example
upper_case = "Y"

if lower_case != upper_case:
    print("y and Y are not the same")

else:
    print("It's a miracle!")

# Task_03
print("Task 03")
lower_case = "Note"   # Values are compared
upper_case = "Note"

if lower_case != upper_case:
    print("Are NOT the same!")

else:
    print("Are the same.")

# Task_04
print("Task 04")
    # Checking is a user entered number is even or odd
number = int(input("Enter a number : "))
if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

# Task_05
    # We're listing all weekday & weekend tasks and showing list depending on user selection
print("Task 05")

weekday_tasks = ["Morning meeting", "Task research", "Planning", "Conference", "Budgeting"]
weekend_tasks = ["Laundry", "Vet appointment", "Pet store", "Grocery shopping", "Pay bills"]

# print("Day of week:", datetime.date.today())
weekday_tasks[0] = "Drink ColdBrew coffee"
weekday = int(input("Enter weekday day number (1-7) : "))
if weekday == 1:
    print("\nMonday tasks: ", weekday_tasks)

elif weekday == 2:
    print("\nTuesday", weekday_tasks)

elif weekday == 3:
    print("\nWednesday", weekday_tasks)

elif weekday == 4:
    print("\nThursday", weekday_tasks)

elif weekday == 5:
    print("\nFriday", weekday_tasks)

elif weekday == 6:
    print("\nSaturday", weekend_tasks)

elif weekday == 7:
    print("\nSunday", weekend_tasks)

else:
    print("\nYou have entered incorrect weekday number. Please enter weekday number between 1-7.")

# print("All weekday tasks are the following: ", weekday_tasks)
# print("And all weekend tasks are the following: ", weekend_tasks)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
