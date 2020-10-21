#Lists in Lists, Accessing nested lists

#people = [["Darren", "Raines", 31], ["Joi", "Raines", 34]]

#1.Write a program that has a list of shopping lists where each list is for a 
#different food group.
#Print each full list on a seperate line.

# shopping = [
#     ["rice", "bread", "quinoa"], 
#     ["apples", "oranges", "grapes"], 
#     ["chicken", "beef", "fish",]
# ]
# for lists in shopping:
#     print(lists)



#2.Using the code from the previous exercise, have each grouping have a title with 
# the number in the title and each item of the list have a number in front of the item.
# (bonus) Have each of the titles of the main grouping be in a 
#seperate list that gives the name to the heading.

# shopping = [
#     ["rice", "bread", "quinoa"], 
#     ["apples", "oranges", "grapes"], 
#     ["chicken", "beef", "lamb",]
# ]
# index = 0
# for lists in shopping:
#     index += 1
#     print(index , + lists) 

shopping_list = ["Carbs", "Fruit", "Meat"]

# first_food_group = ["rice", "bread", "quinoa"]
# second_food_group = ["apples", "oranges", "grapes"]
# thrid_food_group = ["chicken", "beef", "lamb"]

shopping_group = [
    ["rice", "bread", "quinoa"],
    ["apples", "oranges", "grapes"],
    ["chicken", "beef", "lamb"]]

j = 0
for list in shopping_list:
    i = 0
    print("%i. %s" %(j+1, list))
    for food in shopping_group[j]:
        #for food in group:
            #if i <= len(food):
        print("   %i. %s" %(i+1, food))
        i += 1
    j += 1    