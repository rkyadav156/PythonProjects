#Take input n fron user to insert elements as list
n=int(input("Enter the number of elements to be inserted: "))
# initialize an empty list
a=[]
# FOR loop to track elements
for i in range(0,n):
    elem=int(input("Enter element'i': "))
#appending elements in the empty list    
    a.append(elem)
#using average formula 
avg=sum(a)/n
#Getting the result printed
print("Average of elements in the list",round(avg,2))
#Ended Here