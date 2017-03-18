import turtle

def draw_square():
	window = turtle.Screen()
	window.bgcolor("black")
	
	pet = turtle.Turtle()
	pet.speed(40)
	pet.shape("turtle")
	pet.color("white")
	apet=turtle.Turtle()
	apet.shape("turtle")
	apet.color("pink")
	apet.speed(20)
	
	for x in range(36):
		for i in range(4):
			pet.forward(100)
			pet.right(90)
		pet.right(10)
		if(x<=10):
			apet.circle(200)
			apet.right(36)
			

	window.exitonclick()

draw_square()
