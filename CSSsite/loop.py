print("What is a word that you would like me to spell?")
a = input()
for i in a:
	print(i)

def function1():
	c = 1
	while c < 6:
		print("Hi " + str(c))
		c += 1

function1()

b = input("what would you like to multiply by 2?")

def multifunction(x):
	return (2*x)

print(multifunction(int(b)))

