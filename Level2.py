# Problem 1 
# Question : Write a loop program to print  1 to 5 on one by one.
# Output  :     
#  1
#  2
#  3
#  4
#  5

# for i in range(1,6):
#     print(i)


#! Problem 2 
# Question : Write a loop program to print 5 to 1 on one by one.
# Output  :   
# 5
# 4
# 3
# 2
# 1

# for i in range(5,0,-1):
#     print(i)

#! Problem 3 
# Question : Write a loop program to print sum of 1 to 5.
# Output  : 15

# sum=0
# for i in range(1,6):
#     sum=sum+i
# print(sum)    

#! Problem 4 
# Question : Write a loop program to print sum of 6 to 1.
# Output  :    21

# sum=0
# for i in range(6,0,-1):
#     # print(i)
#     sum+=i
# print(sum)    

#! Problem 5 
# Question : Write a loop program to print odd numbers 1 to 9.
# Output  :   
# 1
# 3
# 5
# 7
# 9

# for i in range(1,10):
#     if i%2!=0:
#         print(i)

#! Problem 6 
# Question :  Write a loop program to print the two-digit odd numbers, below 
# 20.
# Output  :   
# 11
# 13
# 15
# 17
# 19

# for i in range(11,20,2):
#     print(i)


#! Problem 7 
# Question : Write a loop program to print the two-digit odd numbers, 
# who’s sum of digits are 7.
# Output  :   
# 25
# 43
# 61

# for i in range(10,100):
#     if i%2!= 0:
#         if ((i//10)+(i%10)==7):
#             print(i)

#! Problem 8
# Question : Write a loop program to print the two-digit even numbers, 
# who’s sum of digits are 6.
# Output  :
# 24
# 42
# 60

# for i in range(10,100):
#     if i%2==0:
#         sum=(i//10)+(i%10)
#         if sum==6:
#             print(i)

#! Problem 9
# Question :  Write a loop program to print the sum of two-digit numbers 
# whose one’s digit is 5.
# Output  :  495

# sum=0
# for i in range(15,100,10):
#     sum=sum+i
# print(sum)

#! Problem 10
# Question : Write a loop program to print the sum of two-digit odd numbers, 
# whose ten’s digit is 7.
# Output  :  375

# sum=0
# for i in range(70,80):
#     if i%2!=0:
#         sum=sum+i
# print(sum)    

#! Problem 11
# Question : Write a program to get a number from user print the total 
# number of digits in that number
# Output  :    
# Input : 123456 - Output – 6
# Input : 76895439- Output – 8
# Input : 675 – Output - 3

# num=int(input("Enter a number: "))   
# count=0
# for i in str(num):
#     count=count+1
# print(count)    

#! Problem 12
# Question :Write a program to get a number from user and print the sum 
# of all digits.
# Output  :  
# Input: 123456 - Output – 21
# Input: 76895439 - Output – 51
# Input: 675 – Output - 18

# num=int(input("Enter a number: "))
# sum=0
# for i in str(num):
#     sum=sum+int(i)
# print(sum)    

#another method
# num=int(input("Enter a number: "))
# sum=0
# while num>0:
#     digit=num%10
#     sum+=digit
#     num//=10
# print(sum)    

#! Problem 13
# Question :Write a program to get a number from user and print the 
# reverse of that number
# Output  :  
# Input : 123456 - Output – 654321
# Input : 76895439- Output – 93459867
# Input : 675 – Output - 576

# num=int(input("Enter a number: "))
# rev=0
# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10
# print(rev)  

#! Problem 14
# Question : Write a program to get a number from user and interchange the 
# first and last digits and print the result.
# Output  :  
# Input : 123456 - Output – 623451
# Input : 76895439- Output – 96895437
# Input : 675 – Output - 576

# num=input("Enter a number: ")
# print(num[-1]+num[1:-1]+num[0])
      
# another method

# num=int(input("Enter a number: "))
# temp=num
# count=0
# while temp>0:
#     count+=1
#     temp//=10
# first=num//(10**(count-1))
# last=num%10
# middle=(num%(10**(count-1)))//10
# result=last*(10**(count-1))+middle*10+first
# print(result)   

#! Problem 15

# Question :  Write a program to get a number from user and if the last digit of 
# the number is even print the same number. If the last digit of the number is 
# odd then subtract 1 from the last digit and print the number.
# (Note: Last digit -MSB) 
# Output  :  
# Input : 123456 - Output – 023456  Input : 96895439- Output – 86895439 
# Input : 675 – Output - 675 Input : 575 – Output - 475.

# num=int(input("Enter a number: "))
# temp=num
# count=0
# while temp>0:
#     count+=1
#     temp//=10
# first=num//(10**(count-1)) 
# last=num%10 
# middle=(num%(10**(count-1)))//10


# if first%2==0:
#     res=first*(10**(count-1))+middle*10+last
#     print(res)
# else:
#     res=(first-1)*(10**(count-1))+middle*10+last
#     print(res)    


#! Problem 16 

# Question :  Write a program get number from user print whether that number 
# is prime or not.
# Output  :   
# Input : 31 - Output : Prime
# Input : 27 - Output : Not Prime

# num=int(input("Enter a number: "))
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count+=1
# if count==2:
#     print("Prime")    
# else:
#     print("Not Prime")             

#! Problem 17

# Question :    Write a program to get a number from user, print whether that 
# number is prime, and sum of digit is equal to 14.
# Output  :   
# Input: 59 - Output: Prime & Sum of Digits is 14
# Input: 77 - Output: Not Prime but sum of digits is 14
# Input: 13 - Output: Prime, but sum of Digits is not 14

# num=int(input("Enter a number: "))
# temp=num
# sum=0
# count=0
# while temp>0:
#     digit=temp%10
#     sum+=digit
#     temp//=10

# for i in range(1,num+1):
#     if num%i==0:
#         count+=1
# if count==2 and sum==14:
#     print("Prime & Sum of Digits is 14")    
# elif count==2 and sum!=14:
#     print("Prime, but sum of digits is not 14")

# else:
#     print("Not Prime but sum of digits is 14")

#! Program 18
# Question : Write a program to get number from user, print whether that 
# number’s first two digits (ten’s digits and one’s digit) is prime.
# Output  :    
# Input: 359 - Output: Prime
# Input: 3577 - Output: Not Prime     

# num=int(input("Enter a number: "))
# digits=num%100

# count=0
# for i in range(1,digits+1):
#     if digits%i==0:
#         count+=1

# if count==2:
#     print("Prime")
# else:
#     print("Not Prime")

#! Problem 19
# Question :  Write a program to get a 4-digit number from user, print whether 
# that number’s middle two digits (hundred’s digit and ten’s digit) is prime.
# Output  :   
# Input: 6359 - Output: Not Prime
# Input: 3517 - Output: Prime
# num=int(input("Enter a four-digit number: "))
# middle=(num//10)%100
# count=0
# for i in range(1,middle+1):
#     if middle%i==0:
#         count+=1
# if count==2:
#     print("Prime")
# else:
#     print("Not prime")            

#! Problem 20
# Question : Write a program print total number of single digit Prime numbers
# Output  : 4

# count=0
# for i in range(2,10):
#     factors=0
#     for j in range(1,i+1):
#         if i%j==0:
#             factors+=1
#     if factors==2:
#         count+=1
# print(count)      

#! Problem 21  
# Question :   Write a program get number from user print the total number 
# digits which are odd in the number.
# Output  :   
# Input : 12345678 - Output : 4
# Input : 987531 - Output : 5

# num=int(input("Enter a number: "))         
# count=0
# while num>0:
#     digit=num%10

#     if digit%2!=0:
#         count+=1

#     num//=10
# print(count)                

#! Problem 22
# Question : Write a program get number from user print the total number 
# of two-digit odd numbers in the number.
# Output  :   
# Input: 12345678 - Output: 3
# Input: 987531 - Output: 4

# num=int(input("Enter a number: "))
# count=0
# while num>10:
#     digit=num%100
    
#     if digit%2!=0:
#         count=count+1
#     num//=10
# print(count)    

#! Problem 23

# Question : Write a program get number from user print the total number 
# of single-digit perfect square numbers in the number.
# Output  :  
# Input: 123456789 - Output: 3
# Input: 987531 - Output: 2   

# num=int(input("Enter a number: "))
# count=0
# while num>0:
#     digit=num%10

#     if digit==1 or digit==4 or digit==9:
#         count=count+1

#     num=num//10
# print(count)    

#! Problem 24
    
# Question :Write a program get number from user print the total number 
# of two-digit perfect square numbers in the number.
# Output  :   
# Input: 163496481 - Output: 4
# Input: 364925 - Output: 4

# num=int(input("Enter a number: "))
# count=0
# while num>=10:
#     digit=num%100
#     if digit==16 or digit==25 or digit==36 or digit==49 or digit==64 or digit==81:
#         count+=1
#     num//=10
# print(count)        

#! Problem 25

# Question : Write a program get number from user print the total number of 
# single-digit prime numbers in the number.
# Output  :   
# Input: 163496481 - Output: 1
# Input: 364925 - Output: 3

# num=int(input("Enter a number: "))
# count=0
# while num>0:
#     digit=num%10
#     if digit==2 or digit==3 or digit==5 or digit==7:
#         count+=1
#     num//=10    
# print(count)        

#! Problem 26
# Question : Write a program to print biggest 4-digit number which is 
# divisible by 7 and 9

# for i in range(9999,999,-1):
#     if i%7==0 and i%9==0:
#         print(i)
#         break


#! Problem 27
# Question :Write a program to print the total count of numbers which are 
# less than 100000 and whose sum of digits is 14.
# count=0
# for i in range(1,100000):
#     temp=i
#     sum=0

#     while temp>0:
#         digit=temp%10
#         sum=sum+digit
#         temp//=10

#     if sum==14:
#         count=count+1
# print(count)            

#! Problem 28

# Question :  Write a program to get two numbers from user and print the 
# LCM of those numbers. 
# num1=int(input("Enter a number: "))
# num2=int(input("Enter a number: "))
# max_num=max(num1,num2) 
# while True:
#     if max_num%num1==0 and max_num%num2==0:
#         print("LCM of two number is:",max_num)
#         break
#     max_num=max_num+1

#! Problem 29

# Question :Write a program to get three numbers from user and print the 
# LCM of those numbers.

# num1=int(input("Enter a number: "))
# num2=int(input("Enter a number: "))
# num3=int(input("Enter a number: "))
# max_num=max(num1,num2,num3)
# while True:
#     if max_num%num1==0 and max_num%num2==0 and max_num%num3==0:
#         print("LCM of three numbers is", max_num)
#         break
#     max_num+=1
    
#! Problem 30
    
# Question : Write a program to get two numbers from user and print the 
# HCF of those numbers.

# num1=int(input("Enter a number: "))
# num2=int(input("Enter a number: "))
# min_num=min(num1,num2)
# for i in range(min_num,0,-1):
#     if num1%i==0 and num2%i==0:
#         print("HCF of two numbers is ",i)
#         break





