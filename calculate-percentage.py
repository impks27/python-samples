name=input("Enter name: ")
print("Name: ", name)
num=int(input("Enter total number of subjects: "))
a=[]
for i in range(0,num):
  element=int(input("Enter subject marks: "))
  a.append(element)
percentage=sum(a)/num
print("Percentage: ",round(percentage,2))
