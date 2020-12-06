import sys

print("Welcome to BeachBot, which will get you ready for next summer and long expected BEACH TIME!")
weight = float(input("Please enter your weight in kilograms: "))
height = float(input("Please enter your height in meters: "))

def bmi_index():
    return weight/(height*height)

bmi = bmi_index()
print("Your BMI is: ", "%.2f" % bmi)

print("")

def BMI_range():
    if bmi > 0 and bmi < 18.5:
       print("You are light as feather. Summer winds will blow you away.")
       sys.exit()
    elif bmi > 18.5 and bmi < 25.00:
       print("Perfect! You are ready for the beach! Have fun")
       sys.exit()
    elif bmi > 25.00 and bmi < 30.00 :
       print("You are overweight!")
    else :
       print("You are obiese")
       return ""

bmi_result = BMI_range()
print(bmi_result)

if bmi > 25.00 :
   print("I advise you doing some exercises. \nTo help you here is diary which can help you track your activities!")


def my_menu():
   
   operation = input("""
    --Select operation:--\n 
   [1] Add exercise to list\n 
   [2] Display list\n""")

   if operation == "1":
      print("Type the exercise that you would to add to your list")
      exercise = input("")
      exercise_list.append(exercise)
   elif operation == "2":
      print("You have made", len(exercise_list), "exercises.")
      print(exercise_list)
   else:
      print("You have not chosen valid operator, please run the program again ")

   again()

exercise_list = []

def num_of_exercises():
   if len(exercise_list) >= 5:
      print("Good job! Goodbye.")
   else:
      print("You could do better!")
      list_again = input("Would you like to see menu? (Y/N): ")
      if list_again.upper() == "Y":
         my_menu()
      elif list_again.upper() == "N":
         print("Goodbye!")
         sys.exit()
      

def again():
   list_again = input("Would you like to see menu? (Y/N): ")
   if list_again.upper() == "Y":
      print("So far you have made", len(exercise_list), "exercises.")
      my_menu()
   elif list_again.upper() == "N":
     print("You have made", len(exercise_list), "exercises.")
     num_of_exercises()
   else:
      again()

my_list = my_menu()



