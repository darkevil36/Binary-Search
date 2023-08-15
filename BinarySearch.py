import random
x = random.randint(1, 1000)
y = int(input("Guess The Number:"))
print("Note:The Number Is Between 1 and 1000")
while y > x or y < x :
	y = int(input("Try Again!!:"))
	if  y < x :
		print()
		print("The number is greater than you think!!")
	elif y > x :
		print()
		print("The number is less than you think!!")
if y == x :
   	print("Great!! You guessed the number!!")
    