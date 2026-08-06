import math

#get coordinates from the user
x1= float(input("Enter x1:"))
y1= float(input("Enter y1:"))
x2= float(input("Enter x2:"))
y2= float(input("Enter y2:"))

#Calculating the distance based on inputs
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

#Displaying results
print()
print(f"The distance between the two points is: {distance:.2f}")

#REFLECTION
#Because of the library, my work became more efficient. The functions became easier to process and it lessened the risk of human error. Without sqrt() and pow(), 
#I would have to manually type out a lengthy code