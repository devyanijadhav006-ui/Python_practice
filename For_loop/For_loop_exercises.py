# for i in range(0,21,2):
#     print(i, end=" ")


# rows = 5  # number of rows

# for i in range(1, rows + 1):      # outer loop for rows
#     for j in range(i):             # inner loop for stars
#         print("*", end="")         # print stars on same line
#     print()   

#multiplication Table
# num= int(input("Enter a number"))
# for i in range(1,11):
#     print(num, "X" ,i, "=", num*i)

# sum = 0
# for i in range(1, 21):
#     if i % 2 == 0:
#         sum += i
#         print(sum)

# num= int(input("ENter a number"))
# count =0
# #abs () Work with absolute value to handle negatives
# num=abs(num)
# for digit in str(num):
#     count +=1
#     print(count)


#Another way is 
# num = int(input("Enter a number: "))

# # Convert number to string and count length
# count = len(str(abs(num)))   # abs() handles negative numbers

# print("Number of digits:", count)

#Check Prime number

# num = int(input("Enter a number: "))
# if num>1:
#     for i in range(2, num):
#         if num % i ==0:
#             print ("number is not a prime number")
#             break
#     else:
#         print ("Number is a prime number")
# else:
#     print ("number is not a prime number")

# rows = 4  # number of rows
# for i in range(1, rows + 1):      # outer loop for rows
#     for j in range(1, i+1):
#         print (j, end=" " )
                                  
#     print()   

# rows= 5
# for i in range (rows, 0, -1):
#     for j in range(1,i+1):
#         print(j, end =" ")
#     print()

#Do while loop in python

# while True:
#     print("Hello")
    
#     choice = input("Continue? (y/n): ")
#     if choice == 'n':
#         break

# for i in range(1, 6):
#     if i % 2 == 0:
#         continue
#     print(i)

# for i in range(5):
#     print(i)
#     break

# for i in range(1, 4):
#     for j in range(1, 3):
#         print(i, j)

# for i in range(2):
#     for j in range(2):
#         print("*", end=" ")

count = 0
for i in range(1, 11):
    if i % 2 == 0:
        count += 1

print(count)