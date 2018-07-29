n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
  element=int(input("Enter the element: "))
  a.append(element)
avg=sum(a)/n
print("Average",round(avg,2))
