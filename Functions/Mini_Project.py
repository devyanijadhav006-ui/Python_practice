#Fuction to calculate Total
def calculate_total(m1, m2, m3):
    return(m1+m2+m3)

#Function to calculate percentage
def cal_percetage(total):
    return(total/3)

#function to assign garde
def get_grade(percentage):
    if percentage >=90:
        return("A")
    elif percentage>=75:
        return("B")
    elif percentage>=50:
        return("C")
    else:
        ("Kid is failed")

#main:

name= input("Name of the Student: ")
m1= float(input("Enter marks 1"))
m2= float(input("Enter marks 2"))
m3= float(input("Enter marks 3"))
 
total= calculate_total(m1, m2,m3)
percentage= cal_percetage(total)
grade= get_grade(percentage)

print("\n--- Result ---")
print("Name:", name)
print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)
