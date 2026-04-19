# def name(MyName):
#     print("Hello" ,MyName)

# name("Devyani")

# def add(a,b):
#     return(a+b)

# result= add(3,7)
# print(result)

# def even_or_odd(a):
#     if a % 2==0:
#         return("even")
#     if a % 2 !=0:
#         return("odd")
    
# result= even_or_odd(4679)
# print(result)

def prime(num):
    if num>1:
        for i in range(2, num):
            if num % i==0:
                return("This number is not prime")
        
        return("This number is Prime")
    else:
        return("Number is not a prime")
    
Result=prime(int(input("Enter a number: ")))
print(Result)

        