# Problem 1 
# Question : Write a loop program to print 1 to 5 on one by one.
# Output  :     
# 1
# 2
# 3
# 4
# 5
# def main():
#     for i in range(1,5):
#         print(i)
# if __name__ =="__main__":
#     main()        

# Problem 2 
# Question : Write a loop program to print 5 to 1 on one by one.
# def main():
  
#     for i in range(5,0,-1):
#         print(i)
# if __name__ =="__main__":
#     main()        


#  Problem 3 
# Question : Write a loop program to print sum of 1 to 5.
# Output  : 15

# sum=0
# for i in range(1,6):
#     sum=sum+i
# print(sum)    

# Problem 4 
# Question :Write a loop program to print sum of 5 to 1.
# Output  : 21

# sum=0
# for i in range(5,0,-1):
#     sum=sum+i
# print(sum)    

# Problem 5 
# Question : Write a loop program to print odd numbers 1 to 9.
# Output  :     
# 1
# 3
# 5
# 7
# 9

for i in range(1,10):
    if i%2!=0:
        print(i)