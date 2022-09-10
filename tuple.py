# TODO: Question One:
# t = ('Java','Python','SQL','C')
# print(type(t))

# TODO: Question Two
# number = int(input('Enter:'))
# listOne = []
# for i in range(number):
#   listOne.append(input())

# tupleOne = tuple(listOne)
# print(tupleOne)
# print(type(tupleOne))

# Another Way
# a = tuple([(i) for i in input('Enter the value:').split(",")])
# print(a)
# print(type(a))

# TODO:3. Write a python program to reverse the tuple.
# tupleOne = (10,20,30,40,50)
# length = len(tupleOne)-1
# for i in range(length,-1,-1):
#   print(tupleOne[i])

  
# 4. Write a python program to Swap two tuples in Python.

# tupleOne = (10,20,30,40)
# tupleTwo = (50,60,70,80)

# a=10
# b=20
# tupleOne,tupleTwo = tupleTwo,tupleOne
# print(tupleOne)
# print(tupleTwo)

# 5. Write a python program to check if all items in the tuple are the same.

# tupleOne = (10,10,10,10,10)
# for i in range(len(tupleOne)):
#   if tupleOne[i] == 10:
#     pass

# print('All items are same')

# 6. Write a python program to divide the tuple into four variables.
# a,b,c,d=(100, 200, 300, 400)
# print(a,b,c,d, sep="\n")

# 7. Write a python program to copy elements 4 and 5 from the following tuple into a new tuple. 
# tuple1=(1,2,3,4,5,6)
# tupleOne = list(tuple1)
# listTwo= []
# for i in tupleOne:
#   if i ==4:
#     listTwo.append(i)
#   else:
#     if i ==5:
#       listTwo.append(i)
  
# finaTuple = tuple(listTwo)
# print(finaTuple)
# print(type(finaTuple))

# 9. Write a python program to print the value 20 from given nested tuple
# tuple1 = ("Python", [10, 20, 30], (2, 4, 16))

# for i in range(len(tuple1)):
#   if type(tuple1[i]) == list:
#     for m in range(len(tuple1[i])):
#       if tuple1[i][m] == 20:
#         print(tuple1[i][m],":", m)
      
    

# 10. Write a python program to change the first item (22) of a list within the following tuple to 222.
tuple1 = (11, [22, 33], 44, 55)
for i in range(len(tuple1)):
  if type(tuple1[i]) == list:
    for m in range(len(tuple1[i])):
      if tuple1[i][m] == 22:
        tuple1[i][m] = 222
        
print(tuple1)
print()

