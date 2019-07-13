# Implementation of  Linear Search using Brute Force Approach in Python
# date created :13 July 2019

""" Taking Input """
n=int(input("Enter the number of items :"))
items=[]
while n>0 :
  m=int(input("Enter items in the list :"))
  items= items+ [m]
  n=n-1
  
""" Printing the inputed Items """
print("list of items are :",items)

""" Main Linear Search code using Brute Force Approach """
x=int(input("Enter item to be searched :")) 
i=flag=0
while i<len(items):
  if items[i]==x:
    flag=1
    break
  i=i+1

""" Making the user update about the output of the search """
if flag==1:
  print("Item found at Position :",i+1)
else:
  print("Item not Found")
  
