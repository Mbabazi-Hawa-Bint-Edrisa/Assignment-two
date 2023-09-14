#python program 
#change item 80 to 89 in the list

student_marks = [60 , 80 , 90 , 98]
student_marks[1] = 89
print(student_marks)


#add/append a new item 55 to the list 

student_marks = [60 , 80 , 90 , 98]
student_marks.append(55)
print(student_marks)


#find the size of the list having appended item 55

print(len(student_marks))


#write a program to sum all items in that list 

student_marks =[60 , 80 , 90 , 98]
list_sum = sum(student_marks)
#print the sum

print("The sum of all the items in the list is:",list_sum )


#write a function that takes two lists and returns two if they have atleast one common member

list1 = input("Enter items:")
print(list1)

list2 = input("Enter items:")
print(list2) 

#check  if the is a common member 
common_member = 2 
print(common_member)
print("The common member is" + "" + str(common_member))

