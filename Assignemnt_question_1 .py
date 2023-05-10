# num = int(input("Enter the number : "))
# n1,n2 = 0,1
# count = 0
# if no <=0:
#     print("Entera positive number :")
# elif no ==1:
#     print("Fibonacci series",no,":")
#     print(n1)
# else:
#     print("Fibonacci Series :")
#     while count<no:
#         print(n1)
#         nth = n1+n2
#         n1=n2
#         n2=nth
#         count += 1
        
        
        
        
no = int(input("Enter the number : "))
n1,n2 = 0,1
count = 0
if no <=0:
    print("Entera positive number :")
elif no ==1:
    print("Fibonacci series",no,":")
    print(n1)
else:
    print("Fibonacci Series :")
    while count<no:
        print(n1)
        nth = n1+n2
        n1=n2
        n2=nth
        count += 1