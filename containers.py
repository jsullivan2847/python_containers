
# Exercise 1
# Create a list named studentscontaining some student names (strings).
# Print out the second student's name.
# Print out the last student's name.





students = ['henry', 'samantha', 'eli', 'lily', 'summer']
# print(students[1])
# print(students[-1])






# Exercise 2
# Create a tuple named foodscontaining the same number of foods (strings) as there are names in the studentslist.
# Use a forloop to print out the string "food goes here is a good food".

foods = ('pizza', 'hotdog', 'french-fry', 'pea soup', 'ramen')
# for food in foods:
#     print(f'{food} is a good food')





# Exercise 3
# Using a forloop, print just the last two food strings from foods.

for index, food in enumerate(foods):
    if index == 3 or index == 4: 
        print(food)
    


# Exercise 4
# Create a dictionary named home_towncontaining the keys of city, stateand population.
# Print a string with this format:
# "I was born in city, state - population of population"

home_town = {
    'city': 'Grand Rapids',
    'state': 'Michigan',
    'population': 250000,
}

# print(f'''I was born in 
# {home_town["city"]}, {home_town["state"]} - population of {home_town["population"]}''')

# Exercise 5
# Iterate over the key: value pairs in home_town

# for key, value in home_town.items():
#     print(f'{key} : {value}')

# Exercise 6
# Create an empty list named cohort.
# Using a forloop, add one dictionary to the cohortlist for each student name. Each dictionary should have this shape:

cohort = []

for index, student in enumerate(students):
    cohort.append({
        'student': student,
        'fav_food': foods[index],
    })

# print(cohort)

# Exercise 7
# Using the list of studentsb and list comprehension, assign to a variable named awesome_studentsa new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over awesome_students printing out each string.


awesome_students = [f'{student} is awesome!' for student in students]
# print(awesome_students)


# Exercise 8
# Using the tuple foods and list comprehension within a forloop, print each food string that contains the letter a.

# for food in foods:
#     if('a' in food):
#         print(food)

# new_food = [food for food in foods if 'a' in food]

# print(new_food)





   











    