#Problem 1 
# Question :Get a number from user and add 2 to that number and print the 
# result. Write your code inside the function. Do not Change the Code. 
# Output : Input :45 Output 47. 
# Input:56789 Output:56791 

# def function(no1):
# # Define and initialize no2
#     no2 = 0
# # Your Program Here
#     no2=no1+2
#     return no2
# def main():
#     number1 = int(input("Enter a number: "))
#     number2 = function(number1)
#     print(number2)
# if __name__ == "__main__":
#     main()


#Problem 2 
# Question :Get a number from user and subtract 5 to that number and print 
# the result. Write your code inside the function.
# Output  :   Input :45 Output 40. Input:56789 Output:56784

# def function(no1):
#     no2 = 0
#     # Your Program Here
#     no2=no1-5
#     return no2

# def main():
#     number1 = int(input("Enter a number: "))
#     number2 = function(number1)
#     print(number2)
# if __name__ == "__main__":
#     main()

#Problem3
# Question :Get a number from user and Check whether the sum of digits is 
# 14 and print the result. Write your code inside the function. Do not Change 
# the format.
# Output  :   Input: 59 Output: Sum of Digits is 14. Input :123 Output: Sum of 
# digits is not 14

# def sum14(no):
#     sum=0
#     while no>0:
#         digit=no%10
#         sum=sum+digit
#         no=no//10
#     if sum== 14:
#         return 1
#     else:
#         return 0
# def main():
#     number = int(input("Enter a number: "))
#     result = sum14(number)
#     if result == 1:
#         print("Sum of Digits is 14")
#     else:
#         print("Sum of Digits is not 14")
# if __name__ == "__main__":
#     main()

#Problem 4 
# Question :Get a number from user and Check Prime or Not and print the 
# result. Write your code inside the function. Do not Change the format.
# Output: Input: 61 Output Number is Prime. Input: 1200 Output: Number is 
# not Prime.

# def is_prime(num):
#     if num<2:
#         return False
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             return False
#     return True    

# def main():
#     number = int(input("Enter a number: ")) 
#     result = is_prime(number)
#     if result:
#         print(f"{number} is a prime number.")
#     else:
#         print(f"{number} is not a prime number.")
# if __name__ == "__main__":
#     main()

#Problem 5 
# Question :Get a number from user and count the number of zeros in that 
# number and print. Write your code inside the function. Do not Change the
# format.
# Output  :  Input: 100 Output: 2 . Input: 1060030 Output: 4.

# def find_number_of_zeros(num):
#     count=0
#     while num>0:
#         digit=num%10
#         if digit==0:
#             count=count+1
#         num=num//10
#     return count    
# def main():
#     number = int(input("Enter a number: "))
#     result = find_number_of_zeros(number)
#     print(result)
# if __name__=="__main__":
#     main()    

# Problem 6 
# Question :Get a number from user and reverse that number and print. Write 
# your code inside the function. Do not Change the format.
# Output  :   Input: 123 Output: 321. Input: 56789 Output: 98765.

# def reverse_number(num):
#     rev=0
#     while num>0:
#         digit=num%10
#         rev=rev*10+digit
#         num//=10
#     return rev    
# def main():

#     number = int(input("Enter a number: "))
#     result = reverse_number(number)

#     print(f"The reversed number is: {result}")
# if __name__ == "__main__":
#     main()

#  Problem 7 
# Question :Get two numbers from user and compare the numbers. If same 
# print “Same” otherwise print “Not Same”. Write your code inside the function. Do not Change the format.
# Output  : Input: 123, 123 Output: Same. Input: 56789,12345 Output: “Not Same”


# def function(no1):
#     no2 = int(input("Enter another number: "))
#     if no1 == no2:
#         print("Same")
#     else:
#         print("Not Same")    
#     # return no2

# def main():
#     number1 = int(input("Enter a number: "))
#     number2 = function(number1)
#     # print(number2)
# if __name__ == "__main__":
#     main()


# Problem 8 
# Question :Get a number from user and check whether the digits are in ascending order.
# Output  :  Input: 1234 Output: Yes. Input: 5687 Output: No

# def check_assending(no):
#     temp=no
#     prev=10
#     while temp>0:
#         digit=temp%10
#         if digit>prev:
#             return "No"
#         prev=digit
#         temp=temp//10
#     return "Yes"       
# def main():
#     number1 = int(input("Enter a number: "))
#     print(check_assending(number1))
    
# if __name__ == "__main__":
#     main()

# Problem 9 
# Question :Get a two-digit number from user swap the digits.
# Output  :  Input: 34 Output: 43. Input: 56 Output: 65

# def swapNumbers(no):
#     number2=int(input("Enter a two-digit number: "))
#     no,number2=number2,no
#     return no,number2
# def main():
#     number1=int(input("Enter two-digit number: "))
#     result1,result2=swapNumbers(number1)
#     print(f"Swapped numbers are: {result1} and {result2}")
# if __name__=="__main__":
#     main()  

# Problem 10 
# Question : Get a number from user, find the number of digits and print the same.
# Output  : Input: 34678 Output: 5. Input: 12345678 Output: 8

def count_Digits(no):
    count=0
    while no>0:
        digit=no%10
        count+=1
        no//=10
    return count
def main():
    number=int(input("Enter a number: "))
    print(count_Digits(number))
if __name__=="__main__":
    main()
