from turtle import Turtle
FONT=("Courier",24,"normal")



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.update()
        
    def update(self):
        self.clear()
        self.write(f"level:{self.level}",align="left",font=FONT)
    
    def increase_level(self):
        self.level+=1
        self.update()
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",align="center",font=FONT)

        