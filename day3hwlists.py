# Question 1 Task 1

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort (reverse=True)
print(grades)

# Question 1 Task 2 

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
print((sum(grades))/len(grades))

# Question 2

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

common_elements = [element for element in submitted if element in attended]
print(common_elements)

    
    



#Question 3 Task 1

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
week_2temps = temperatures[7:14]
print(week_2temps)

#Question 3 Task 2

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
high_temps = temperatures[24:29]
print(high_temps)


