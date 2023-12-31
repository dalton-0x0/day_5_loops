# for loop with Lists
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit + " Pie")
print(fruits)

# average height exercise
student_heights = [156, 178, 165, 171, 187]

total_height = 0
for height in student_heights:
    total_height += height
print(f"total height: {total_height}cm")

number_of_students = 0
for _ in student_heights:
    number_of_students += 1
print(f"number of students: {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"average height: {average_height}cm")

# highest score exercise
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"highest score: {highest_score}%")

# for loop with range
for number in range(0, 11, 2):
    print(number)

# sum of all numbers from 1 to 100
sum_num = 0
for number in range(1, 101):
    sum_num += number
print("sum of numbers from 1 to 100:", sum_num)

# sum of all even numbers from 1 to 100
sum_even = 0
for number in range(2, 101, 2):
    sum_even += number
print("sum of even numbers from 1 to 100:", sum_even)
