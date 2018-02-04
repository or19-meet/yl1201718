a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for number in a:
	if number<5:
		print(number)

print("exercise done!")
##extras:
#a
b=[]
for number in a:
	if number<5:
		b.append(number)
print(b)
print("exercise done!")

#b
c=[]
Number = input("choose a number")
for number in a:
	if Number<number:
		c.append(Number)
		print(c)





