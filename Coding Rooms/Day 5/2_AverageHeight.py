# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest = 0
for x in range(0, len(student_scores)):
    if(student_scores[x] > highest):
        highest = student_scores[x]
print("The highest score in the class is: "+ str(highest))

#print(max(student_scores))



