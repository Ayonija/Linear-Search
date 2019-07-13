# Implementation of  Linear Search using Brute Force Approach in Python
# date created :13 July 2019
n=int(input("Enter the number of items :"))
items=[]
while n>0 :
  m=int(input("Enter items in the list :"))
  items= items+ [m]
  n=n-1
print("list of items are :",items)
x=int(input("Enter item to be searched :")) 
i=flag=0
while i<len(items):
  if items[i]==x:
    flag=1
    break
  i=i+1
if flag==1:
  print("Item found at Position :",i+1)
else:
  print("Item not Found")
