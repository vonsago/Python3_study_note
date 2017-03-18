import turtle

def draw_square():
	window = turtle.Screen()
	window.bgcolor("black")
	
	pet = turtle.Turtle()
	pet.speed(2)
	pet.shape("turtle")
	pet.color("white")
	
	for i in range(4):
		pet.forward(100)
		pet.right(90)
	pet.left(90)
	for i in range(4):
		pet.forward(200)
		pet.left(90)
	window.exitonclick()

draw_square()
