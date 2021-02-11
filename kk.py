going=True
def catmove(x):
	
	n="north"
	s="south"
	q="esth"
	e="easth"
	
	if n==x:
		print("you just move to  the north")
	elif s==x:
		print("you judt move to the south")
	elif q==x:
		print("you judt move to the esth")
	else: 
		print("you judt move to the easth")

def cat(food):
	global going

	if "fish"== food and going==True:
		going=True
		catmove('north')
		print("and eat "+food)
	elif "chicken"== food and going==True:
		going=True
		catmove('south')
		print("and eat "+food)
	elif "meat"== food and going==True:
		going=True
		catmove('esth')
		print("and eat "+food)


	elif "egg"== food and going==True:
		going=True
		catmove('easth')
		print("and eat "+food)
	else:
		print("you dont move at all")
		
cat('bread')