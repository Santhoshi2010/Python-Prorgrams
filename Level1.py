#Problem 1--Question:Get a number from user and add 2 to that number and print the result.

# Testcase: Input:45 Output:47
#           Input:56789  Output:56791

# x=int(input("Enter Number: "))
# y=2+x
# print(f"Result={y}")

# Problem 2--Question: Get a number from user and subtract 5 to that number and 
# print the result.
# Testcase :     Input :45 Output 40.  Input: 56789 Output: 56784
# def main():
#     x = int(input("Enter Number: "))
#     y=x-5
#     print(f"Result = {y}")
# if __name__ == "__main__":
#     main()

# Problem 3-- Question : Get a number from user and multiply 3 to that number and 
# print the result.
# Testcase : Input: 45 Output 135. Input: 1200 Output: 3600

# def main():
#     x = int(input("Enter Number: "))
#     y=x*3
#     print(f"Result = {y}")
# if __name__ == "__main__":
#     main()

# Problem 3--Question : Get a number from user and divide by the number by 6 and 
# print the quotient.
# Testcase :   Input: 45 Output 7. Input: 143 Output: 23

# def main():
#     x = int(input("Enter Number: "))
#     y=int(x/6)
#     print(f"Result = {y}")
# if __name__ == "__main__":
#     main()

# Problem 4--Question : Get a number from user and divide by the number by 8 and 
# print the remainder.
# Testcase : Input: 45 Output 5. Input: 143 Output: 7    
# def main():
#     x = int(input("Enter Number: "))
#     y=int(x/8)
#     print(f"Result = {y}")
# if __name__ == "__main__":
#     main()

# Problem 5-- Question :    Get a two-digit number from user and print the one’s digit.
# Testcase :   Input: 45 Output 5. Input: 56 Output: 6
# def main():
#     x = int(input("Enter a two-digit number: "))
#     y = x%10
#     print(f"Result = {y}")
# if __name__ == "__main__":
#     main()

# Problem 6--Question : Get a two-digit number from user and print the ten’s digit.
# Testcase : Input: 45 Output 4. Input: 56 Output: 5

# def main():
#     x = int(input("Enter a two-digit number: "))
#     y=x//10
#     print(f"Result = {y}")
# if __name__ == "__main__":
#     main()

# Problem 8--Question : Get a three-digit number from user and print the one’s digit.
# Testcase : Input: 456 Output 6. Input: 569 Output: 9
# def main():
#     x = int(input("Enter a three-digit number: "))
#     y = x%10
#     print(f"Result = {y}")
# if __name__ == "__main__":
#     main()

# Problem 9--Question :  Get a three-digit number from user and print the hundred’s 
# digit.
# Testcase : Input: 456 Output 4. Input: 569 Output: 5

# def main():
#     x = int(input("Enter a three-digit number: "))
#     y=x//10
#     res=y//10
#     print(f"Result = {res}")

# if __name__ == "__main__":
#     main()

# Problem 10-- Question : Get a three-digit number from user and print the ten’s digit.
# Testcase : Input: 456 Output 5. Input: 569 Output: 6


# def main():
#     x = int(input("Enter a three-digit number: "))
#     y=(x//10)%10
  
#     print(f"Result = {y}")
# if __name__ == "__main__":
#     main()

# Problem 11--Question :    Get a two-digit number from user and print sum the digits.
# Testcase :    Input: 56 Output 11. Input: 69 Output: 15

# num=int(input("Enter a two-digit Number: "))
# sum=0
# while num>0:
#     dig=num%10
#     sum=sum+dig
#     num=num//10
# print(sum)

# Problem 12--Question : Get a three-digit number from user and print sum the digits.
# Testcase : Input: 562 Output 13. Input: 469 Output: 19
# num=int(input("Enter a a three-digit number: "))
# sum=0
# while num>0:
#     digit=num%10
#     sum=sum+digit
#     num=num//10
# print(sum)    

# Problem 13--Question : Get a two-digit number from user and print the reverse of the 
# number.
# Testcase : Input: 56 Output 65. Input: 59 Output: 95
# num=int(input("Enter a two-digit number:"))
# rev=0
# while num>0:
#     last_digit=num%10
#     rev=rev*10+last_digit
#     num=num//10
# print(rev)    

# Problem 14--Question : Get a three-digit number from user and print the reverse of the 
# number.
# Testcase :  Input: 561 Output 165. Input: 859 Output: 958

# num=int(input("Enter a three-digit number:"))
# rev=0
# while num>0:
#     last_dig=num%10
#     rev=rev*10+last_dig
#     num=num//10
# print(rev)    

# Problem 15--Question :      Get a four-digit number from user and only reverse the
# first two digits of the number, then print the number.
# Testcase :  Input: 9561 Output 9516. Input: 3859 Output: 3895
# num=int(input("Enter a four-digit number: "))
# first=num//100 #9561//100=95
# last=num%100 #9561%100=61
# reverse=(last%10)*10 + (last//10) #16
# rev_num=first*100+reverse


# print(rev_num) 

# Problem 16--Question :Get a four-digit number from user and only reverse the
# first two digits of the number, then print the number.
# Testcase :  Input: 9561 Output 9516. Input: 3859 Output: 389   

# num=int(input("Enter a  four-digit number: "))
# last=num%100 #61
# first=num//100 #95
# reverse=(first%10)*10+(first//10) #59
# res=reverse*100+last
# print(res)

# Problem 17--Question : Get a two-digit number from user and make the one’s digit as 
# 0, then print it.
# Testcase :  Input: 95 Output 90. Input: 18 Output: 10

# num=int(input("Enter a two-digit number: "))
# x=num//10
# res=x*10

# print(res)


# Problem 18--Question : Get a two-digit number from user and make the ten’s digit 1,
# then print it.
# Testcase : Input: 95 Output 15. Input: 82 Output: 12

# num=int(input("Enter a number: "))
# x=num%10
# res=x+10
# print(res)

# Problem 19--Question: Get a three-digit number from user and make the one’s digit 
# as 2, then print it.
# Testcase : Input: 695 Output 692. Input: 182 Output: 18
# num=int(input("Enter a three digit number: "))
# x=num//10 
# res=x*10+2
# print(res)

# Problem 20 --Question : Get a three-digit number from user and make the ten’s digit as 
# 0, then print it.
# Testcase :Input: 695 Output 605. Input: 182 Output: 102

# num=int(input("Enter a three-digit number: "))
# x=num//100*100
# last=num%10
# res=x+last
# print(res)

# Problem 21--Question :Get a number from user and subtract 5 from that number if 
# the number is odd, then print the result. Do not use “if”. 
# Testcase : Input: 695 Output 690. Input: 182 Output: 182

# num=int(input("Enter a number: "))
# while(num%2!=0):
#     num=num-5
# print(num)    

#Problem 22--Question : Get a number from user and subtract 5 from that number if 
# the number’s ten’s position digit is odd, then print the result. Do not use “if”. 
# Testcase : Input: 685 Output 685. Input: 89172 Output: 89167

# num=int(input("Enter a number: "))
# a=num//10
# print(a) #68 ,8917
# b=a%10
# print(b) #8, 7
# c=b%2
# print(c) #0,1
# d=5*c
# print(d) #0,5

# result=num-d
# print(result)

#Problem 23--Question : Get a two digit number from user and subtract 5 from that 
# number if the sum of the digits of the number is odd, then print the result. 
# Do not use “if”.
# Testcase : Input: 95 Output 95. Input: 72 Output: 67

# num=int(input("Enter a two-digit number: "))
# temp=num
# sum=0
# while num>0:
#     digit=num%10
#     sum=sum+digit
#     num=num//10
# result=temp-(5*(sum%2))
# print(result)
  
#Problem 24--Question : Get a three-digit number from user and subtract 5 from that 
# number if one’s digit number and 100’s digit number are same, then print the
# result. Do not use “if”. 
# Testcase : Input: 595 Output 590. Input: 372 Output: 372

# num=int(input("Enter a three-digit number: "))
# a=num%10 #5
# # print(a)
# b=num//100 #5
# # print(b)
# result=num-(5 *(a==b))
# print(result)    

#Problem 25--Question :  Get a four-digit number from user and subtract 5 from that 
# number if ten’s digit position and 100’s digit position is same, then print the 
# result. Do not use “if”. 
# Testcase : Input: 7595 Output 7595. Input: 3772 Output: 3767

# num=int(input("Enter a four-digit number: "))
# x=num%100
# tens=x//10 #7 tens place

# z=num//100 #37
# hunderds=z%10

# result=num-(5*(tens==hunderds))

# print(result)

#Problem 26--Question : Get a two-digit number from user. If the sum of the digits is 10 
# then print “Success”, otherwise print “Failure”.
# Testcase :Input: 56 - Output Failure. Input: 37 - Output: Success.

# num=int(input("Enter a two-digit number: "))
# sum=0
# while num>0:
#     digit=num%10
#     sum+=digit
#     num//=10
# if sum==10:
#     print("Success")
# else:
#     print("Failure")    

#Problem 27--Question : Get a three-digit number from user. If the sum of the digits is 
# 10 then print “Success”, otherwise print “Failure”.
# Testcase :      
# Input: 956 - Output: Failure.  Input: 127 - Output: Success

# num=int(input("Enter a three-digit number: "))
# sum=0
# while num>0:
#     digit=num%10
#     sum+=digit
#     num//=10
# if sum==10:
#     print("Success")
# else:
#      print("Failure")    

# Problem 28--Question : Get a three-digit number from user. If the sum of the one’s 
# digit and hundred’s digit is less than 10, then print “Success”, otherwise print
# “Failure”.
# Testcase : Input: 569 - Output Failure. Input: 316 - Output: Success 

# num=int(input("Enter a three-digit number: "))

# ones=num%10 #9
# # print(ones)
# hunderds=num//100 #5
# # print(hunderds)
# sum=ones+hunderds
# if sum<10:
#     print("Success")
# else:
#     print("Failure")    

# Problem 29--Question : Get a four-digit number from user. If the sum of the ten’s digit 
# and hundred’s digit is greater than 10, then print “Success”, otherwise print
# “Failure”.
# Testcase :      
# Input: 7529 – Output: Failure. Input: 9386 - Output: Success

# num=int(input("Enter a four-digit number: "))
# tens=(num%100)//10
# hunderds=(num//100)%10
# sum=tens+hunderds
# if sum>10:
#     print("Success")
# else:
#     print("Failure")    

# Problem 30--Question : Get a four-digit number from user. If the sum of the ten’s digit 
# and hundred’s digit is equal to 10, and one of the digits is more than 7 then
# print “Success”, otherwise print “Failure”.
# Testcase : Input: 4649 – Output: Failure. Input: 9286 - Output: Success.

# num=int(input("Enter a four-digit number: "))
# tens=(num%100)//10
# hunderds=(num//100)%10
# sum=tens+hunderds
# if (sum==10) and (tens>7 or hunderds>7):
#     print('Success')
# else:
#     print("Failure")    

# Problem 31--Question : Get a three-digit number from user. If the sum of the digits is 
# less than 10, then print the sum, otherwise add the digits of the sum. If the 
# sum of the digits is less than 10, then print the sum, otherwise add the digits 
# of the sum, and print the sum.
# Note: The result should be always single digit only. 
# Testcase :
# Input: 123 – Output: 6
# Input: 149 - Output: 5 (149:1+4+9 = 14: 1+4 = 5)
# Input: 991 - Output: 1 (991: 9+9+1 = 19: 1+9 = 10: 1+0 = 1)

# num=int(input("Enter a three-digit number: "))
# sum=0
# while num>0:
#     digit=num%10
#     sum+=digit
#     num//=10
# if sum<10:
#     print(sum)    
# else:
#     sum=(sum//10)+(sum%10)
#     if sum<10:
#         print(sum)
#     else:
#         sum=(sum//10)+(sum%10)
#         print(sum)


# Problem 32:Question : Get two 2-digit numbers from user. If the sum of the numbers is 
# less than 100, then print the sum, otherwise print the difference.
# Testcase : Input: 56 78 – Output: 22 Input: 14 65 - Output: 79

# num1=int(input("Enter a number: "))
# num2=int(input("Enter a number: "))
# sum=num1+num2
# if sum<100:
#     print(sum)
# else:
#     print(abs(num1-num2))    


# Problem 33--Question :Get two 2-digit numbers from user. Print the sum of digits of 
# the biggest number.
# Testcase :     
# Input: 56 78 – Output: 15
# Input: 14 65 - Output: 11

# num1=int(input("Enter a two-digit number: "))
# num2=int(input("Enter a two-digit number: "))

# sum1=(num1//10)+(num1%10)
# sum2=(num2//10)+(num2%10)
# # print(sum1)
# # print(sum2)

# if sum1>sum2:
#     print(sum1)
# else:
#     print(sum2)    

# Problem 34--Question : Get two 3-digit numbers from user. Print the difference 
# between the one’s digit and
# hundred’s digit of the number whose ten’s digit is bigger than the other 
# number’s ten’s
# digit
# Testcase :      
# Input: 856 978 – Output: 1
# Input: 128 365 - Output: 2

# num1=int(input("Enter a three-digit number: "))
# num2=int(input("Enter a three-digit number: "))

# tens1=(num1%100)//10
# tens2=(num2%100)//10
# # print(tens1)
# # print(tens2)
# if tens1>tens2:
#     hunderds=num1//100
#     ones=num1%10
# else:
#     hunderds=num2//100
#     ones=num2%10
# print(abs(hunderds-ones))  

# Problem 35 --Question : Get two 3-digit numbers from user. Add the one’s and 
# hundred’s digits of both the numbers. Print the sum of all the digits of the 
# number whose sum of one’s and hundred’s digits is bigger.
# Testcase :    
# Input: 856 978 – Output: 24
# Input: 128 365 - Output: 11

num1=int(input("Enter a three-digit number: "))
num2=int(input("Enter a three-digit number: "))
hunderds1=num1//100
ones1=num1%10
sum1=hunderds1+ones1
hunderds2=num2//100
ones2=num2%10
sum2=hunderds2+ones2
if sum1>sum2:
    result=(num1//100)+((num1//10)%10)+(num1%10)

else:
    result=(num2//100)+((num2//10)%10)+(num2%10)  

print(result)  
print(num1)  




       


